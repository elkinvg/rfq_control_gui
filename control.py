#!/usr/bin/env python
# -*- coding: utf-8 -*-

# class LedIndicator(QtGui.QWidget):
#     def __init__(self, status):
from PyQt4 import QtCore, QtGui
import PyTango
import ui_control
import setting
import json
import time
import datetime
import os
from threading import Thread, Timer

server_name = setting.server_name
json_get = setting.json_get
MDEBUG = setting.MDEBUG
MODBUSOUT = setting.MODBUSOUT
TEXTEDIT = setting.TEXTEDIT
fontSize = setting.fontSize
timer_sec = setting.timer_sec * 1000

sizeWindowWithEdit = setting.sizeWindowWithEdit
sizeWindowWithoutEdit = setting.sizeWindowWithoutEdit

class Main_Control2(ui_control.Ui_MainWindow):
    def __init__(self):
        self.frame_Protect_Main.setEnabled(False)
        self.Volt_Set_lineEdit.setText()
        # self.cur_Get_lcdNumber.setRa
        self.frame_2.show()


class Main_Control(object):
    def __init__(self,uic):

        try:
            self.dev = PyTango.DeviceProxy(server_name)
        except PyTango.DevFailed as exc:
            self.exceptionDialog(exc)
            return

        # включает отклюает панель защиты. Если истина, панель блокируется.
        self.protect_Status = False
        # установка в True, когда все элементы системы включены (лампочки зеленые)
        self.system_Status = False
        # блокировка кнопки вентилятора
        self.ventil_block = False
        # статус включения накала (влияет на блокировку кнопки ВНМ)
        self.heat_block = False
        # статус включения ВНМ
        self.rfq_block = False

        self.firstRun = True

        self.uic = uic

        # # установка валидатора
        # vd = QtGui.QIntValidator()
        # vd.setRange(0,65535)
        # self.uic.cur_Set_lineEdit.setValidator(vd)
        # self.uic.Volt_Set_lineEdit.setValidator(vd)
        # # парсинг строки статусов и значений регистров и флагов
        # self.parsed_json = {}

        # Свойства для установки тока и напряжения
        self.uic.cur_Set_lineEdit.setMinimum(0)
        self.uic.cur_Set_lineEdit.setMaximum(60000)
        self.uic.cur_Set_lineEdit.setSingleStep(10)
        # self.uic.cur_Set_lineEdit.setSuffix('mA')

        self.uic.Volt_Set_lineEdit.setMinimum(0)
        self.uic.Volt_Set_lineEdit.setMaximum(60000)
        self.uic.Volt_Set_lineEdit.setSingleStep(100)

        # BUNCHER
        # Свойства для установки тока и напряжения
        self.uic.cur_Set_lineEdit_Buncher.setMinimum(0)
        self.uic.cur_Set_lineEdit_Buncher.setMaximum(60000)
        self.uic.cur_Set_lineEdit_Buncher.setSingleStep(10)
        # self.uic.cur_Set_lineEdit.setSuffix('mA')

        self.uic.Volt_Set_lineEdit_Buncher.setMinimum(0)
        self.uic.Volt_Set_lineEdit_Buncher.setMaximum(60000)
        self.uic.Volt_Set_lineEdit_Buncher.setSingleStep(100)


        # блокировка панелей включения и установки
        # self.setEnabledPanels( self.uic,False)
        self.setDisablePanels()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(timer_sec)

        self.dict = {}
        self.dictBut = {}
        self.dict_vent = {}
        # инициализация словаря регистров для Индикаторов защиты
        self.leds = []#['X0','X1','M24','X12','X13','M25']
        self.blk_ventil = [] #['X0','X1','M24']
        self.blk_heat = [] #['X0','X1','M24','X12','X13','M25','M3']
        self.blk_rfq = [] #['X0','X1','M24','X12','X13','M25','M3','M1']
        self.initDictOfLedsAndButton()

        # Скрытие тектового вывода
        if TEXTEDIT == False:
            self.uic.frame_2.hide()
            self.uic.outtextRadioButton.setChecked(False)
        else:
            self.uic.outtextRadioButton.setChecked(True)

        # установка размера шрифта в выводе
        font = QtGui.QFont()
        font.setPointSize(fontSize)
        self.uic.output_textBrowser.setFont(font)

        self.setSignalHandler()
        self.timer.start()


    def initDictOfLedsAndButton(self):
        #self.leds = ['X0','X1','M24','X12','X13','M1','M3','M5'] #25?
        # self.leds = ['X0','X1','M24','X10','X11','X3','M25','M45','X15'] #25?
        self.leds = ['X0','X1','M24','X10','X11','X3','M25','M45','X13'] #25?
        self.blk_ventil = ['X0','X1','M24']
        self.blk_heat = ['X0','X1','M24','X10','X11','M45'] #M3->M45
        self.blk_rfq = ['X0','X1','M24','X10','X11','M25','M45','X3'] #M3->M45
        # self.rfq_statled = 'M5'
        # self.rfq_statled = 'X15'
        self.rfq_statled = 'X13'


        self.dict['X0'] = self.uic.protect_Door_Led
        self.dict['X1'] = self.uic.protect_Barbell_Led
        self.dict['M24'] = self.uic.protect_External_Led
        self.dict['X10'] = self.uic.protect_Transformator_Led
        self.dict['X11'] = self.uic.protect_Lamp_Led
        self.dict['M25'] = self.uic.protect_Vacuum_Led
        self.dict['X3'] = self.uic.heat_Status
        self.dict['M45'] = self.uic.ventil_Status
        # self.dict['M5'] = self.uic.bhm_Rfq_Status
        # self.dict['X15'] = self.uic.bhm_Rfq_Status
        self.dict['X13'] = self.uic.bhm_Rfq_Status

        self.dictBut['heat_pb'] = 'M1'
        self.dictBut['ventil_pb'] = 'M3'
        self.dictBut['Rfq_pb'] = 'M5'


    def setSignalHandler(self):
        QtCore.QTimer.connect(self.timer,QtCore.SIGNAL("timeout()"),self.getInfoFromServerInJson)
        self.uic.ventil_pushButton.clicked.connect(self.ventil_On)
        self.uic.heat_pushButton.clicked.connect(self.heat_On)
        self.uic.bhm_Rfq_pushButton.clicked.connect(self.bhm_Rfq_On)
        self.uic.cur_Volt_pushButton.clicked.connect(self.setCurVoltage)
        # self.uic.cur_Volt_pushButton.clicked.connect(self.test)
        self.uic.clearEdit_pushButton.clicked.connect(self.clearEdit)
        self.uic.clsSign.connect(self.clearEdit)
        self.uic.outtextRadioButton.toggled.connect(self.showOutput)

        # ??? !!!
        self.uic.cur_Volt_pushButton_Buncher.clicked.connect(self.setCurVoltage_Buncher)

    def showOutput(self):
        if (self.uic.outtextRadioButton.isChecked() == True):
            self.uic.frame_2.show()
            MainWindow.setFixedSize(sizeWindowWithEdit[0],sizeWindowWithEdit[1])
        else:
            self.uic.frame_2.hide()
            MainWindow.setFixedSize(sizeWindowWithoutEdit[0],sizeWindowWithoutEdit[1])


    def ventil_On(self):
        if self.rfq_block != 0:
            self.message_err(QtCore.QString.fromUtf8("Накал и ВНМ RFQ должны быть выключены"))
            return
        if self.parsed_json['argout'][0][self.dictBut['ventil_pb']] == 0:
            inn = [self.dictBut['ventil_pb'],"1"]
        else:
            inn = [self.dictBut['ventil_pb'],"0"]
        self.dev.command_inout("WriteRegisterOrFlag",inn)

    def heat_On(self):
        if self.system_Status == 1:
            self.message_err(QtCore.QString.fromUtf8("ВНМ RFQ должны быть выключены"))
            return
        if self.parsed_json['argout'][0][self.dictBut['heat_pb']] == 0:
            inn = [self.dictBut['heat_pb'],"1"]
        else:
            inn = [self.dictBut['heat_pb'],"0"]
        self.dev.command_inout("WriteRegisterOrFlag",inn)

    def bhm_Rfq_On(self):
        if self.parsed_json['argout'][0][self.dictBut['Rfq_pb']] == 0:
            inn = [self.dictBut['Rfq_pb'],"1"]
            # self.rfq_Status = 1
        else:
            inn = [self.dictBut['Rfq_pb'],"0"]
            # self.rfq_Status = 0
        self.dev.command_inout("WriteRegisterOrFlag",inn)

    def clearEdit(self):
        txt =  self.uic.output_textBrowser.toPlainText()
        self.save_to_logfile(txt)
        self.uic.output_textBrowser.clear()

    def test(self):
        val = self.uic.cur_Set_lineEdit.text()
        print("TEST:" + str(val))
        inn = ["D68",str(val)]
        aa = self.dev.command_inout("WriteRegisterOrFlag",inn)
        print(aa)
        val = self.uic.Volt_Set_lineEdit.text()
        inn = ["D66",str(val)]
        print("TEST2:" + str(val))
        aa = self.dev.command_inout("WriteRegisterOrFlag",inn)
        print(aa)

    def setCurVoltage(self):
        try:
            txt = "Установлены значения "
            val = self.uic.cur_Set_lineEdit.text()
            st = True
            if MDEBUG:
                print("TEST:" + str(val))
            inn = ["D68",str(val)]
            aa = self.dev.command_inout("WriteRegisterOrFlag",inn)
            txt = txt + " ток: <b>" + str(val) + "мА</b>, "
            st = st & aa
            if MDEBUG:
                print(aa)
            val = self.uic.Volt_Set_lineEdit.text()
            inn = ["D66",str(val)]
            if MDEBUG:
                print("TEST2:" + str(val))
            aa = self.dev.command_inout("WriteRegisterOrFlag",inn)
            txt = txt + " напряжение: <b>" + str(val) + "В</b><br>"
            st = st & aa
            if MDEBUG:
                print(aa)
            if st:
                self.send_to_textBrowser(QtCore.QObject.trUtf8(app, txt))
                # self.send_to_textBrowser(u"ППлоывралтыслвап")
        except PyTango.DevFailed as exc:
            if MDEBUG:
                print("exc in setCurVoltage")

    def setCurVoltage_Buncher(self):
        try:
            txt = "Установлены значения "
            val = self.uic.cur_Set_lineEdit_Buncher.text()
            st = True
            if MDEBUG:
                print("TEST:" + str(val))
            inn = ["D58", str(val)]
            aa = self.dev.command_inout("WriteRegisterOrFlag", inn)
            txt = txt + " ток: <b>" + str(val) + "мА</b>, "
            st = st & aa
            if MDEBUG:
                print(aa)
            val = self.uic.volt_Set_lineEdit_Buncher.text()
            inn = ["D106", str(val)]
            if MDEBUG:
                print("TEST2:" + str(val))
            aa = self.dev.command_inout("WriteRegisterOrFlag", inn)
            txt = txt + " напряжение: <b>" + str(val) + "В</b><br>"
            st = st & aa
            if MDEBUG:
                print(aa)
            if st:
                self.send_to_textBrowser(QtCore.QObject.trUtf8(app, txt))
                # self.send_to_textBrowser(u"ППлоывралтыслвап")
        except PyTango.DevFailed as exc:
            if MDEBUG:
                print("exc in setCurVoltage")

    def changedStatus(self):
        for key in self.leds:
            col = self.dict[key].getLedColor()
            if col == "green":
                stat = 1
            if col == "red":
                stat = 0
            # print self.parsed_json['argout'][0][key]
            # print stat
            if stat != self.parsed_json['argout'][0][key]:
                if key == 'X0':
                    mod = "Двери модулятора закрыты"
                elif key == 'X1':
                    mod = "Штанга повешена"
                elif key == 'M24':
                    mod = "Внешнее управление"
                elif key == 'X10':
                    mod = "Охлаждение накального трасформатора"
                elif key == 'X11':
                    mod = "Охлаждение лампы"
                elif key == 'M25':
                    mod = "Вакуум"
                elif key == 'M45':
                    mod = "Вентилятор"
                elif key == 'X3':
                    mod = "Накал"
                elif key == 'X13':
                    mod = "ВНМ RFQ"

                mes = "Статус <b>" + mod + "</b> поменялся на " + str(self.parsed_json['argout'][0][key]) + "<br>"
                self.send_to_textBrowser(QtCore.QObject.trUtf8(app, mes))

    def getInfoFromServerInJson(self):
        try:
            # dev = PyTango.DeviceProxy(server_name)
            # parsed_json = {}
            json_from_serv = self.dev.command_inout(json_get)

            # Проверка предыдущего статуса для предотвращения лишнего вывода
            prereadStatus = False
            if self.firstRun != True:
                prereadStatus = self.parsed_json['readStatus']
            self.parsed_json = json.loads(json_from_serv)
            readStatus = self.parsed_json['readStatus']

            # Вывод в случае изменения одного из статусов
            if (self.firstRun == False and readStatus==1 and prereadStatus==1):
                self.changedStatus()

            self.setLedColorStatus(self.parsed_json)
            self.set_LcdNumbers_Value()

            if self.firstRun:
                ddd = str(self.parsed_json['argout'][0]['D66'])
                # self.uic.Volt_Set_lineEdit.setText(ddd)
                self.uic.Volt_Set_lineEdit.setValue(int(ddd))
                ddd = str(self.parsed_json['argout'][0]['D68'])
                #self.uic.cur_Set_lineEdit.setText(ddd)
                self.uic.cur_Set_lineEdit.setValue(int(ddd))
                self.firstRun = False
                if (readStatus == 0):
                    mes = u"Нет соединения с контроллером"
                    self.send_to_textBrowser(mes)
                    # self.out_Value_regflags_toBrowser(self.parsed_json['readStatus'])
                # self.out_Value_regflags_toBrowser(self.parsed_json['argout'][0])

            if MODBUSOUT:
                self.out_Value_regflags_toBrowser(self.parsed_json['argout'][0])

        except PyTango.DevFailed as exc:
            self.setDisablePanels()
            self.parsed_json['readStatus'] = 0
            self.setLedColorStatus(self.parsed_json)
            self.set_LcdNumbers_Value()
            if MDEBUG:
                print("exc in getInfoFromServerInJson")
        except KeyError:
            # self.dev.command_inout("Init")
            if MDEBUG:
                print("key error in parsed_json")
            # print("key error in parsed_json")

    def setDisablePanels(self):
        # отключение панелей, если не все флаги состояния защиты активны
        self.uic.frame_System_Main.setEnabled(False)
        self.uic.frame_HighVoltage_Main.setEnabled(False)

    def set_LcdNumbers_Value(self):
        # Напряжение накала лампы выходного каскада ГВЧ ???
        val = self.parsed_json['readStatus']
        if val == 1:
            val = self.parsed_json['argout'][0]['D46']
            val = val/10.
            self.uic.system_lcdNumber.display(val)
            # напряжение на емкостях длинной линии модулятора RFQ
            val = self.parsed_json['argout'][0]['D98']
            self.uic.Volt_Get_lcdNumber.display(val)
            # ток заряда емкостей длинной линии модулятора RFQ
            val = self.parsed_json['argout'][0]['D9']/100.
            self.uic.cur_Get_lcdNumber.display(val)
            #??? !!! заряд банчер
            val = self.parsed_json['argout'][0]['D116']
            self.uic.Volt_Get_lcdNumber_Buncher.display(val)
        else:
            self.uic.system_lcdNumber.display(0)
            self.uic.Volt_Get_lcdNumber.display(0)
            self.uic.cur_Get_lcdNumber.display(0)

    def setLedColorStatus(self, parsed):
        # установка цветового статуса на лампы состяния элементов защиты
        isConnected = False
        phk = parsed.has_key('readStatus')
        pag = parsed.has_key('argout')
        if(phk):
            if (parsed['readStatus'] == 1):
                self.uic.connectStatus_Led.setLedColor("green")
                isConnected = True
            else:
                self.uic.connectStatus_Led.setLedColor("red")
                isConnected = False
        else:
            if MDEBUG:
                print("has not key readStatus")
            isConnected = False
            self.uic.connectStatus_Led.setLedColor("red")

        if isConnected == True:
            self.protect_Status = True
            self.system_Status = True
            self.ventil_block = True
            self.heat_block = True
            self.rfq_block = True
        else:
            self.protect_Status = False
            self.system_Status = False

        for key in self.leds:
            # включение выключение лампочек статусов
            # # if MDEBUG & phk & pag:
            # #     sys.stdout.write(" " + str(key) + "=" + str(parsed['argout'][0][key]))
            if isConnected:
                if parsed['argout'][0][key] == 1:
                    self.dict[key].setLedColor("green")
                else:
                    self.dict[key].setLedColor("red")
                    self.system_Status = False
            else:
                self.dict[key].setLedColor("red")
                self.protect_Status = False

        self.ventil_block = self.checkBlock(self.blk_ventil,self.ventil_block,isConnected,parsed)
        self.heat_block = self.checkBlock(self.blk_heat,self.heat_block,isConnected,parsed)
        self.rfq_block = self.checkBlock(self.blk_rfq,self.rfq_block,isConnected,parsed)

        # Включение выключение системной панели и панели установки напряжения модулятора
        # self.system_Status = self.system_Status & parsed['argout'][0][self.rfq_statled]

        self.uic.frame_System_Main.setEnabled(self.protect_Status)
        self.uic.frame_HighVoltage_Main.setEnabled(self.system_Status)

        self.uic.ventil_pushButton.setEnabled(self.ventil_block)
        self.uic.heat_pushButton.setEnabled(self.heat_block)
        self.uic.bhm_Rfq_pushButton.setEnabled(self.rfq_block)

    def checkBlock(self,btns,block,isConnected,parsed):
        for key in btns:
            if isConnected:
                block = block & parsed['argout'][0][key]
            else:
                return False
        return block

    def message_err(self,str):
        error = QtGui.QMessageBox(QtGui.QMessageBox.Critical,"Error",str,buttons = QtGui.QMessageBox.Ok)
        error.exec_()

    def messageException(self,exc):
        lenExc = len(tuple(exc))

        mes = QtCore.QString("<b>Exceptions:</b><br><br>")
        for k in range(0,lenExc):
            mes = mes + QtCore.QString("Exception"+str(k)+"<br>")
            # mes = mes + QtCore.QString("<b>Reason</b>: " + str(exc.args[k].reason) + "<br>")
            mes = mes + QtCore.QString("<b>Description</b>: " + str(exc.args[k].desc) + "<br>")
            # mes = mes + QtCore.QString("<b>Origin</b>: " + str(exc.args[k].origin) + "<br>")
            mes = mes + QtCore.QString("<br>")
        return mes

    def printException(self, exc):
        lenExc = len(tuple(exc))
        mes = self.messageException(exc)
        self.send_to_textBrowser(QtCore.QObject.trUtf8(app, mes))

    def exceptionDialog(self, exc):
        mes = self.messageException(exc)
        error = QtGui.QMessageBox(QtGui.QMessageBox.Critical,"Error",mes,buttons = QtGui.QMessageBox.Ok)
        error.exec_()

    def out_Value_regflags_toBrowser(self,parsedArgout):
        txt = ""
        for key in parsedArgout:
            txt = txt + "<b>" + str(key) + "</b>" + "->" + str(parsedArgout[key]) + "  "
        txt = txt + "<br><br>"
        self.send_to_textBrowser(txt)


    def save_to_logfile(self,strr):
        # self.output_textBrowser = QtGui.QTextBrowser(self.frame_2)
        if strr.count() == 0:
            return
        now = datetime.datetime.now()
        timeF = str(now.year) + str("%02d" % now.month) + str("%02d" % now.day)
        timeT = str("%02d" % now.hour) + str("%02d" % now.minute) + str("%02d" % now.second)

        if not os.path.exists("./log"):
            os.makedirs("./log")
        fnm = "log_" + timeF + timeT + ".out"
        f = open(str("./log/" + fnm),'w')
        f.write(strr.toUtf8())
        f.close()

    def send_to_textBrowser(self,txt):
        maxnum = 100000
        strr =  self.uic.output_textBrowser.toPlainText()
        if (strr.count() > maxnum):
            self.save_to_logfile(strr)
            self.clearEdit()
        ct = QtCore.QDateTime.currentDateTime()
        in_txt = "<b>" + ct.toString() + "</b>" + " " + txt;
        self.uic.output_textBrowser.append(in_txt)

class MyWindowQ(QtGui.QMainWindow):
    trigger = QtCore.pyqtSignal()
    def closeEvent(self, event):
        self.trigger.emit()
        event.accept()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = MyWindowQ()
    if TEXTEDIT == True:
        MainWindow.setFixedSize(sizeWindowWithEdit[0],sizeWindowWithEdit[1])
    else:
        MainWindow.setFixedSize(sizeWindowWithoutEdit[0],sizeWindowWithoutEdit[1])
    ui = ui_control.Ui_MainWindow()
    # ui = Main_Control()
    ui.setupUi(MainWindow)
    MainWindow.show()
    mc = Main_Control(ui)
    sys.exit(app.exec_())