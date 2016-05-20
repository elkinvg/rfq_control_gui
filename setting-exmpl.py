# -*- coding: utf-8 -*-
import os
### Вывод информации в консоль
MDEBUG = True
# MDEBUG = False
### Вывод значений регистров и флагов полученных с MODBUS в textEdit
# MODBUSOUT = True
MODBUSOUT = False
### Текстовый вывод в редактор
TEXTEDIT = False
# путь к танго-серверу модулятора
server_name = "tango://localhost:10000/test/mb/con"
# имя метода получения значений всех регистров и флагов в JSON
json_get = "ReadAllRegistersAndFlagsFromCacheInJson"
# установка времени таймера запроса по модбасу
timer_sec = 3
# установка размера текста в выводе
fontSize = 7
