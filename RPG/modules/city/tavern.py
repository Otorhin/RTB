def city_tavern(user_id):
    _hero = db.get_hero(user_id)

    text = 'Дубовая нескладная дверь таверны отворилась перед тобой.'
    text += '\nЗайдя внутрь, ты понимаешь, что ничего не изменилось: горы мусора и битой посуды, невозмутимый хозяин, вопли пьянчуг и незнакомец в темном углу.'
    text += '\nМожешь пропустить стаканчик с каким-нибудь старым знакомым или же взяться за дело. Что выберешь?'
    button = [
        ['🤠К хозяину'],
        ['🍺В бар'],
        #['Cыграть в игры'],
        ['🚪Выйти из таверны']
    ]
    send_message(user_id, text, button)
    set_hand(user_id, city_tavern_hand)


def city_tavern_hand(user_id, message):

    if message == '🚪Выйти из таверны':
        bot_city(user_id)
    elif message == '🤠К хозяину':
        tavern_owner().on_entry(user_id)
    elif message == '🍺В бар':
        tavern_bar().on_entry(user_id)
    #elif message.lower() == 'сыграть в игры':
        #tavern_minigame().on_entry(user_id)
    else:
        pass


class tavern_owner():

    @staticmethod
    def on_entry(user_id):
        text = '`– Ну здравствуй, вечный странник. Зачем пожаловали?`'
        button = [['📜Заказное дело'], ['💬Слухи'], ['🚪Отойти от него']]
        _quest = db.get_quest(user_id)
        if int(_quest['allquest']) > 16:
            button[0].append('📦Отдать найденный груз')
        send_message(user_id, text, button, 'Markdown')
        set_hand(user_id, tavern_owner().handler)

    @staticmethod
    def handler(user_id, message):
        _hero = db.get_hero(user_id)
        _quest = db.get_quest(user_id)
        if message == '📜Заказное дело':
            tavern_owner().mission(user_id)
        elif message == '💬Слухи':
            text = 'Знаешь, сплетни - это не мое, но зеваки шепчут, что самая достоверная информация о делах в городе есть в @RogTorChat'
            send_message(user_id, text)
        elif message == '🚪Отойти от него':
            city_tavern(user_id)
        elif message == '📦Отдать найденный груз' and int(_quest['allquest']) > 16:
            tavern_owner().lost_cargo(user_id)
        else:
            pass


    @staticmethod
    def lost_cargo(user_id):
        _hero = db.get_hero(user_id)
        _store = db.get_user_inventory(user_id)
        _item_list = ['stick', 'coal', 'iron', 'stone', 'thread', 'bone', 'ruby']
        _gold = [25,300]
        if _store['lost_cargo'] != 0 :
            text = '`Я благодарен что ты решил вернуть найденный груз.\nИ оставить без награды не могу, поэтому держи часть этого груза.`\nПолучено *{}*'
            if random.random() < 0.3:
                _ntext = str(i_get_gold(user_id, wars=random.randint(*_gold))) + '💰'
                text = text.format( _ntext )
            else:
                _count = random.randint(1,5)
                _name = random.choice(_item_list)
                _ntext = names.item[_name] + ' x' + str(_count)
                db.add_inventory(user_id, _name, _count)
                text = text.format ( _ntext )
            db.add_inventory(user_id, 'lost_cargo', -1)
        else:
            text = '`У тебя же нет никакого груза.\nПриходи как найдешь потерянный груз.`'
        send_message(user_id, text, parse_mode = 'Markdown')


    @staticmethod
    def mission(user_id):
        _hero = db.get_hero(user_id)
        # 11 - стартовых квестов
        _quest = db.get_quest(user_id)
        if _quest['monster']:
            if _quest['monster'] in ['forest', 'mount', 'desert', 'tavern', 'guild'] and _quest['killed'] < _quest['need']:
                text = 'Тебя не видели в локации `{}`'.format( names.adventure_name[_quest['monster']] )
            elif _quest['killed'] < _quest['need']:
                _tttt = monsters[_quest['monster']]['name']
                text = '`У тебя только ' + str(_quest['killed']) + ' из ' + str(_quest['need']) + ' голов монстра известного под именем ' + _tttt + '`'
            else:
                text = '`Чтож. Ты быстро расправился с этим заданием. Держи свою награду.`'
                text += '\n{}💰{}💎{}💡'.format(i_get_gold(user_id, exp = 3), i_get_diamond(user_id, exp = 2), i_get_exp(user_id))
                db.change_quest(user_id, None, None, None, None, None, allquest =  int(_quest['allquest']) + 1)
        elif _quest['item']:
            _store = db.get_user_inventory(user_id)
            if _quest['item'] in ['gun', 'potion']:
                _colvo = db.get_count_inv(user_id, _quest['item'], _quest['inv'])
                if _colvo < _quest['need']:
                    _test = eval('equip.{}'.format(_quest['item']))[_quest['inv']][0]
                    text = '-Ты что, не понимаешь, что такое *{}*? Я же ясно сказал, мне нужно *{}* шт. Ни больше ни меньше! А у тебя всего *{}*!'.format( _test, _quest['need'], _colvo )
                else:
                    text = '`Чтож. Ты быстро расправился с этим заданием. Держи свою награду.`'
                    text += '\n{}💰{}💎{}💡'.format(i_get_gold(user_id, exp = 3), i_get_diamond(user_id, exp = 2), i_get_exp(user_id))
                    db.del_inventory_item(user_id, _quest['item'], _quest['inv'])
                    db.change_quest(user_id, None, None, None, None, None, allquest = int(_quest['allquest']) + 1)
            elif _store[_quest['item']] < _quest['need']:
                text = '-Ты что, не понимаешь, что такое *{}*? Я же ясно сказал, мне нужно *{}* шт. Ни больше ни меньше! А у тебя всего *{}*!'.format( names.item[_quest['item']], _quest['need'], _store[_quest['item']] )
                #text = '`Ты ещё собрал недостаточно {}. У тебя {} из {} необходимых мне.`'.format( names.item[_quest['item']], _store[_quest['item']], _quest['need'] )
            else:
                text = '`Чтож. Ты быстро расправился с этим заданием. Держи свою награду.`'
                text += '\n{}💰{}💎{}💡'.format(i_get_gold(user_id, exp = 3), i_get_diamond(user_id, exp = 2), i_get_exp(user_id))
                db.add_inventory(user_id, _quest['item'], -_quest['need'])
                db.change_quest(user_id, None, None, None, None, None, allquest = int(_quest['allquest']) + 1)
        elif 'start_{}'.format(_quest['allquest']) in names.quests:
            _id_quest = 'start_{}'.format(_quest['allquest'])
            _new_quest = names.quests[_id_quest]
            text = '{text}'.format(**_new_quest)
            if _new_quest['type'] == 'item':
                db.change_quest(user_id, _id_quest, item = _new_quest['item'], need = _new_quest['need'], allquest = int(_quest['allquest']), lastquest = _id_quest)
                _name = names.item[_new_quest['item']]
                _count = _new_quest['need']
                text += '\n\n*Задание: {} x{}*'.format(_name, _count)
            elif _new_quest['type'] in ['gun', 'potion']:
                db.change_quest(user_id, _id_quest, item = _new_quest['type'], need = _new_quest['need'], allquest = int(_quest['allquest']), lastquest = _id_quest, inv = _new_quest['item'])
                _name = eval('equip.{}'.format(_new_quest['type']))[_new_quest['item']][0]
                _count = _new_quest['need']
                text += '\n\n*Задание: {} x{}*'.format(_name, _count)
            elif _new_quest['type'] == 'adventure':
                db.change_quest(user_id, _id_quest, monster = _new_quest['adventure'], killed = 0, need = 1, allquest = int(_quest['allquest']), lastquest = _id_quest)
                _name = names.adventure_name[_new_quest['adventure']]
                text += '\n\n*Задание: посетить локацию {}*'.format(_name)
            else:
                db.change_quest(user_id, _id_quest, monster = _new_quest['monster'], killed = 0, need = _new_quest['need'], allquest = int(_quest['allquest']), lastquest = _id_quest)
                _name = monsters[_new_quest['monster']]['name']
                _count = _new_quest['need']
                text += '\n\n*Задание: Головы монстра {} x{}*'.format(_name, _count)
        else:
            text = '`Ты уж извини, но пока задания закончились, заходи позже.`'
        send_message(user_id, text, None, 'Markdown')


