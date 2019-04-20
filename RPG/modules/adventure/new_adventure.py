exec(open("./modules/adventure/room/mobs.py" , encoding='utf-8').read())
exec(open("./modules/adventure/room/manager.py" , encoding='utf-8').read())


def get_adv_item(adv, user_id):
    _item_lists = names.list_item[adv]
    _store = db.get_user_inventory(user_id)
    _hero = db.get_hero(user_id)
    _quest = db.get_quest(user_id)

    if 'change' in temp[user_id]:
        temp[user_id]['change'] += 0.01
    else:
        temp[user_id]['change'] = 0.01
        if _hero['guild_id']:
            _guild = db.get_guild(_hero['guild_id'])
            temp[user_id]['change'] += int(_guild['build3']) * 0.01

    _item_list = _item_lists[0]

    if random.random() < (0.6 + temp[user_id]['change'] ):
        _item_list = _item_list + _item_lists[1]
    if random.random() < (0.4 + temp[user_id]['change'] ):
        _item_list = _item_list + _item_lists[2]
        if adv == 'forest':
            if int(_quest['allquest']) > 15:
                _item_list.append('lost_cargo')
    if random.random() < (0.2 + temp[user_id]['change'] ):
        _item_list = _item_list + _item_lists[3]
        if adv == 'mount':
            if int(_quest['allquest']) > 13 and int(_quest['allquest']) < 15:
                _item_list.append('snowflower')

    random.shuffle(_item_list)
    random.shuffle(_item_list)
    random_item = random.choice(_item_list)

    return (random_item)



