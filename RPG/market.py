# -*- coding: utf-8 -*-
import config
import telebot
import db
import threading
import traceback
import time
from otrh import function as otrh_f
from otrh import names
from otrh import equip

db.init()
temp_data = {}

API_TOKEN = config.market_token
bot = telebot.TeleBot(API_TOKEN, skip_pending = True)
game_bot = telebot.TeleBot(config.tg_token)

@bot.message_handler(content_types=['audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location', 'contact', 'new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo', 'delete_chat_photo', 'group_chat_created', 'supergroup_chat_created', 'channel_chat_created', 'migrate_to_chat_id', 'migrate_from_chat_id', 'pinned_message'])
def zalupa(m):
    return


@bot.message_handler(func=lambda message: str(message.from_user.id) in config.banned_users)
def zalup(m):
    return


@bot.message_handler(func=lambda message: message.text.startswith('/add_'))
def add_item_trade(m):
    _user_id = str(m.from_user.id)
    if _user_id not in temp_data:
        temp_data[_user_id] = {}
    _data = m.text.split('_')
    _store = db.get_user_inventory(str(m.from_user.id))
    if len(_data) == 3:
        try:
            int(_data[2])
        except:
            return
        if _data[1] not in names.item or _data[1] in ['user_id', 'logic', 'lost_cargo', 'blacksmithtools']:
            text = 'Неправильная команда'
        elif int(_store[_data[1]]) < int(_data[2]) or int(_data[2]) < 1 or int(_data[2]) != round(int(_data[2])):
            text = 'У тебя нет столько ресурсов'
        else:
            text = 'Ресурсы добавлены в обмен'
            temp_data[_user_id][_data[1]] = int(_data[2])
        bot.reply_to(m, text)
    else:
        bot.reply_to(m, 'Неправильная команда.')


@bot.message_handler(commands=['done'])
def done_trade(m):
    _user_id = str(m.from_user.id)
    if _user_id not in temp_data or temp_data[_user_id] == {}:
        bot.reply_to(m, 'У тебя нет ресурсов для обмена')
        return
    _data = m.text.split(' ')
    if len(_data) == 2:
        try:
            int(_data[1])  
            if not db.get_hero(_data[1]) or _data[1] == _user_id:
                bot.reply_to(m, 'Неправильная команда')
                return
            _hero = db.get_hero(m.from_user.id)
            _hero2 = db.get_hero(int(_data[1]))
            if _hero2['guild_id'] != _hero['guild_id']:
                bot.reply_to(m, 'Человек не в твоей гильдии, куда ты отдаешь ресурсы?')
                return
            _store = db.get_user_inventory(str(m.from_user.id))
            text = 'Ты отдал свои ресурсы {}'.format(db.get_hero(_data[1])['nick'])
            text2 = '⚜️Ты получил ресурсы от {}'.format(db.get_hero(_user_id)['nick'])
            for _item in temp_data[_user_id]:
                if int(_store[_item]) < int(temp_data[_user_id][_item]):
                    bot.reply_to(m, 'У тебя нет ресурсов для обмена')
                    return
                text += '\n{} х{}'.format(names.item[_item], temp_data[_user_id][_item])
                text2 += '\n{} х{}'.format(names.item[_item], temp_data[_user_id][_item])
            for _item in temp_data[_user_id]:
                db.add_inventory(_user_id, _item, -int(temp_data[_user_id][_item]))
                db.add_inventory(_data[1], _item, temp_data[_user_id][_item])
            bot.reply_to(m, text)
            text2 += '\n\nБудет ли ответ?'
            game_bot.send_message(_data[1], text2)
            temp_data[_user_id] = {}
        except Exception as e:
            print(e)
            bot.reply_to(m, 'Неправильная команда')
    else:
        bot.reply_to(m, 'Неправильная команда')

@bot.message_handler(commands=['check'])
def check_trade(m):
    _user_id = str(m.from_user.id)
    text = 'Твое предложение обмена:\n'
    if _user_id not in temp_data:
        bot.reply_to(m, 'Тут все пусто.')
        return
    for _item in temp_data[_user_id]:
        text += '\n{} х{}'.format(names.item[_item], temp_data[_user_id][_item])
    bot.reply_to(m, text)

@bot.message_handler(commands=['clear'])
def check_trade(m):
    _user_id = str(m.from_user.id)
    temp_data[_user_id] = {}
    text = 'Твое предложение обмена очищено.'
    bot.reply_to(m, text)

@bot.message_handler(commands=['help'])
def check_trade(m):
    text = '/check - Проверить что ты хочешь отправить другому игроку'
    text += '\n/clear - очистить список отправки'
    text += '\n/add_{}_{} - добавить в список предмет и его количество'
    text += '\n/done {} - отправить предметы игроку. Вставить его Telegram ID'
    bot.reply_to(m, text)

@bot.message_handler(commands=['start'])
def start_game(m):
    _store = db.get_user_inventory(str(m.from_user.id))
    text = '📦Твой склад с материалами:'
    for _item in _store:
        if _store[_item] != 0 and _item not in ['user_id' ,'logic', 'lost_cargo']:
            enable_hero_store = True
            text += '\n{} х{}\n/add_{}_1'.format(names.item[_item], _store[_item], _item)
    if not enable_hero_store:
        text = 'У вас нету ресурсов.'
    bot.reply_to(m, text)


class other():

    @staticmethod
    def listener3(messages):
        for m in messages:
            if m.text:
                try:
                    print('User: {} ({})'.format(m.from_user.first_name, m.from_user.id))
                    print('Message: ' + m.text)
                    print('|--------------------|')
                except:
                    pass

if True:
    bot.set_update_listener(other().listener3)

i_i_i_i_i = 0

while i_i_i_i_i < 250000:
    try:
        bot.polling(none_stop = True, timeout=20)
    except Exception as e:
        time.sleep(25)
