def handler_adventure():
    while True :
        try :
            i = 0
            for querys in bd_adventure:
                bd_adventure[i][1] -= 1
                if bd_adventure[i][1] == 0:
                    eval(querys[0])(*querys[2])
                    bd_adventure.remove(querys)
                i += 1
        except:
            save_error(str(traceback.format_exc()))
        time.sleep(60)


def new_handler_adventure():
    while True :
        try :
            i = 0
            for querys in bd_adventure2:
                bd_adventure2[i][1] -= 1
                if bd_adventure2[i][1] == 0:
                    eval(querys[0])(*querys[2])
                    bd_adventure2.remove(querys)
                i += 1
        except:
            save_error(str(traceback.format_exc()))
        time.sleep(1.5)



def counter_item(user_id, category, item):
    _inventory = db.get_inventory(user_id)
    i = 0
    for all in _inventory:
        if all[0] == category and all[1] == item:
            i += 1
    return(i)

fast_command['/bag'] = 'bot_fast_bag'
def bot_fast_bag(user_id, message):
    if user_id not in temp or 'bag' not in temp[user_id]:
        send_message(user_id, 'На твоих плечах отсутствует сумка.')
        return
    text = 'В твоей сумке:\n\n'
    _data = {}
    for _item in temp[user_id]['bag']:
        if _item in _data:
            _data[_item] += 1
        else:
            _data[_item] = 1
    for _item in _data:
        text += '{} x{}\n'.format(names.item[_item], _data[_item])
    send_message(user_id, text)

fast_command['/hero'] = 'bot_fast_hero'
def bot_fast_hero(user_id, message):
    text = get_hero(user_id)
    text += i_hero_buff(user_id)
    text += '\n\n🎒Инвентарь {}'.format(len(db.get_inventory(user_id)))
    text += '\n\n' + i_hero_equip(user_id)
    send_message(user_id, text)


fast_command['/stock'] = 'bot_fast_stock'
def bot_fast_stock(user_id, message):
    _store = db.get_user_inventory(user_id)
    enable_hero_store = False
    text = 'Ваши ресурсы:'
    for _item in _store:
        if _store[_item] != 0 and _item != 'user_id':
            enable_hero_store = True
            text += '\n{}: {} штук'.format(names.item[_item], _store[_item])
    if not enable_hero_store:
        text = 'У вас нету ресурсов.'
    send_message(user_id, text)


fast_command['/quest'] = 'bot_fast_quest'
def bot_fast_quest(user_id, message):
    _quest = db.get_quest(user_id)
    _store = db.get_user_inventory(user_id)
    _inventory = db.get_inventory(user_id)
    if _quest['monster']:
        if _quest['monster'] in ['forest', 'mount', 'desert']:
            text = 'Необходимо посетить локацию `{}`'.format( names.adventure_name[_quest['monster']] )
        else:
            _tttt = monsters[_quest['monster']]['name']
            text = '`У тебя ' + str(_quest['killed']) + ' из ' + str(_quest['need']) + ' голов монстра известного под именем ' + _tttt + '`'
    elif _quest['item']:
        if _quest['item'] in ['gun', 'potion']:
            _colvo = db.get_count_inv(user_id, _quest['item'], _quest['inv'])
            if _colvo < _quest['need']:
                _test = eval('equip.{}'.format(_quest['item']))[_quest['inv']][0]
                text = '`Ты собрал {} из {} {}`'.format(_colvo, _quest['need'], _test)
        else:
            text = '`Ты собрал {} из {} {}`'.format(_store[_quest['item']], _quest['need'], names.item[_quest['item']])
    elif _quest['inv']:
        pass
    else:
        text = 'У тебя нет активного задания'
    send_message(user_id, text, parse_mode = 'Markdown')


fast_command['/donate'] = 'bot_donate'
def bot_donate(user_id, message):
    text = 'Поддержи разработчиков бота:'
    text += '\nПолучи уникальную донат-валюту 🍕Пицца '
    text += '1🍕 = 10 rub'
    text += '\nДля доната писать @ot0rhin'
    text += '\n\nУникальные функции за 🍕'
    text += '\nПеренос вашего аккаунта на другой номер Telegram 15🍕'
    text += '\nВайп вашего персонажа 15🍕'
    text += '\nEmoji в ник 10🍕'
    text += '\nПисать @ot0rhin'
    send_message(user_id, text)


