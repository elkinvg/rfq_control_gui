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

# class Main_Control(ui_control.Ui_MainWindow):
class Main_Control(object):
    def __init__(self,uic):
        # uic = ui_control()
        # # super(Main_Control, self).__init__()
        # # self.timer = Timer(1,self.getInfoFromServerInJson)
        # # self.timer.start()
        self.uic = uic
        self.timer = QtCore.QTimer()
        self.timer.setInterval(timer_sec)

        self.dict = {}
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
        self.leds = ['X0','X1','M24','X12','X13'] #25?

        self.dict['X0'] = self.uic.protect_Door_Led
        self.dict['X1'] = self.uic.protect_Barbell_Led
        self.dict['M24'] = self.uic.protect_External_Led
        self.dict['X12'] = self.uic.protect_Transformator_Led
        self.dict['X13'] = self.uic.protect_Lamp_Led
        # self.dict['M25'] = self.uic.protect_Vacuum_Led

    def setSignalHandler(self):
        print("signalhand")
        QtCore.QTimer.connect(self.timer,QtCore.SIGNAL("timeout()"),self.getInfoFromServerInJson)


    def getInfoFromServerInJson(self):
        try:
            dev = PyTango.DeviceProxy(server_name)
            json_from_serv = dev.command_inout(json_get)
            parsed_json = json.loads(json_from_serv)
            self.setLedColorStatus(parsed_json)
            if MDEBUG:
                print parsed_json['readStatus']
        except PyTango.DevFailed as exc:
            print(exc)
        except KeyError:
            print("key error in parsed_json")

    def setLedColorStatus(self, parsed):
        isConnected = False
        if (parsed['readStatus'] == 1):
            self.uic.connectStatus_Led.setLedColor("green")
            isConnected = True
        else:
            self.uic.connectStatus_Led.setLedColor("red")
            isConnected = False

        for key in self.leds:
            print(str(key) + " ---> " + str(parsed['argout'][0][key]))
            if isConnected:
                if parsed['argout'][0][key] == 1:
                    self.dict[key].setLedColor("green")
                else:
                    self.dict[key].setLedColor("red")
            else:
                self.dict[key].setLedColor("red")
            # print self.dict[key]


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

