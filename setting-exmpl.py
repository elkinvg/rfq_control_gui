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
#TEXTEDIT = True
timer_sec = 3
# установка размера текста в выводе
fontSize = 10

# одноразовые настройки
# зазмеры окна с окном мывода и без
sizeWindowWithEdit = [1120, 650]
sizeWindowWithoutEdit = [800, 650]
# путь к танго-серверу модулятора
server_name = "tango://172.16.21.5:10000/test/rfq/read"
# имя метода получения значений всех регистров и флагов в JSON
json_get = "ReadAllRegistersAndFlagsFromCacheInJson"
# установка времени таймера запроса по модбасу