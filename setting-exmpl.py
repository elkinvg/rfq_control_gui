# -*- coding: utf-8 -*-
import os
### Вывод информации в консоль
MDEBUG = True
# MDEBUG = False
### Вывод значений регистров и флагов полученных с MODBUS в textEdit
# MODBUSOUT = True
MODBUSOUT = False
os.environ['TANGO_HOST'] = '172.16.21.5:10000'
server_name = "test/mb/con"
json_get = "ReadAllRegistersAndFlagsFromCacheInJson"
timer_sec = 3
