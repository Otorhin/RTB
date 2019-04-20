# -*- coding: utf-8 -*-

_print = print
log = open('log.txt', 'a')
def myprint(*args, **kwargs):
    _print(*args, **kwargs)
    try:
        log.write('\t'.join(str(v) for v in args))
        log.write('\n')
        log.flush()
    except:
        pass
print = myprint

error = open('errors.txt', 'a')

import importlib
from math import floor, ceil
import config
import telebot
from telebot import types
import db
import os
from otrh import function as otrh_f
from otrh import names
from otrh import game_config as gcfg
from otrh import equip
import threading
import pymysql
import json
import random
import traceback
import time
from math import floor, ceil
import pickle

db.init()

#список забаненных
banned = config.banned_users

#Админка
admin_command = ['admin_notify', 'clear_hand_player']
fast_command = {}
admin_ids = ['ne_you_mom']

API_TOKEN = config.tg_token
bot = telebot.TeleBot(API_TOKEN, skip_pending = True)


test_player = admin_ids + ['your_dick']

def get_message(user_id, message):
    if user_id in banned:
        return

    if user_id not in test_player:
        return

    print ('user_id : ' + str(user_id) + ' | Message : ' + message + ' | Time : ' + str(time.time()))
    print ('|--------------------|')

    if user_id in admin_ids and message.lower() in admin_command:
        set_hand(user_id, eval(message.lower()))
        return

    if user_id == '439637823' and message == 'reload1':
        enabled_plugins = [f[:-3] for f in os.listdir('modules') if f.endswith('.py')]
        print ('-----Подключение модулей-----')
        for plugin in enabled_plugins:
            try:
                exec(open("./modules/" + plugin + ".py" , encoding='utf-8').read())
                print("Подключен " + plugin)
            except Exception as e:
                print("Ошибка подключения " + plugin)
                print(e)
                exit(1)
        return

    if user_id == '439637823' and message == 'reload2':
        importlib.reload(otrh_f)
        importlib.reload(names)
        importlib.reload(equip)
        return


    if message.startswith('/start'):

        if len(message.split(' ')) > 1:
            if db.get_hero(message.split(' ')[1]) and not db.get_hero(user_id):
                db.create_hero(user_id)
                start_tutorial(user_id, ref = message.split(' ')[1])
                return

        if not db.get_hero(user_id):
            db.create_hero(user_id)
            start_tutorial(user_id)
            return



    if message.split(' ')[0] in fast_command:
        eval(fast_command[message.split(' ')[0]])(user_id, message)
        return

    if message == '/test_oldpve':
        pve_battle().start(user_id, 'knight')
        return

    if message.lower() in ['/terms', 'правила']:
        send_message(user_id, names.rules)
        return

    if message.startswith('pr_'):
        use_promocode(user_id, message)
        return
    elif message.startswith('up_'):
        use_update_code(user_id, message)
        return

    if message.startswith('/craft_'):
        game_crafting(user_id, message)
    if message.startswith('/cook_'):
        game_alchemy1(user_id, message)


    if user_id in otrh_handlers :
        otrh_handlers[user_id](user_id, message)
        return
    else :
        start_game(user_id)

def clear_hand(user_id):
    set_hand(user_id, start_game_hand)

def set_hand(user_id, hand):
    otrh_handlers[user_id] = hand


def save_error(error):
    message = str(error)
    log.write(message)
    log.write('\n\n-------------------------\n\n')
    log.flush()
    try:
        telebot.TeleBot('error_bot_token').send_message('your_mom', message)
    except:
        pass

def event_start(message):
    telebot.TeleBot(config.herald_token).send_message(config.test_chat, message)

def send_message(user_id, message, button = None, parse_mode = None):
    try:
        if button:
            buter = button
            button = types.ReplyKeyboardMarkup(resize_keyboard=True ,row_width=len(buter))
            for buter1 in buter:
                button.add(*buter1)
        bot.send_message(user_id, message , reply_markup = button, parse_mode= parse_mode)
    except Exception as e:
        print(traceback.format_exc())
        save_error(traceback.format_exc())

def send_sticker(user_id, sticker_id):
    try:
        bot.send_sticker(user_id, sticker_id)
    except:
        print(traceback.format_exc())
        save_error(traceback.format_exc())

    
enabled_plugins = [f[:-3] for f in os.listdir('modules') if f.endswith('.py')]
print ('-----Подключение модулей-----')
for plugin in enabled_plugins:
    try:
        exec(open("./modules/" + plugin + ".py" , encoding='utf-8').read())
        print("Подключен " + plugin)
    except Exception as e:
        print("Ошибка подключения " + plugin)
        print(e)
        exit(1)


with open('temp/otrh_handlers.data', 'rb') as f:
    try:
        otrh_handlers = pickle.load(f)
    except:
        otrh_handlers = {}
    
with open('temp/bd_adventure.data', 'r') as f:
    bd_adventure = f.read()
    bd_adventure = eval(bd_adventure)

with open('temp/bd_adventure2.data', 'r') as f:
    bd_adventure2 = f.read()
    bd_adventure2 = eval(bd_adventure2)

with open('temp/temp.data', 'r') as f:
    temp = f.read()
    temp = eval(temp)

with open('temp/city.data', 'r') as f:
    city = f.read()
    city = eval(city)

def save_temp():
    while True:
        f = open('temp/otrh_handlers.data', 'wb')
        pickle.dump(otrh_handlers, f)
        f.close()
        f = open('temp/temp.data', 'w', encoding='utf-8')
        f.write(str(temp))
        f.close()
        f = open('temp/city.data', 'w', encoding='utf-8')
        f.write(str(city))
        f.close()
        f = open('temp/bd_adventure.data', 'w', encoding='utf-8')
        f.write(str(bd_adventure))
        f.close()
        f = open('temp/bd_adventure2.data', 'w', encoding='utf-8')
        f.write(str(bd_adventure2))
        f.close()
        time.sleep(5)


threading.Timer(1.0, handler_adventure).start()
threading.Timer(1.0, new_handler_adventure).start()
threading.Timer(1.0, save_temp).start()

def listener3(messages):
    for m in messages:
        if m.text:
            try:
                get_message(str(m.chat.id), m.text)
            except Exception as e:
                print(traceback.format_exc())
                save_error(traceback.format_exc())


bot.set_update_listener(listener3)

i_i_i_i_i = 0

while i_i_i_i_i < 250000:
    try:
        bot.polling(none_stop=True, timeout=60)
    except Exception as e:
        save_error(traceback.format_exc())
        time.sleep(5)

