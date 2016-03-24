import os
MDEBUG = True
os.environ['TANGO_HOST'] = '172.16.21.5:10000'
server_name = "test/rfq/read"
json_get = "ReadAllRegistersAndFlagsFromCacheInJson"
timer_sec = 1