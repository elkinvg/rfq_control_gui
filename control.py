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
from threading import Thread, Timer

server_name = setting.server_name
json_get = setting.json_get
MDEBUG = setting.MDEBUG
timer_sec = setting.timer_sec * 1000

class Main_Control2(ui_control.Ui_MainWindow):
    def __init__(self):
        self.frame_Protect_Main.setEnabled(False)
        self.connectStatus_Led.setLedColor()
        self.ventil_pushButton.clicked.connect()
        self.heat_pushButton.clicked.connect()
        self.bhm_Rfq_pushButton.clicked.connect()
        self.ventil_Status
        self.heat_Status
        self.bhm_Rfq_Status

class Main_Control(object):
    def __init__(self,uic):
        # uic = ui_control()
        # # super(Main_Control, self).__init__()
        # # self.timer = Timer(1,self.getInfoFromServerInJson)
        # # self.timer.start()

        try:
            self.dev = PyTango.DeviceProxy(server_name)
        except PyTango.DevFailed as exc:
            self.exceptionDialog(exc)
            return

        # установка в True, когда все элементы защиты включены (лампочки зеленые)
        self.protect_Status = False

        self.uic = uic

        # блокировка панелей включения и установки
        # self.setEnabledPanels( self.uic,False)
        self.setDisablePanels()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(timer_sec)

        self.dict = {}
        # инициализация словаря регистров для Индикаторов защиты
        self.leds = []#['X0','X1','M24','X12','X13','M25']
        self.initDictOfLeds()

        self.setSignalHandler()
        self.timer.start()

        #
        # #dict['X1'] = self.protect_Door_Led
        # # self.connectStatus_Led.setLedColor("white")
        # # print(super.protect_Door_Led)
        #
        # print dict
        # # ht = Thread(target=self.getInfoFromServerInJson)
        # # ht.start()

        # MainWindow = QtGui.QMainWindow()
        # ui = ui_control.Ui_MainWindow()
        # # ui = Main_Control()
        # ui.setupUi(MainWindow)
        # MainWindow.show()

    def initDictOfLeds(self):
        self.leds = ['X0','X1','M24','X12','X13','M1','M3','M5'] #25?

        self.dict['X0'] = self.uic.protect_Door_Led
        self.dict['X1'] = self.uic.protect_Barbell_Led
        self.dict['M24'] = self.uic.protect_External_Led
        self.dict['X12'] = self.uic.protect_Transformator_Led
        self.dict['X13'] = self.uic.protect_Lamp_Led
        # self.dict['M25'] = self.uic.protect_Vacuum_Led
        self.dict['M1'] = self.uic.heat_Status
        self.dict['M3'] = self.uic.ventil_Status
        self.dict['M5'] = self.uic.bhm_Rfq_Status


    def setSignalHandler(self):
        print("signalhand")
        QtCore.QTimer.connect(self.timer,QtCore.SIGNAL("timeout()"),self.getInfoFromServerInJson)
        self.uic.ventil_pushButton.clicked.connect(self.ventil_On)
        self.uic.heat_pushButton.clicked.connect(self.heat_On)
        self.uic.bhm_Rfq_pushButton.clicked.connect(self.bhm_Rfq_On)

    def ventil_On(self):
        inn = ["M3","1"]
        self.dev.command_inout("WriteRegisterOrFlag",inn)

    def heat_On(self):
        inn = ["M1","1"]
        self.dev.command_inout("WriteRegisterOrFlag",inn)

    def bhm_Rfq_On(self):
        inn = ["M5","1"]
        self.dev.command_inout("WriteRegisterOrFlag",inn)

    def test(self):
        print("TEST")

    def getInfoFromServerInJson(self):
        try:
            # dev = PyTango.DeviceProxy(server_name)
            parsed_json = {}
            json_from_serv = self.dev.command_inout(json_get)
            parsed_json = json.loads(json_from_serv)
            self.setLedColorStatus(parsed_json)
            if MDEBUG:
                print parsed_json['readStatus']
        except PyTango.DevFailed as exc:
            self.setDisablePanels()
            self.setLedColorStatus(parsed_json)
            if MDEBUG:
                print("exc in getInfoFromServerInJson")
        except KeyError:
            if MDEBUG:
                print("key error in parsed_json")
            print("key error in parsed_json")

    def setDisablePanels(self):
        # отключение панелей, если не все флаги состояния защиты активны
        self.uic.frame_System_Main.setEnabled(False)
        self.uic.frame_HighVoltage_Main.setEnabled(False)

    def setLedColorStatus(self, parsed):
        # установка цветового статуса на лампы состяния элементов защиты
        isConnected = False
        phk = parsed.has_key('readStatus')
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


        self.protect_Status = True

        for key in self.leds:
            if MDEBUG & phk:
                print(str(key) + " ---> " + str(parsed['argout'][0][key]))
            if isConnected:
                self.protect_Status = self.protect_Status & parsed['argout'][0][key]
                if parsed['argout'][0][key] == 1:
                    self.dict[key].setLedColor("green")
                else:
                    self.dict[key].setLedColor("red")
            else:
                self.dict[key].setLedColor("red")
                self.protect_Status = False
        if MDEBUG:
            print("Protect_status: " + str(self.protect_Status))
        self.uic.frame_System_Main.setEnabled(self.protect_Status)


            # print self.dict[key]

    def exceptionDialog(self, exc):
        lenExc = len(tuple(exc))

        mes = QtCore.QString("<b>Exceptions:</b><br><br>")
        for k in range(0,lenExc):
            mes = mes + QtCore.QString("Exception"+str(k)+"<br>")
            # mes = mes + QtCore.QString("<b>Reason</b>: " + str(exc.args[k].reason) + "<br>")
            mes = mes + QtCore.QString("<b>Description</b>: " + str(exc.args[k].desc) + "<br>")
            # mes = mes + QtCore.QString("<b>Origin</b>: " + str(exc.args[k].origin) + "<br>")
            mes = mes + QtCore.QString("<br>")

        error = QtGui.QMessageBox(QtGui.QMessageBox.Critical,"Error",mes,buttons = QtGui.QMessageBox.Ok)
        error.exec_()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = ui_control.Ui_MainWindow()
    # ui = Main_Control()
    ui.setupUi(MainWindow)
    MainWindow.show()
    mc = Main_Control(ui)
    sys.exit(app.exec_())