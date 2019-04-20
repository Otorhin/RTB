class oldbattle():

    @staticmethod
    def get_def_atk(_atk, _def):
        return (ceil(_atk * 19 / (_def + 19) + 0.05))

    @staticmethod
    def get_user_atk(user_id):
        _equip = db.get_equip(user_id)
        _weapon = _equip['gun'][0].split('-')
        _weapon_lvl = oldbattle().get_lvl_weapon('123')

        atk = get_atk(user_id)
        atk *= (5 + _weapon_lvl) *  0.2

        if False:
            _change2 = _weapon_lvl * 0.05
            _change3 = _change2 * 0.5
            if random.random() < _change2:
                atk = get_atk(user_id) * 2
                temp[user_id]['text'] = '🎯Критический удар'
            if random.random() < _change3:
                temp[user_id]['text'] = '🎯Критический удар (в тройном размере)'
                atk = get_atk(user_id) * 3
        elif False:
            _change = _weapon_lvl * 0.05
            _change2 = _weapon_lvl * 0.02
            if random.random() < _change:
                temp[user_id]['blood'] = True
            if random.random() < _change2:
                atk = get_atk(user_id) * 30
                temp[user_id]['text'] = '🎯Ты стал зол и нанес нереальный урон.'
        else:
            pass


        atk = round(random.uniform((atk * 0.7), (atk * 1.3)))
        return (atk)

    @staticmethod
    def get_lvl_weapon(exp):
        return (0)

    @staticmethod
    def add_weapon_exp(user_id):
        pass