class adventure():

    @staticmethod
    def header(user_id):
        _hero = db.get_hero(user_id)
        text = '{gold}💰 | {diamond}💎 | {rating}🏆\n'.format(**_hero)
        return (text)

    @staticmethod
    def choice(user_id):
        _hero = db.get_hero(user_id)
        _quest = db.get_quest(user_id)
        text = 'Выбери куда пойдешь на этот раз?'
        text += '\n\n🌲Лес - спокойный и тихий поход за ресурсами.'
        button = [['🌲Лeс'], ['⬅️Назад']]
        if int(_quest['allquest']) > 10:
            text += '\n\n🗻Горы - слегка рискованный поход за более ценными ресурсами. Иногда можно наткнутся на озлобленного монстра.'
            button[0].append('🗻Горы')
        if int(_quest['allquest']) > 24:
            button[0].append('🏜Пустыня')
        send_message(user_id, text, button)
        set_hand(user_id, adventure.choice_handler)


    @staticmethod
    def choice_handler(user_id, message):
        _hero = db.get_hero(user_id)
        _quest = db.get_quest(user_id)
        if message == '⬅️Назад':
            start_game(user_id)
        elif message == '🌲Лес' or message == '🌲Лeс' :
            adventure.enter(user_id, 'forest')
            if _quest['monster'] and _quest['monster'] == 'forest':
                db.change_quest(user_id,quest = _quest['quest'], monster = _quest['monster'], killed = int(_quest['killed']) + 1, need = _quest['need'], allquest = _quest['allquest'])
        elif message == '🗻Горы' and int(_quest['allquest']) > 10:
            adventure.enter(user_id, 'mount')
            if _quest['monster'] and _quest['monster'] == 'mount':
                db.change_quest(user_id,quest = _quest['quest'], monster = _quest['monster'], killed = int(_quest['killed']) + 1, need = _quest['need'], allquest = _quest['allquest'])
        elif message == '🏜Пустыня' and int(_quest['allquest']) > 24:
            adventure.enter(user_id, 'desert')
            if _quest['monster'] and _quest['monster'] == 'desert':
                db.change_quest(user_id,quest = _quest['quest'], monster = _quest['monster'], killed = int(_quest['killed']) + 1, need = _quest['need'], allquest = _quest['allquest'])
        else:
            pass

    @staticmethod
    def enter(user_id, adventures):
        adventure.item_timer(user_id)
        text = names.adv_text[adventures]
        button = [['Ожидать'], ['Вернуться домой']]
        send_message(user_id, text, button)
        temp[user_id] = {}
        _skill = db.get_skill(user_id)
        _hero = db.get_hero(user_id)
        temp[user_id]['count_item'] = round(int(_skill['bag']) * 2,5)
        temp[user_id]['bag'] = []
        temp[user_id]['gold'] = 0
        temp[user_id]['expect'] = 0
        temp[user_id]['adv'] = adventures
        temp[user_id]['dungeon'] = False
        if adventures == 'mount':
            temp[user_id]['change_mob'] = 0.3
        elif adventures == 'forest':
            temp[user_id]['change_mob'] = 0.25
        else:
            temp[user_id]['change_mob'] = 1
        _equip = db.get_equip(user_id)
        if _equip['amulet']:
            if _equip['amulet'][0] == 'collector':
                temp[user_id]['change_mob'] -= 0.05
            if _equip['amulet'][0] == 'hunter':
                temp[user_id]['change_mob'] += 0.05

    @staticmethod
    def item_timer(user_id):
        set_hand(user_id, adventure.adventure_handler)
        time = random.randint(20, 30)
        bd_adventure2.append(['adventure.random_item', time, [user_id]])

    @staticmethod
    def random_item(user_id):
        if temp[user_id]['dungeon']:
            return
        _skill = db.get_skill(user_id)
        if temp[user_id]['count_item'] == 0 or len(temp[user_id]['bag']) == int(_skill['bag']):
            print ('user_id : ' + str(user_id) + ' | Action: Return home | Time : ' + str(time.time()))
            if len(temp[user_id]['bag']) == 0:
                text = 'Ты вернулся домой с пустыми руками.\nНичего, в следующий раз будет лучше.'
            else:
                text = 'Ты принес домой следующие предметы:\n'
                _data = {}
                for _item in temp[user_id]['bag']:
                    if _item in _data:
                        _data[_item] += 1
                    else:
                        _data[_item] = 1
                for _item in _data:
                    text += '{} x{}\n'.format(names.item[_item], _data[_item])
                if temp[user_id]['gold'] != 0:
                    text += '\n{}💰'.format(temp[user_id]['gold'])
            send_message(user_id, text, get_start_button(user_id))
            temp[user_id] = {}
            return

        temp[user_id]['count_item'] -= 1
        text = random.choice(names.advent_text[temp[user_id]['adv']])
        send_message(user_id, text)
        print ('user_id : ' + str(user_id) + ' | Action: Get /catch | Time : ' + str(time.time()))
        print ('|--------------------|')
        set_hand(user_id, adventure.item_handler)
        bd_adventure2.append(['adventure.item_timer', 20, [user_id]])



    @staticmethod
    def item_handler(user_id, message):
        _hero = db.get_hero(user_id)
        if message.lower() == 'вернуться домой':
            text = 'Ты выдвинулся домой.'
            temp[user_id]['count_item'] = 0
            send_message(user_id, text)
            return
        elif message.lower() == '/catch':
            set_hand(user_id, adventure.adventure_handler)
            _quest = db.get_quest(user_id)

            if temp[user_id]['adv'] in ['forest', 'mount'] and (random.random() < 0.05):
                random_item = get_adv_item(temp[user_id]['adv'], user_id)
                if _quest['item'] != random_item:
                    text = 'Ты нашел **{}**, но он рассыпался прямо у тебя в руках.\nСмахнув слезу, ты решил продолжить приключение.'.format(names.item[random_item])
                    send_message(user_id, text, parse_mode = 'Markdown')
                    return

            if temp[user_id]['adv'] == 'mount' and _quest['quest'] == 'start_23' and random.random() < 0.1 and int(_store['logic']) < 1:
                _quest = db.get_quest(user_id)
                text = 'Внезапно вы решили поискать логику, но ничего не вышло. Возвращайтесь в Таверну.'
                db.add_inventory(user_id, 'logic', 1)
                send_message(user_id, text)
                return

            if temp[user_id]['adv'] == 'desert' and random.random() < 0.25:
                print ('user_id : ' + str(user_id) + ' | Action: Get Dungeon | Time : ' + str(time.time()))
                print ('|--------------------|')
                temp[user_id]['dungeon'] = True
                unknown_dungeon().on_entry(user_id)
                set_hand(user_id, unknown_dungeon().handler)
                return

            if (random.random() < temp[user_id]['change_mob'] and get_atk(user_id) > 20) or temp[user_id]['adv'] == 'desert':
                _mob_list = [*gcfg.mobs[temp[user_id]['adv']]['easy']]
                if _hero['rating'] > 150:
                    _mob_list += [*gcfg.mobs[temp[user_id]['adv']]['medium']]
                if _hero['rating'] > 250:
                    _mob_list += [*gcfg.mobs[temp[user_id]['adv']]['hard']]
                monster_battle(user_id, random.choice(_mob_list))
                return

            random_item = get_adv_item(temp[user_id]['adv'], user_id)
            text = random.choice(names.advent_text['item']).format(names.item[random_item])
            if random.random() < 0.075:
                text = random.choice(names.advent_text['diamond_item']).format(names.item[random_item])
                send_sticker(user_id, 'CAADAgADXwADP1c0Gk1PS2oDPWnTAg')
                i_get_diamond(user_id, 1)
            if random.random() > 0.8:
                _gold = i_get_gold(user_id)
                text += '\nТакже ты нашел под ногами {}💰.'.format(_gold)
                temp[user_id]['gold'] += _gold
            send_message(user_id, text, parse_mode = 'Markdown')
            temp[user_id]['bag'].append(random_item)
            db.add_inventory(user_id, random_item, 1)
        elif message.lower() == 'вернуться домой':
            temp[user_id]['count_item'] = 0
            text = 'Ты выдвинулся домой.'
            send_message(user_id, text, parse_mode = 'Markdown')
        else:
            return

    @staticmethod
    def adventure_handler(user_id, message):
        if message == '/catch':
            text = random.choice(names.advent_text['not_item'])
        elif message.lower() == 'ожидать':
            if temp[user_id]['expect'] == 10:
                send_sticker(user_id, 'CAADAgADXQADP1c0GhOSdTV19-FaAg')
                add_new_ach(user_id, 'expect')
                text = 'Кажется ожидание убило тебя, но может оно и к лучшему'
                temp[user_id]['count_item'] = 0
            else:
                text = 'Ну ты ожидаешь, но пока успехов это тебе не дало.'
            temp[user_id]['expect'] += 1
        elif message.lower() == 'вернуться домой':
            text = 'Ты выдвинулся домой.'
            temp[user_id]['count_item'] = 0
        else:
            return
        send_message(user_id, text)