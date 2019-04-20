import config
import pymysql
from otrh import function as otrh_f
import os
import time

def init():
    pass

enabled_plugins = [f[:-3] for f in os.listdir('dbmodules') if f.endswith('.py')]
print ('-----Подключение модулей-----')
for plugin in enabled_plugins:
    try:
        exec(open("./dbmodules/" + plugin + ".py" , encoding='utf-8').read())
        print("Подключен " + plugin)
    except Exception as e:
        print("Ошибка подключения " + plugin)
        print(e)
        exit(1)