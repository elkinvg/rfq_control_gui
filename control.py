#!/usr/bin/env python
# -*- coding: utf-8 -*-

# class LedIndicator(QtGui.QWidget):
#     def __init__(self, status):
from PyQt4 import QtCore, QtGui
import PyTango
import ui_control
import setting
import json
from threading import Thread

server_name = setting.server_name
json_get = setting.json_get

class Main_Control(ui_control.Ui_MainWindow):
    def __init__(self):
        # self.getInfoFromServerInJson()
        ht = Thread(target=self.getInfoFromServerInJson)
        ht.start()
        print("start")

    def getInfoFromServerInJson(self):
        try:
            dev = PyTango.DeviceProxy(server_name)
            json_from_serv = dev.command_inout(json_get)
            print json_from_serv
        except PyTango.DevFailed as exc:
            print(exc)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    # ui = ui_control.Ui_MainWindow()
    ui = Main_Control()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

