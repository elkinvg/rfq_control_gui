#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Mar 23 15:02:40 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(995, 616)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_4 = QtGui.QFrame(self.frame)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelMainTop = QtGui.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelMainTop.setFont(font)
        self.labelMainTop.setObjectName(_fromUtf8("labelMainTop"))
        self.verticalLayout_2.addWidget(self.labelMainTop)
        self.frame_6 = QtGui.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.checkBox_11 = QtGui.QCheckBox(self.frame_6)
        self.checkBox_11.setText(_fromUtf8(""))
        self.checkBox_11.setObjectName(_fromUtf8("checkBox_11"))
        self.gridLayout_3.addWidget(self.checkBox_11, 1, 0, 1, 1)
        self.protect_Lamp = QtGui.QCheckBox(self.frame_6)
        self.protect_Lamp.setObjectName(_fromUtf8("protect_Lamp"))
        self.gridLayout_3.addWidget(self.protect_Lamp, 1, 3, 1, 1)
        self.protect_External = QtGui.QCheckBox(self.frame_6)
        self.protect_External.setObjectName(_fromUtf8("protect_External"))
        self.gridLayout_3.addWidget(self.protect_External, 2, 1, 1, 1)
        self.checkBox_13 = QtGui.QCheckBox(self.frame_6)
        self.checkBox_13.setText(_fromUtf8(""))
        self.checkBox_13.setObjectName(_fromUtf8("checkBox_13"))
        self.gridLayout_3.addWidget(self.checkBox_13, 0, 2, 1, 1)
        self.checkBox_10 = QtGui.QCheckBox(self.frame_6)
        self.checkBox_10.setText(_fromUtf8(""))
        self.checkBox_10.setObjectName(_fromUtf8("checkBox_10"))
        self.gridLayout_3.addWidget(self.checkBox_10, 0, 0, 1, 1)
        self.protect_Door = QtGui.QCheckBox(self.frame_6)
        self.protect_Door.setEnabled(True)
        self.protect_Door.setObjectName(_fromUtf8("protect_Door"))
        self.gridLayout_3.addWidget(self.protect_Door, 0, 1, 1, 1)
        self.checkBox_12 = QtGui.QCheckBox(self.frame_6)
        self.checkBox_12.setText(_fromUtf8(""))
        self.checkBox_12.setObjectName(_fromUtf8("checkBox_12"))
        self.gridLayout_3.addWidget(self.checkBox_12, 2, 0, 1, 1)
        self.protect_Vacuum = QtGui.QCheckBox(self.frame_6)
        self.protect_Vacuum.setObjectName(_fromUtf8("protect_Vacuum"))
        self.gridLayout_3.addWidget(self.protect_Vacuum, 2, 3, 1, 1)
        self.protect_Transformator = QtGui.QCheckBox(self.frame_6)
        self.protect_Transformator.setObjectName(_fromUtf8("protect_Transformator"))
        self.gridLayout_3.addWidget(self.protect_Transformator, 0, 3, 1, 1)
        self.protect_Barbell = QtGui.QCheckBox(self.frame_6)
        self.protect_Barbell.setObjectName(_fromUtf8("protect_Barbell"))
        self.gridLayout_3.addWidget(self.protect_Barbell, 1, 1, 1, 1)
        self.checkBox_14 = QtGui.QCheckBox(self.frame_6)
        self.checkBox_14.setText(_fromUtf8(""))
        self.checkBox_14.setObjectName(_fromUtf8("checkBox_14"))
        self.gridLayout_3.addWidget(self.checkBox_14, 1, 2, 1, 1)
        self.checkBox_15 = QtGui.QCheckBox(self.frame_6)
        self.checkBox_15.setText(_fromUtf8(""))
        self.checkBox_15.setObjectName(_fromUtf8("checkBox_15"))
        self.gridLayout_3.addWidget(self.checkBox_15, 2, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_3 = QtGui.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.labelMainCenter = QtGui.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelMainCenter.setFont(font)
        self.labelMainCenter.setObjectName(_fromUtf8("labelMainCenter"))
        self.verticalLayout_3.addWidget(self.labelMainCenter)
        self.frame_5 = QtGui.QFrame(self.frame_3)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_5)
        self.gridLayout_2.setContentsMargins(-1, -1, 9, -1)
        self.gridLayout_2.setHorizontalSpacing(9)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.bhm_Rfq_pushButton = QtGui.QPushButton(self.frame_5)
        self.bhm_Rfq_pushButton.setObjectName(_fromUtf8("bhm_Rfq_pushButton"))
        self.gridLayout_2.addWidget(self.bhm_Rfq_pushButton, 1, 2, 1, 1)
        self.checkBox_9 = QtGui.QCheckBox(self.frame_5)
        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
        self.gridLayout_2.addWidget(self.checkBox_9, 1, 3, 1, 1)
        self.ventil_pushButton = QtGui.QPushButton(self.frame_5)
        self.ventil_pushButton.setObjectName(_fromUtf8("ventil_pushButton"))
        self.gridLayout_2.addWidget(self.ventil_pushButton, 0, 0, 1, 1)
        self.heat_pushButton = QtGui.QPushButton(self.frame_5)
        self.heat_pushButton.setObjectName(_fromUtf8("heat_pushButton"))
        self.gridLayout_2.addWidget(self.heat_pushButton, 1, 0, 1, 1)
        self.checkBox_7 = QtGui.QCheckBox(self.frame_5)
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.gridLayout_2.addWidget(self.checkBox_7, 0, 1, 1, 1)
        self.checkBox_8 = QtGui.QCheckBox(self.frame_5)
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.gridLayout_2.addWidget(self.checkBox_8, 1, 1, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.system_lcdNumber = QtGui.QLCDNumber(self.frame_5)
        self.system_lcdNumber.setSmallDecimalPoint(False)
        self.system_lcdNumber.setDigitCount(7)
        self.system_lcdNumber.setProperty("value", 0.0)
        self.system_lcdNumber.setObjectName(_fromUtf8("system_lcdNumber"))
        self.horizontalLayout_9.addWidget(self.system_lcdNumber)
        self.label = QtGui.QLabel(self.frame_5)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_9.addWidget(self.label)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 3, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_7 = QtGui.QFrame(self.frame)
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.gridLayout = QtGui.QGridLayout(self.frame_7)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.label_7 = QtGui.QLabel(self.frame_7)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_8.addWidget(self.label_7)
        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 2, 1, 1)
        self.cur_Volt_pushButton = QtGui.QPushButton(self.frame_7)
        self.cur_Volt_pushButton.setObjectName(_fromUtf8("cur_Volt_pushButton"))
        self.gridLayout.addWidget(self.cur_Volt_pushButton, 2, 3, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.Cur_Set_lineEdit = QtGui.QLineEdit(self.frame_7)
        self.Cur_Set_lineEdit.setMaxLength(32767)
        self.Cur_Set_lineEdit.setFrame(True)
        self.Cur_Set_lineEdit.setObjectName(_fromUtf8("Cur_Set_lineEdit"))
        self.horizontalLayout_5.addWidget(self.Cur_Set_lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame_7)
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
        self.Cur_Get_lcdNumber = QtGui.QLCDNumber(self.frame_7)
        self.Cur_Get_lcdNumber.setObjectName(_fromUtf8("Cur_Get_lcdNumber"))
        self.horizontalLayout_3.addWidget(self.Cur_Get_lcdNumber)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.Volt_Set_lineEdit = QtGui.QLineEdit(self.frame_7)
        self.Volt_Set_lineEdit.setObjectName(_fromUtf8("Volt_Set_lineEdit"))
        self.horizontalLayout_6.addWidget(self.Volt_Set_lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 2, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.Volt_Get_lcdNumber = QtGui.QLCDNumber(self.frame_7)
        self.Volt_Get_lcdNumber.setObjectName(_fromUtf8("Volt_Get_lcdNumber"))
        self.horizontalLayout_4.addWidget(self.Volt_Get_lcdNumber)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 2, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.label_6 = QtGui.QLabel(self.frame_7)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_7.addWidget(self.label_6)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 1, 1, 1)
        self.labelMainBottom = QtGui.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelMainBottom.setFont(font)
        self.labelMainBottom.setObjectName(_fromUtf8("labelMainBottom"))
        self.gridLayout.addWidget(self.labelMainBottom, 0, 0, 1, 3)
        self.verticalLayout.addWidget(self.frame_7)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.output_textBrowser = QtGui.QTextBrowser(self.frame_2)
        self.output_textBrowser.setMaximumSize(QtCore.QSize(16777215, 16777215))
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

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.labelMainTop.setText(_translate("MainWindow", "Состояние элементов защиты", None))
        self.protect_Lamp.setText(_translate("MainWindow", "Охлаждение лампы", None))
        self.protect_External.setText(_translate("MainWindow", "Внешнее управление", None))
        self.protect_Door.setText(_translate("MainWindow", "Двери модулятора закрыты", None))
        self.protect_Vacuum.setText(_translate("MainWindow", "Вакуум", None))
        self.protect_Transformator.setText(_translate("MainWindow", "Охлаждение накального трансформатора", None))
        self.protect_Barbell.setText(_translate("MainWindow", "Штанга повешена", None))
        self.labelMainCenter.setText(_translate("MainWindow", "Включение системы", None))
        self.bhm_Rfq_pushButton.setText(_translate("MainWindow", "Включение BHM RFQ", None))
        self.checkBox_9.setText(_translate("MainWindow", "CheckBox", None))
        self.ventil_pushButton.setText(_translate("MainWindow", "Включение вентилятора", None))
        self.heat_pushButton.setText(_translate("MainWindow", "Включение накала", None))
        self.checkBox_7.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_8.setText(_translate("MainWindow", "CheckBox", None))
        self.label.setText(_translate("MainWindow", "В", None))
        self.label_7.setText(_translate("MainWindow", "Напряжение В", None))
        self.cur_Volt_pushButton.setText(_translate("MainWindow", "Установить", None))
        self.label_4.setText(_translate("MainWindow", "Заданное", None))
        self.label_5.setText(_translate("MainWindow", "Измеренное", None))
        self.label_6.setText(_translate("MainWindow", "Ток мА", None))
        self.labelMainBottom.setText(_translate("MainWindow", "Высокое напряжение модулятора  (BHM) RFQ", None))
        self.clearEdit_pushButton.setText(_translate("MainWindow", "Очистить", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