class pve_battle():

    @staticmethod
    def header(user_id):
        _hero = db.get_hero(user_id)
        text = ''

        if user_id in temp:
            if 'hp' in temp[user_id]:
                text += str(temp[user_id]['hp']) + '❤️'
                text += ' ' + str(temp[user_id]['stamina']) + '⚡️'
                text += '\n' + temp[user_id]['monster']['name'] + ': ' + str(temp[user_id]['monster']['hp']) + '❤️'

        text += '\n\n'
        return (text)

    @staticmethod
    def battle_handler(user_id, message):
        _equip = db.get_equip(user_id)
        _hero = db.get_hero(user_id)

        if message.lower() == 'ударить оружием' and _equip['gun']:
            temp[user_id]['last'] = 'weapon'
            if temp[user_id]['stamina'] < 50:
                text = 'У тебя не хватает сил для удара оружием.'
                send_message(user_id, text)
                return

            if random.random() > 0.9:
                text = 'Монстр увернулся от твоего удара.'
                temp[user_id]['stamina'] -= 50
                pve_battle().battle(user_id, text)
                return

            _atk = oldbattle().get_user_atk(user_id)
            oldbattle().add_weapon_exp(user_id)
            temp[user_id]['stamina'] -= 50
            temp[user_id]['monster']['hp'] = temp[user_id]['monster']['hp'] - _atk
            text = 'Ты ударил ' + temp[user_id]['monster']['name'] + ' на ' + str(_atk) + '💥 урона'
            if 'text' in temp[user_id]:
                text = temp[user_id]['text'] + '\n' + text

            pve_battle().battle(user_id, text)

        elif message.lower() == 'пнуть противника':
            if temp[user_id]['stamina'] < 25:
                temp[user_id]['stamina'] -= 25
                text = 'У тебя не хватает сил для пинка врагу.'
                send_message(user_id, text)
                return

            temp[user_id]['last'] = 'atk'
            _atk = _hero['atk']
            _atk = round(random.uniform((_atk * 0.9), (_atk * 1.2)))
            temp[user_id]['stamina'] -= 25
            temp[user_id]['monster']['hp'] = temp[user_id]['monster']['hp'] - _atk
            text = 'Ты ударил ' + temp[user_id]['monster']['name'] + ' на ' + str(_atk) + '💥 урона'
            pve_battle().battle(user_id, text)

        elif message.lower() == 'блокировать удар':
            if temp[user_id]['last'] == 'full_block':
                send_message(user_id, 'Ты только что блокировал удар. Твое тело не выдержит второго удара.')
                return

            temp[user_id]['last'] = 'full_block'
            text = 'Собравшись с духом, ты успешно отбил эту атаку.'
            pve_battle().battle(user_id, _text=text, _lock = 'full')

        elif message.lower() == 'лениво блокировать удар':
            if temp[user_id]['last'] == 'lazy_block':
                send_message(user_id, 'Ты только что блокировал удар. Твое тело не выдержит второго удара.')
                return

            temp[user_id]['last'] = 'lazy_block'
            temp[user_id]['stamina'] += 25
            text = 'Ты вало отбил эту атаку'
            pve_battle().battle(user_id, _text=text, _lock = 'lazy')

        elif message.lower() == 'поспать':
            if temp[user_id]['last'] == 'lazy':
                send_message(user_id, 'Ты только что cпал. У нас разве соревнование кто дольше спит?')
                return

            temp[user_id]['last'] = 'lazy'
            text = 'Ты выспался посередине боя'
            temp[user_id]['stamina'] = 100
            pve_battle().battle(user_id, _text= text)

        else:
            pass

    @staticmethod
    def battle(user_id , _text = '', _lock = None):
        _hero = db.get_hero(user_id)
        _equip = db.get_equip(user_id)

        button = []

        text = _text

        if temp[user_id]['blood']:
            _blood = 3
            temp[user_id]['monster']['hp'] = temp[user_id]['monster']['hp'] - _blood
            text += '\n' + temp[user_id]['monster']['name'] + ' истекает кровью на ' + str(_blood) + '🖤'

        if temp[user_id]['monster']['hp'] > 0:

            if str(_lock) == 'lazy':
                _wayyyyy = oldbattle().get_def_atk(random.randint(*temp[user_id]['monster']['damage']), get_def(user_id))
                _wayyyyy = round(_wayyyyy * 0.5)
                text += '\n' + temp[user_id]['monster']['name'] + ' нанес тебе ' + str(_wayyyyy) + '💥 урона'
                temp[user_id]['hp'] -= _wayyyyy
            elif str(_lock) == 'full':
                text += '\n' + temp[user_id]['monster']['name'] + ' громко и звонко ударился(лась) об твою защиту'
            else:
                _wayyyyy = oldbattle().get_def_atk(random.randint(*temp[user_id]['monster']['damage']), get_def(user_id))
                text += '\n' + temp[user_id]['monster']['name'] + ' нанес тебе ' + str(_wayyyyy) + '💥 урона'
                temp[user_id]['hp'] -= _wayyyyy

        else:
            text = pve_battle().header(user_id) + text

            if temp[user_id]['monster']['gold'] or temp[user_id]['monster']['diamond'] or temp[user_id]['monster']['loot']:
                text += pve_battle().give_stuff(user_id)

            _quest = db.get_quest(user_id)
            if _quest['monster']:
                if monsters[_quest['monster']]['name'] == temp[user_id]['monster']['name']:
                    db.change_quest(user_id, _quest['monster'], int(_quest['killed']) + 1, _quest['need'])

            db.add_rating(user_id, 1)

            if 'room' in temp[user_id]['monster']:
                _room = temp[user_id]['monster']['room']
                send_message(user_id, text)
                del temp[user_id]
                eval(_room)(user_id)
                return

            del temp[user_id]
            send_message(user_id, text, get_start_button(user_id))
            return

        if temp[user_id]['hp'] < 1:
            text += '\n\n' + temp[user_id]['monster']['name'] + ' одолел тебя.\nТебе должно быть стыдно.'
            db.add_rating(user_id, -1)
            text = pve_battle().header(user_id) + text
            del temp[user_id]
            send_message(user_id, text, get_start_button(user_id))
            return

        if _equip['gun']:
            button.append(['Ударить оружием'])
        button.append(['Пнуть противника'])
        button.append(['Лениво блокировать удар'])
        button.append(['Блокировать удар'])
        button.append(['Поспать'])

        text = pve_battle().header(user_id) + text

        send_message(user_id, text, button)
        set_hand(user_id, pve_battle().battle_handler)

    @staticmethod
    def give_stuff(user_id):
        return ('')
        _inventory = db.get_inventory(user_id)

        text = ''
        if temp[user_id]['monster']['gold']:
            text += '\nПолучено : ' + str(i_get_gold(user_id, wars=random.randint(*temp[user_id]['monster']['gold']))) + ' золота'
        if temp[user_id]['monster']['diamond']:
            text += '\nПолучено : ' + str(i_get_diamond(user_id, wars=random.randint(*temp[user_id]['monster']['diamond']))) + ' алмазов'
        if temp[user_id]['monster']['loot'] and random.random() < 0.15:
            _res = temp[user_id]['monster']['loot']

            if _res[0] == 'resource':
                _number = random.randint(*_res[2])
                db.add_inventory(user_id, _res[1], _number)
                text += '\nПолучено: ' + names.item[_res[1]] + ' x' + str(_number)

            elif _res[0] in ['head', 'mask', 'body', 'gun', 'legs'] and len(_inventory) < 15:
                text += '\nПолучено: ' + eval('equip.' + _res[0])[_res[1]][0]
                db.add_inventory_item(user_id, _res[0], _res[1], 1)

        return (text)

    @staticmethod
    def start(user_id, monster):
        button = []
        _equip = db.get_equip(user_id)
        _hero = db.get_hero(user_id)

        text = pve_battle().header(user_id)
        text += 'Тебе предстоит битва с ' + monsters[monster]['name']
        text += '\nВыбери удар из списка ниже.'

        temp[user_id] = {
            'battle' : 'pve',
            'monster' : {'name' : 'Рыцарь','hp' : 1000,'damage' : [40,50],'gold' : [1,50],'diamond' : False,'loot' : None},
            'hp' : _hero['hp'],
            'stamina' : 100,
            'last' : '',
            'blood' : False
        }

        if _equip['gun']:
            button.append(['Ударить оружием'])
        button.append(['Пнуть противника'])
        button.append(['Блокировать удар'])
        button.append(['Поспать'])

        send_message(user_id, text, button)
        set_hand(user_id, pve_battle().battle_handler)