# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Mar 23 15:02:40 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from taurus.qt.qtgui.display import TaurusLed

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtCore.QObject):
    # class Ui_MainWindow(object):
    clsSign = QtCore.pyqtSignal()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        # MainWindow.setFixedSize(1020, 616)
        # MainWindow.setFixedSize(1120, 616)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        # self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        # self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.horizontalLayout_st = QtGui.QHBoxLayout()
        self.horizontalLayout_st.setObjectName(_fromUtf8("horizontalLayout_st"))

        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.addStatusLed()

        #init frame_Protect_Main
        self.addAndInitFrameProtectMain()

        #init frame_System_Main (self.frame_3)
        self.addAndInitFrameSystem_Main()

        #init frame_HighVoltage_Main (self.frame_7)
        self.addAndInitFrameHighVoltage_Main()

        #??? !!! TST
        self.addAndInitFrameHighVoltage_Main_Buncher()
        #self.addAndInitFrameBuncher_Main()

        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.output_textBrowser = QtGui.QTextBrowser(self.frame_2)
        # self.output_textBrowser.setFixedWidth(263)
        font = QtGui.QFont()
        font.setPointSize(7)
        # self.label_4.setFont(font)
        self.output_textBrowser.setFont(font)
        self.hoLay = QtGui.QHBoxLayout()
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hoLay.addItem(spacerItem7)
        # self.connectStatus_Led = TaurusLed(self.frame_2)
        # self.connectStatus_Led.setLedColor("red")
        # self.connectStatus_Led.setFixedSize(35,35)
        # self.hoLay.addWidget(self.connectStatus_Led)
        self.verticalLayout_4.addLayout(self.hoLay)
        self.output_textBrowser.setObjectName(_fromUtf8("output_textBrowser"))
        self.verticalLayout_4.addWidget(self.output_textBrowser)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.clearEdit_pushButton = QtGui.QPushButton(self.frame_2)
        self.clearEdit_pushButton.setObjectName(_fromUtf8("clearEdit_pushButton"))
        self.horizontalLayout_2.addWidget(self.clearEdit_pushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 995, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # здесь проходит серия сигналов ... один сигнал порождает другой
        # на данный момет было самое быстрое решение
        MainWindow.trigger.connect(self.tst2)

    def addStatusLed(self):
        self.connectStatus_Led = TaurusLed(self.frame_2)
        self.connectStatus_Led.setLedColor("red")
        self.connectStatus_Led.setFixedSize(20,20)
        self.horizontalLayout_st.addWidget(self.connectStatus_Led)
        self.labelTango = QtGui.QLabel()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTango.setFont(font)
        self.labelTango.setObjectName(_fromUtf8("labelTango"))
        self.horizontalLayout_st.addWidget(self.labelTango)

        self.outtextRadioButton = QtGui.QRadioButton()
        self.outtextRadioButton.setText(_fromUtf8("Показать вывод"))
        self.horizontalLayout_st.addWidget(self.outtextRadioButton)

        self.verticalLayout.addLayout(self.horizontalLayout_st)

    def tst2(self):
        self.clsSign.emit()


    def addAndInitFrameProtectMain(self):
        self.frame_Protect_Main = QtGui.QFrame(self.frame)
        self.frame_Protect_Main.setFrameShape(QtGui.QFrame.Panel)
        self.frame_Protect_Main.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_Protect_Main.setObjectName(_fromUtf8("frame_Protect_Main"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_Protect_Main)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelMainTop = QtGui.QLabel(self.frame_Protect_Main)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelMainTop.setFont(font)
        self.labelMainTop.setObjectName(_fromUtf8("labelMainTop"))
        self.verticalLayout_2.addWidget(self.labelMainTop)


        self.frame_Protect = QtGui.QFrame(self.frame_Protect_Main)
        self.frame_Protect.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_Protect.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_Protect.setObjectName(_fromUtf8("frame_Protect"))

        self.gridLayout_3 = QtGui.QGridLayout(self.frame_Protect)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))

        # LED and label protect_Door
        self.protect_Door_Led = TaurusLed(self.frame_Protect)
        self.gridLayout_3.addWidget(self.protect_Door_Led, 0, 0, 1, 1)
        self.protect_Door = QtGui.QLabel(self.frame_Protect)
        self.protect_Door.setObjectName(_fromUtf8("protect_Door"))
        self.gridLayout_3.addWidget(self.protect_Door, 0, 1, 1, 1)
        self.setStatusColor(self.protect_Door_Led,self.protect_Door,"red")

        # LED and label protect_Barbell
        self.protect_Barbell_Led = TaurusLed(self.frame_Protect)
        self.gridLayout_3.addWidget(self.protect_Barbell_Led, 1, 0, 1, 1)
        self.protect_Barbell = QtGui.QLabel(self.frame_Protect)
        self.protect_Barbell.setObjectName(_fromUtf8("protect_Barbell"))
        self.gridLayout_3.addWidget(self.protect_Barbell, 1, 1, 1, 1)
        self.setStatusColor(self.protect_Barbell_Led,self.protect_Barbell,"red")

        # LED and label protect_External
        self.protect_External_Led  = TaurusLed(self.frame_Protect)
        self.gridLayout_3.addWidget(self.protect_External_Led, 2, 0, 1, 1)
        self.protect_External = QtGui.QLabel(self.frame_Protect)
        self.protect_External.setObjectName(_fromUtf8("protect_External"))
        self.gridLayout_3.addWidget(self.protect_External, 2, 1, 1, 1)
        self.setStatusColor(self.protect_External_Led,self.protect_External,"red")

        # LED and label protect_Transformator
        self.protect_Transformator_Led  = TaurusLed(self.frame_Protect)
        self.gridLayout_3.addWidget(self.protect_Transformator_Led, 0, 2, 1, 1)
        self.protect_Transformator = QtGui.QLabel(self.frame_Protect)
        self.protect_Transformator.setObjectName(_fromUtf8("protect_Transformator"))
        self.gridLayout_3.addWidget(self.protect_Transformator, 0, 3, 1, 1)
        self.setStatusColor(self.protect_Transformator_Led,self.protect_Transformator,"red")

        # LED and label protect_Lamp
        self.protect_Lamp_Led  = TaurusLed(self.frame_Protect)
        self.gridLayout_3.addWidget(self.protect_Lamp_Led, 1, 2, 1, 1)
        self.protect_Lamp = QtGui.QLabel(self.frame_Protect)
        self.protect_Lamp.setObjectName(_fromUtf8("protect_Lamp"))
        self.gridLayout_3.addWidget(self.protect_Lamp, 1, 3, 1, 1)
        self.setStatusColor(self.protect_Lamp_Led,self.protect_Lamp,"red")

        # LED and label protect_Vacuum
        self.protect_Vacuum_Led  = TaurusLed(self.frame_Protect)
        self.gridLayout_3.addWidget(self.protect_Vacuum_Led, 2, 2, 1, 1)
        self.protect_Vacuum = QtGui.QLabel(self.frame_Protect)
        self.protect_Vacuum.setObjectName(_fromUtf8("protect_Vacuum"))
        self.gridLayout_3.addWidget(self.protect_Vacuum, 2, 3, 1, 1)
        # self.setStatusColor(self.protect_Vacuum_Led,self.protect_Vacuum,"white")
        self.setStatusColor(self.protect_Vacuum_Led,self.protect_Vacuum,"red")

        self.gridLayout_3.setColumnStretch(1, 2)
        self.gridLayout_3.setColumnStretch(3, 2)

        self.verticalLayout_2.addWidget(self.frame_Protect)
        self.verticalLayout.addWidget(self.frame_Protect_Main)

    def addAndInitFrameSystem_Main(self):
        self.frame_System_Main = QtGui.QFrame(self.frame)
        # self.frame_System_Main.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_System_Main.setFrameShape(QtGui.QFrame.Panel)
        self.frame_System_Main.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_System_Main.setObjectName(_fromUtf8("frame_System_Main"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_System_Main)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.labelMainCenter = QtGui.QLabel(self.frame_System_Main)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelMainCenter.setFont(font)
        self.labelMainCenter.setObjectName(_fromUtf8("labelMainCenter"))
        self.verticalLayout_3.addWidget(self.labelMainCenter)
        #frame_System frame_ 5
        self.frame_System = QtGui.QFrame(self.frame_System_Main)
        # self.frame_System.setFrameShape(QtGui.QFrame.StyledPanel)
        # self.frame_System.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_System.setObjectName(_fromUtf8("frame_System"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_System)
        # self.gridLayout_2.setContentsMargins(-1, -1, 9, -1)
        # self.gridLayout_2.setHorizontalSpacing(9)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.bhm_Rfq_pushButton = QtGui.QPushButton(self.frame_System)
        self.bhm_Rfq_pushButton.setObjectName(_fromUtf8("bhm_Rfq_pushButton"))
        self.gridLayout_2.addWidget(self.bhm_Rfq_pushButton, 1, 2, 1, 1)

        # self.bhm_Rfq_Status = QtGui.QCheckBox(self.frame_System)
        self.bhm_Rfq_Status = TaurusLed(self.frame_System)
        self.bhm_Rfq_Status.setLedColor("red")
        self.bhm_Rfq_Status.setObjectName(_fromUtf8("bhm_Rfq_Status"))
        self.gridLayout_2.addWidget(self.bhm_Rfq_Status, 1, 3, 1, 1)

        self.ventil_pushButton = QtGui.QPushButton(self.frame_System)
        self.ventil_pushButton.setObjectName(_fromUtf8("ventil_pushButton"))
        # self.ventil_pushButton.setFixedWidth(200)
        self.gridLayout_2.addWidget(self.ventil_pushButton, 0, 0, 1, 1)
        self.heat_pushButton = QtGui.QPushButton(self.frame_System)
        self.heat_pushButton.setObjectName(_fromUtf8("heat_pushButton"))
        # self.heat_pushButton.setFixedWidth(200)
        self.gridLayout_2.addWidget(self.heat_pushButton, 1, 0, 1, 1)

        #self.ventil_Status = QtGui.QCheckBox(self.frame_System)
        self.ventil_Status = TaurusLed(self.frame_System)
        self.ventil_Status.setLedColor("red")
        self.ventil_Status.setObjectName(_fromUtf8("ventil_Status"))
        self.gridLayout_2.addWidget(self.ventil_Status, 0, 1, 1, 1)

        # self.heat_Status = QtGui.QCheckBox(self.frame_System)
        self.heat_Status = TaurusLed(self.frame_System)
        self.heat_Status.setLedColor("red")
        self.heat_Status.setObjectName(_fromUtf8("heat_Status"))
        self.gridLayout_2.addWidget(self.heat_Status, 1, 1, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))

        self.system_lcdNumber = QtGui.QLCDNumber(self.frame_System)
        self.system_lcdNumber.setSmallDecimalPoint(False)
        self.system_lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.system_lcdNumber.setDigitCount(7)
        self.system_lcdNumber.setFixedHeight(50)
        self.system_lcdNumber.setFixedWidth(150)
        self.system_lcdNumber.setProperty("value", 0.0)
        self.system_lcdNumber.setObjectName(_fromUtf8("system_lcdNumber"))
        self.horizontalLayout_9.addWidget(self.system_lcdNumber)
        self.label = QtGui.QLabel(self.frame_System)
        self.label.setObjectName(_fromUtf8("label"))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label.setFont(font)
        self.horizontalLayout_9.addWidget(self.label)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 3, 0, 1, 1)
        # spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        # self.horizontalLayout_9.addItem(spacerItem)

        self.verticalLayout_3.addWidget(self.frame_System)
        self.verticalLayout.addWidget(self.frame_System_Main)

    def addAndInitFrameHighVoltage_Main(self):
        self.frame_HighVoltage_Main = QtGui.QFrame(self.frame)
        self.frame_HighVoltage_Main.setFrameShape(QtGui.QFrame.Panel)
        self.frame_HighVoltage_Main.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_HighVoltage_Main.setObjectName(_fromUtf8("frame_HighVoltage_Main"))
        self.gridLayout = QtGui.QGridLayout(self.frame_HighVoltage_Main)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.label_7 = QtGui.QLabel(self.frame_HighVoltage_Main)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_8.addWidget(self.label_7)
        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 2, 1, 1)

        self.cur_Volt_pushButton = QtGui.QPushButton(self.frame_HighVoltage_Main)
        self.cur_Volt_pushButton.setFixedWidth(150)
        self.cur_Volt_pushButton.setObjectName(_fromUtf8("cur_Volt_pushButton"))
        self.gridLayout.addWidget(self.cur_Volt_pushButton, 2, 3, 1, 1)

        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)

        # self.cur_Set_lineEdit = QtGui.QLineEdit(self.frame_HighVoltage_Main)
        self.cur_Set_lineEdit = QtGui.QSpinBox(self.frame_HighVoltage_Main)
        self.setLineEditStile(self.cur_Set_lineEdit)
        self.cur_Set_lineEdit.setObjectName(_fromUtf8("cur_Set_lineEdit"))
        self.horizontalLayout_5.addWidget(self.cur_Set_lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 1, 1, 1)

        self.label_4 = QtGui.QLabel(self.frame_HighVoltage_Main)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame_HighVoltage_Main)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)

        self.cur_Get_lcdNumber = QtGui.QLCDNumber(self.frame_HighVoltage_Main)
        self.cur_Get_lcdNumber.setObjectName(_fromUtf8("cur_Get_lcdNumber"))
        self.horizontalLayout_3.addWidget(self.cur_Get_lcdNumber)
        self.cur_Get_lcdNumber.setDigitCount(6)
        self.cur_Get_lcdNumber.setFixedHeight(40)
        self.cur_Get_lcdNumber.setFixedWidth(120)
        self.setLcdPalette(self.cur_Get_lcdNumber)

        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        # self.Volt_Set_lineEdit = QtGui.QLineEdit(self.frame_HighVoltage_Main)
        self.Volt_Set_lineEdit = QtGui.QSpinBox(self.frame_HighVoltage_Main)
        self.Volt_Set_lineEdit.setObjectName(_fromUtf8("Volt_Set_lineEdit"))
        self.setLineEditStile(self.Volt_Set_lineEdit)
        self.horizontalLayout_6.addWidget(self.Volt_Set_lineEdit)

        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 2, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)

        self.Volt_Get_lcdNumber = QtGui.QLCDNumber(self.frame_HighVoltage_Main)
        self.Volt_Get_lcdNumber.setObjectName(_fromUtf8("Volt_Get_lcdNumber"))
        self.horizontalLayout_4.addWidget(self.Volt_Get_lcdNumber)
        self.Volt_Get_lcdNumber.setFixedHeight(40)
        self.Volt_Get_lcdNumber.setFixedWidth(120)
        self.setLcdPalette(self.Volt_Get_lcdNumber)

        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 2, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.label_6 = QtGui.QLabel(self.frame_HighVoltage_Main)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_7.addWidget(self.label_6)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 1, 1, 1)
        self.labelMainBottom = QtGui.QLabel(self.frame_HighVoltage_Main)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelMainBottom.setFont(font)
        self.labelMainBottom.setObjectName(_fromUtf8("labelMainBottom"))
        self.gridLayout.addWidget(self.labelMainBottom, 0, 0, 1, 3)
        self.verticalLayout.addWidget(self.frame_HighVoltage_Main)
        self.horizontalLayout.addWidget(self.frame)

    # ??? !!!
    def addAndInitFrameHighVoltage_Main_Buncher(self):
        self.frame_HighVoltage_Main_Buncher = QtGui.QFrame(self.frame)
        self.frame_HighVoltage_Main_Buncher.setFrameShape(QtGui.QFrame.Panel)
        self.frame_HighVoltage_Main_Buncher.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_HighVoltage_Main_Buncher.setObjectName(_fromUtf8("frame_HighVoltage_Main_Buncher"))
        self.gridLayout_Buncher = QtGui.QGridLayout(self.frame_HighVoltage_Main_Buncher)
        self.gridLayout_Buncher.setObjectName(_fromUtf8("gridLayout_Buncher"))
        self.horizontalLayout_8_Buncher = QtGui.QHBoxLayout()
        self.horizontalLayout_8_Buncher.setObjectName(_fromUtf8("horizontalLayout_8_Buncher"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8_Buncher.addItem(spacerItem1)
        self.label_7_Buncher = QtGui.QLabel(self.frame_HighVoltage_Main_Buncher)
        self.label_7_Buncher.setObjectName(_fromUtf8("label_7_Buncher"))
        self.horizontalLayout_8_Buncher.addWidget(self.label_7_Buncher)
        self.gridLayout_Buncher.addLayout(self.horizontalLayout_8_Buncher, 1, 2, 1, 1)

        self.cur_Volt_pushButton_Buncher = QtGui.QPushButton(self.frame_HighVoltage_Main_Buncher)
        self.cur_Volt_pushButton_Buncher.setFixedWidth(150)
        self.cur_Volt_pushButton_Buncher.setObjectName(_fromUtf8("cur_Volt_pushButton_Buncher"))
        self.gridLayout_Buncher.addWidget(self.cur_Volt_pushButton_Buncher, 2, 3, 1, 1)

        self.horizontalLayout_5_Buncher = QtGui.QHBoxLayout()
        self.horizontalLayout_5_Buncher.setObjectName(_fromUtf8("horizontalLayout_5_Buncher"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5_Buncher.addItem(spacerItem2)

        # self.cur_Set_lineEdit = QtGui.QLineEdit(self.frame_HighVoltage_Main)
        self.cur_Set_lineEdit_Buncher = QtGui.QSpinBox(self.frame_HighVoltage_Main_Buncher)
        self.setLineEditStile(self.cur_Set_lineEdit_Buncher)
        self.cur_Set_lineEdit_Buncher.setObjectName(_fromUtf8("cur_Set_lineEdit_Buncher"))
        self.horizontalLayout_5_Buncher.addWidget(self.cur_Set_lineEdit_Buncher)
        self.gridLayout_Buncher.addLayout(self.horizontalLayout_5_Buncher, 2, 1, 1, 1)

        self.label_4_Buncher = QtGui.QLabel(self.frame_HighVoltage_Main_Buncher)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4_Buncher.setFont(font)
        self.label_4_Buncher.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_Buncher.addWidget(self.label_4_Buncher, 2, 0, 1, 1)
        self.label_5_Buncher = QtGui.QLabel(self.frame_HighVoltage_Main_Buncher)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5_Buncher.setFont(font)
        self.label_5_Buncher.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_Buncher.addWidget(self.label_5_Buncher, 3, 0, 1, 1)
        self.horizontalLayout_3_Buncher = QtGui.QHBoxLayout()
        self.horizontalLayout_3_Buncher.setObjectName(_fromUtf8("horizontalLayout_3_Buncher"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3_Buncher.addItem(spacerItem3)

        self.cur_Get_lcdNumber_Buncher = QtGui.QLCDNumber(self.frame_HighVoltage_Main_Buncher)
        self.cur_Get_lcdNumber_Buncher.setObjectName(_fromUtf8("cur_Get_lcdNumber"))
        self.horizontalLayout_3_Buncher.addWidget(self.cur_Get_lcdNumber_Buncher)
        self.cur_Get_lcdNumber_Buncher.setDigitCount(6)
        self.cur_Get_lcdNumber_Buncher.setFixedHeight(40)
        self.cur_Get_lcdNumber_Buncher.setFixedWidth(120)
        self.setLcdPalette(self.cur_Get_lcdNumber_Buncher)

        self.gridLayout_Buncher.addLayout(self.horizontalLayout_3_Buncher, 3, 1, 1, 1)
        self.horizontalLayout_6_Buncher = QtGui.QHBoxLayout()
        self.horizontalLayout_6_Buncher.setObjectName(_fromUtf8("horizontalLayout_6_Buncher"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6_Buncher.addItem(spacerItem4)
        # self.Volt_Set_lineEdit = QtGui.QLineEdit(self.frame_HighVoltage_Main)
        self.Volt_Set_lineEdit_Buncher = QtGui.QSpinBox(self.frame_HighVoltage_Main_Buncher)
        self.Volt_Set_lineEdit_Buncher.setObjectName(_fromUtf8("Volt_Set_lineEdit_Buncher"))
        self.setLineEditStile(self.Volt_Set_lineEdit_Buncher)
        self.horizontalLayout_6_Buncher.addWidget(self.Volt_Set_lineEdit_Buncher)

        self.gridLayout_Buncher.addLayout(self.horizontalLayout_6_Buncher, 2, 2, 1, 1)
        self.horizontalLayout_4_Buncher = QtGui.QHBoxLayout()
        self.horizontalLayout_4_Buncher.setObjectName(_fromUtf8("horizontalLayout_4_Buncher"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4_Buncher.addItem(spacerItem5)

        self.Volt_Get_lcdNumber_Buncher = QtGui.QLCDNumber(self.frame_HighVoltage_Main_Buncher)
        self.Volt_Get_lcdNumber_Buncher.setObjectName(_fromUtf8("Volt_Get_lcdNumber_Buncher"))
        self.horizontalLayout_4_Buncher.addWidget(self.Volt_Get_lcdNumber_Buncher)
        self.Volt_Get_lcdNumber_Buncher.setFixedHeight(40)
        self.Volt_Get_lcdNumber_Buncher.setFixedWidth(120)
        self.setLcdPalette(self.Volt_Get_lcdNumber_Buncher)

        self.gridLayout_Buncher.addLayout(self.horizontalLayout_4_Buncher, 3, 2, 1, 1)
        self.horizontalLayout_7_Buncher = QtGui.QHBoxLayout()
        self.horizontalLayout_7_Buncher.setObjectName(_fromUtf8("horizontalLayout_7_Buncher"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7_Buncher.addItem(spacerItem6)
        self.label_6_Buncher = QtGui.QLabel(self.frame_HighVoltage_Main_Buncher)
        self.label_6_Buncher.setObjectName(_fromUtf8("label_6_Buncher"))
        self.horizontalLayout_7_Buncher.addWidget(self.label_6_Buncher)
        self.gridLayout_Buncher.addLayout(self.horizontalLayout_7_Buncher, 1, 1, 1, 1)
        self.labelMainBottom_Buncher = QtGui.QLabel(self.frame_HighVoltage_Main_Buncher)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelMainBottom_Buncher.setFont(font)
        self.labelMainBottom_Buncher.setObjectName(_fromUtf8("labelMainBottom_Buncher"))
        self.gridLayout_Buncher.addWidget(self.labelMainBottom_Buncher, 0, 0, 1, 3)
        self.verticalLayout.addWidget(self.frame_HighVoltage_Main_Buncher)
        self.horizontalLayout.addWidget(self.frame)

    def setStatusColor(self,led,label,color):
        palette = QtGui.QPalette()
        if color=="red":
            palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)
        elif color=="green":
            palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.green)
        else:
            palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)
        label.setPalette(palette)
        led.setLedColor(color)

        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        label.setFont(font)

    def setLcdPalette(self,LCD):
        palette = LCD.palette()
        palette.setColor(palette.WindowText, QtCore.Qt.darkBlue)
        # background color
        palette.setColor(palette.Background, QtGui.QColor(0, 170, 255))
        # "light" border
        #palette.setColor(palette.Light, QtGui.QColor(255, 0, 0))
        # "dark" border
        palette.setColor(palette.Dark, QtCore.Qt.darkBlue)
        LCD.setPalette(palette)

    def setLineEditStile(self,set_lineEdit):
        set_lineEdit.setFixedHeight(30)
        set_lineEdit.setFixedWidth(120)
        # set_lineEdit.setMaxLength(6)
        set_lineEdit.setAlignment(QtCore.Qt.AlignRight)
        font = QtGui.QFont()
        font.setPointSize(12)
        set_lineEdit.setFont(font)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Управление модулятором", None))
        self.labelMainTop.setText(_translate("MainWindow", "Состояние элементов защиты", None))
        self.labelTango.setText(_translate("MainWindow", "Подключение к серверу Tango", None))
        self.protect_Lamp.setText(_translate("MainWindow", "Охлаждение лампы", None))
        self.protect_External.setText(_translate("MainWindow", "Внешнее управление", None))
        self.protect_Door.setText(_translate("MainWindow", "Двери модулятора закрыты", None))
        self.protect_Vacuum.setText(_translate("MainWindow", "Вакуум", None))
        self.protect_Transformator.setText(_translate("MainWindow", "Охлаждение накального трансформатора", None))
        self.protect_Barbell.setText(_translate("MainWindow", "Штанга повешена", None))
        self.labelMainCenter.setText(_translate("MainWindow", "В(ы)ключение системы", None))
        self.bhm_Rfq_pushButton.setText(_translate("MainWindow", "В(ы)ключение BHM RFQ", None))
        # self.bhm_Rfq_Status.setText(_translate("MainWindow", "CheckBox", None))
        self.ventil_pushButton.setText(_translate("MainWindow", "В(ы)ключение вентилятора", None))
        self.heat_pushButton.setText(_translate("MainWindow", "В(ы)ключение накала", None))
        # self.ventil_Status.setText(_translate("MainWindow", "CheckBox", None))
        # self.heat_Status.setText(_translate("MainWindow", "CheckBox", None))
        self.label.setText(_translate("MainWindow", "В", None))
        self.label_7.setText(_translate("MainWindow", "Напряжение В", None))
        self.cur_Volt_pushButton.setText(_translate("MainWindow", "Установить", None))
        self.label_4.setText(_translate("MainWindow", "Заданное", None))
        self.label_5.setText(_translate("MainWindow", "Измеренное", None))
        self.label_6.setText(_translate("MainWindow", "Ток мА", None))
        self.labelMainBottom.setText(_translate("MainWindow", "Высокое напряжение модулятора  (BHM) RFQ", None))
        self.clearEdit_pushButton.setText(_translate("MainWindow", "Очистить", None))

        #new ??? !!!
        self.cur_Volt_pushButton_Buncher.setText(_translate("MainWindow", "Установить", None))
        self.labelMainBottom_Buncher.setText(_translate("MainWindow", "Высокое напряжение Банчера RFQ", None))
        self.label_7_Buncher.setText(_translate("MainWindow", "Напряжение В", None))
        self.label_6_Buncher.setText(_translate("MainWindow", "Ток мА", None))
        self.label_4_Buncher.setText(_translate("MainWindow", "Заданное", None))
        self.label_5_Buncher.setText(_translate("MainWindow", "Измеренное", None))

        # def addAndInitFrameBuncher_Main(self):
        #     self.frame_Buncher_Main = QtGui.QFrame(self.frame)
        #     self.frame_Buncher_Main.setFrameShape(QtGui.QFrame.Panel)
        #     self.frame_Buncher_Main.setFrameShadow(QtGui.QFrame.Raised)
        #     self.frame_Buncher_Main.setObjectName(_fromUtf8("frame_Buncher_Main"))
        #
        #     self.Volt_Get_lcdNumber_Buncher = QtGui.QLCDNumber(self.frame_Buncher_Main)
        #     self.Volt_Get_lcdNumber_Buncher.setObjectName(_fromUtf8("Volt_Get_lcdNumber_Buncher"))
        #
        #     self.horiz_layout_Buncher = QtGui.QHBoxLayout(self.frame_Buncher_Main)
        #
        #     # self.horizontalLayout_4.addWidget(self.Volt_Get_lcdNumber)
        #     self.Volt_Get_lcdNumber_Buncher.setFixedHeight(40)
        #     self.Volt_Get_lcdNumber_Buncher.setFixedWidth(120)
        #     self.setLcdPalette(self.Volt_Get_lcdNumber_Buncher)
        #     self.horiz_layout_Buncher.addWidget(self.Volt_Get_lcdNumber_Buncher)
        #
        #     self.cur_Set_lineEdit_Buncher = QtGui.QSpinBox(self.frame_Buncher_Main)
        #     self.setLineEditStile(self.cur_Set_lineEdit_Buncher)
        #     self.cur_Set_lineEdit_Buncher.setObjectName(_fromUtf8("cur_Set_lineEdit_Buncher"))
        #     self.horiz_layout_Buncher.addWidget(self.cur_Set_lineEdit_Buncher)
        #
        #     self.volt_Set_lineEdit_Buncher = QtGui.QSpinBox(self.frame_Buncher_Main)
        #     self.setLineEditStile(self.volt_Set_lineEdit_Buncher)
        #     self.volt_Set_lineEdit_Buncher.setObjectName(_fromUtf8("volt_Set_lineEdit_Buncher"))
        #     self.horiz_layout_Buncher.addWidget(self.volt_Set_lineEdit_Buncher)
        #
        #     self.cur_Volt_pushButton_Buncher = QtGui.QPushButton(self.frame_Buncher_Main)
        #     self.cur_Volt_pushButton_Buncher.setFixedWidth(150)
        #     self.cur_Volt_pushButton_Buncher.setObjectName(_fromUtf8("cur_Volt_pushButton_Buncher"))
        #     self.horiz_layout_Buncher.addWidget(self.cur_Volt_pushButton_Buncher)
        #
        #     self.verticalLayout.addWidget(self.frame_Buncher_Main)
        #     self.horizontalLayout.addWidget(self.frame)