fast_command['/menu'] = 'bot_refresh'
def bot_refresh(user_id, message):
    if user_id in temp:
        if 'bag' in temp[user_id]:
            text = 'К сожалению, эта команда сейчас бессильна'
            send_message(user_id, text)
            return
    start_game(user_id)


fast_command['/ref'] = 'bot_refka'
def bot_refka(user_id, message):
    text = '\nСсылка для приглашения вашего друга : t.me/rogtorbot?start=' + str(user_id)

    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT * FROM `user` WHERE `referal` = %s"
        cursor.execute(sql, (user_id))
        result = cursor.fetchall()

    text += '\n\nТы пригласил {} игроков.'.format( len(result) )


    send_message(user_id, text)




fast_command['/tops'] = 'bot_tops'
def bot_tops(user_id, message):
    text = 'Игровые топы:\n'
    text += '\n💡По опыту /top_e'
    text += '\n💰По золоту /top_g'
    text += '\n🏆По рейтингу /top_r'
    send_message(user_id, text)


fast_command['/top_e'] = 'bot_top_e'
def bot_top_e(user_id, message):
    db1 = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    text = '💡Рейтинг опытных игроков.\n'
    i = 1

    with db1.cursor() as cursor:
        sql = "SELECT `user_id`,`exp` FROM `user` ORDER BY `user`.`exp` DESC LIMIT 10"
        cursor.execute(sql)
        result = cursor.fetchall()
    for alluser in result:
        text += '\n# {} {} - {}💡'.format(i, db.get_hero(alluser['user_id'])['nick'], alluser['exp'])
        i += 1
    db1.close()

    send_message(user_id, text)


fast_command['/top_g'] = 'bot_top_g'
def bot_top_g(user_id, message):
    db1 = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    text = '💰Рейтинг богатых игроков.\n'
    i = 1

    with db1.cursor() as cursor:
        sql = "SELECT `user_id`,`gold` FROM `user` ORDER BY `user`.`gold` DESC LIMIT 10"
        cursor.execute(sql)
        result = cursor.fetchall()
    for alluser in result:
        text += '\n# {} {} - {}💰'.format(i, db.get_hero(alluser['user_id'])['nick'], alluser['gold'])
        i += 1
    db1.close()

    send_message(user_id, text)


fast_command['/top_r'] = 'bot_top_r'
def bot_top_r(user_id, message):
    #send_message(user_id, '🏆Рейтинг временно отключен.\n\nПрошлый Топ-1\n[MAS]Reincor - 452🏆')
    #return
    db1 = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    text = '🏆Рейтинг бесстрашных игроков\n'
    i = 1

    with db1.cursor() as cursor:
        sql = "SELECT `user_id`,`rating` FROM `user` ORDER BY `user`.`rating` DESC LIMIT 10"
        cursor.execute(sql)
        result = cursor.fetchall()
    for alluser in result:
        text += '\n# {} {} - {}🏆'.format(i, db.get_hero(alluser['user_id'])['nick'], alluser['rating'])
        i += 1
    db1.close()

    send_message(user_id, text)


fast_command['/help'] = 'bot_helper'
def bot_helper(user_id, message):
    text = '❓Полезные ссылки:'
    text += '\n• Чат игры @RogTorChat'
    text += '\n• бот для передачи ресурсов между игроками: @rtb_market_bot (пропишите в него /help):'
    text += '\n• багрепорты и идеи писать сюда: @unknown_inbot;'
    text += '\n• библиотека: @RogTorLibrary;'
    text += '\n• новости: @RogTorNews;'
    text += '\n• канал с сhangelog или дичью разраба: @beta_rtb.'
    send_message(user_id, text)


fast_command['/bot_sfdsfdsfdsf'] = 'bot_sfdsfdsfdsf'
def bot_sfdsfdsfdsf(user_id, message):
    db.add_inventory_item(user_id, 'amulet', 'collector')
    db.add_inventory_item(user_id, 'amulet', 'insight')
    db.add_inventory_item(user_id, 'amulet', 'otorhin')
    db.add_inventory_item(user_id, 'amulet', 'hunter')

    db.add_inventory_item(user_id, 'shand', 'knife')
    db.add_inventory_item(user_id, 'shand', 'shield')
    send_message(user_id, 'Набор выдан')