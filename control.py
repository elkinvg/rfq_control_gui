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

class Main_Control(ui_control.Ui_MainWindow):
    def __init__(self):
        # super(Main_Control, self).__init__()
        # self.timer = Timer(1,self.getInfoFromServerInJson)
        # self.timer.start()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(timer_sec)

        self.setSignalHandler()
        self.timer.start()
        # ht = Thread(target=self.getInfoFromServerInJson)
        # ht.start()


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
        if (parsed['readStatus'] == 1):
            self.connectStatus_Led.setLedColor("green")
        else:
            self.connectStatus_Led.setLedColor("red")

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    # ui = ui_control.Ui_MainWindow()
    ui = Main_Control()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