class tavern_bar():

    @staticmethod
    def on_entry(user_id):
        text = '`Опять в разочаровании от неубитого монстра?`'
        text += '\n`Ну присаживайся. Налью тебе бодрящего напитка.`'
        text += '\n\nАссортимента бара:'
        text += '\n🍺*Эль* - 100 золота.'
        text += '\n🥃*Настойка* - 85 золота.'
        text += '\n🍯*Медовуха* - 50 золота.'
        text += '\n🍼*Молоко* - 90 золота.'
        button = [['🍺Эль', '🥃Настойка'], ['🍯Медовуха', '🍼Молоко'],['Отойти от бара']]
        send_message(user_id, text, button, 'Markdown')
        set_hand(user_id, tavern_bar().handler)

    @staticmethod
    def handler(user_id, message):
        _hero = db.get_hero(user_id)
        if 'bar' in get_all_buff(user_id) and message.lower() != 'отойти от бара':
            send_message(user_id, 'Ты уже пьян. Я не налью такому человеку, как ты, не капли алкоголя.')
            return
        if message == '🥃Настойка' and _hero['gold'] > 84:
            db.add_gold(user_id, -85)
            i_hero_add_buff(user_id, 'bar')
            db.add_def(user_id, -10)
            bd_adventure.append(['i_hero_del_buff', 31, [user_id, 'bar']])
            bd_adventure.append(['db.add_def', 31, [user_id, 10]])
            send_message(user_id, random.choice(names.bar_text['tincture']))
        elif message == '🍺Эль' and _hero['gold'] > 99:
            db.add_gold(user_id, -100)
            i_hero_add_buff(user_id, 'bar')
            db.add_atk(user_id, -15)
            bd_adventure.append(['i_hero_del_buff', 31, [user_id, 'bar']])
            bd_adventure.append(['db.add_atk', 31, [user_id, 15]])
            send_message(user_id, random.choice(names.bar_text['el']))
        elif message == '🍯Медовуха' and _hero['gold'] > 49:
            db.add_gold(user_id, -50)
            send_message(user_id, random.choice(names.bar_text['mead']))
        elif 'milk' in get_all_buff(user_id) and message == '🍼Молоко':
            send_message(user_id, 'Не лопнешь, сосунок?')
            return
        elif message == '🍼Молоко' and _hero['gold'] > 89:
            db.add_gold(user_id, -90)
            i_hero_add_buff(user_id, 'milk')
            db.add_atk(user_id, 5)
            db.add_def(user_id, 5)
            bd_adventure.append(['i_hero_del_buff', 31, [user_id, 'milk']])
            bd_adventure.append(['db.add_atk', 31, [user_id, -5]])
            bd_adventure.append(['db.add_def', 31, [user_id, -5]])
            send_message(user_id, random.choice(names.bar_text['milk']))
            return
        elif message.lower() == 'отойти от бара':
            city_tavern(user_id)
            return
        elif _hero['gold'] < 50:
            send_message(user_id, 'У тебя недостаточно денег на что-либо из моего бара')
            return
        else:
            return
        _quest = db.get_quest(user_id)
        if _quest['monster'] and _quest['monster'] == 'tavern':
                db.change_quest(user_id,quest = _quest['quest'], monster = _quest['monster'], killed = int(_quest['killed']) + 1, need = _quest['need'], allquest = _quest['allquest'])
        if str(_quest['allquest']) == '12':
            text = '`-Ты ж… Ик… Понимаешь… Жизнь – тяжелая штка, вт… Мне с моей Элочкой и пришлос с насиженного места срываться-то… Обычно-то… Армия прошлась мимо, нкго не трогая, и потом вернулась, прошла мимо – и как не бывало… А в этот раз – по деревням прошлись, последних кормильцев забрали… Нашего Кирюшу… Да и сгинули они там все… Кроме моего Кирюши! Точно тебе говорю, он еще где-то там, воюет за нас… Живой! А про северную границу… Забудь. Нет её больше.`'
            send_message(user_id, text, parse_mode='Markdown')
        if str(_quest['allquest']) == '17':
            text = 'Пока вы отдыхали, наслаждаясь напитком, к вам кто-то подсел…'
            send_message(user_id, text, parse_mode='Markdown')


class tavern_minigame():

    @staticmethod
    def on_entry(user_id):
        pass

    @staticmethod
    def game_bones(user_id):
        pass
