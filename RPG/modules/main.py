def _get_hero(user_id):
    _hero = db.get_hero(user_id)
    text = _hero['nick']
    text += '\n|❤️' + str(_hero['hp'])
    text += '|🏆' + str(_hero['rating'])
    text += '\n|🗡' + str(get_atk(user_id))
    text += '|🛡' + str(get_def(user_id))
    text += '\n|💰' + str(_hero['gold'])
    text += '|💎 | 🍕' + str(_hero['diamond'])
    return text

def get_hero(user_id):
    _hero = db.get_hero(user_id)
    text = '👤' + _hero['nick']
    text += '\n❤️{hp} 🏆{rating}'.format(**_hero)
    text += '\n🀄️{lvl} 💡{exp}/{new_exp}'.format(**_hero)
    text += '\n🗡{} 🛡{}'.format(get_atk(user_id), get_def(user_id))
    text += '\n💰{gold} 💎{diamond} 🍕{pizza}'.format(**_hero)

    _new_rating = (get_atk(user_id) / 2) + (get_def(user_id) / 10) + (int(_hero['hp']) / 10)
    text += '\n🥽' + str(_new_rating)

    return text


def i_hero_inventory(user_id):
    _inventory = db.get_inventory(user_id)
    button = None
    if len(_inventory) == 0:
        text = ('В вашем инвентаре пусто')
        send_message(user_id, text, button)
        return
    else :
        text = 'В вашем инвентаре : '
        button = []
        _potion = {}
    for all in _inventory:
        if all[0] == 'head':
            if all[2]:
                text += '\n🖊' + all[2]
            else:
                text += '\n' + equip.head[all[1]][0] 
            if int(equip.head[all[1]][1]) > 0:
                text += ' 🛡' + str(int(equip.head[all[1]][1]))
            if int(equip.head[all[1]][2]) > 0:
                text += ' ⚔️' + str(int(equip.head[all[1]][2]))
        elif all[0] == 'body':
            if all[2]:
                text += '\n🖊' + all[2]
            else:
                text += '\n' + equip.body[all[1]][0]
            if int(equip.body[all[1]][1]) > 0:
                text += ' 🛡' + str(int(equip.body[all[1]][1]))
            if int(equip.body[all[1]][2]) > 0:
                text += ' ⚔️' + str(int(equip.body[all[1]][2]))
        elif all[0] == 'legs':
            if all[2]:
                text += '\n🖊' + all[2]
            else:
                text += '\n' + equip.legs[all[1]][0]
            if int(equip.legs[all[1]][1]) > 0:
                text += ' 🛡' + str(int(equip.legs[all[1]][1]))
            if int(equip.legs[all[1]][2]) > 0:
                text += ' ⚔️' + str(int(equip.legs[all[1]][2]))
        elif all[0] == 'mask':
            if all[2]:
                text += '\n🖊' + all[2]
            else:
                text += '\n' + equip.mask[all[1]][0]
            if int(equip.mask[all[1]][1]) > 0:
                text += ' 🛡' + str(int(equip.mask[all[1]][1]))
            if int(equip.mask[all[1]][2]) > 0:
                text += ' ⚔️' + str(int(equip.mask[all[1]][2]))
        elif all[0] == 'gun':
            if all[2]:
                text += '\n🖊' + all[2]
            else:
                text += '\n' + equip.gun[all[1]][0]
            if int(equip.gun[all[1]][1]) > 0:
                text += ' 🛡' + str(int(equip.gun[all[1]][1]))
            if int(equip.gun[all[1]][2]) > 0:
                text += ' ⚔️' + str(int(equip.gun[all[1]][2]))
        elif all[0] == 'shand':
            if all[2]:
                text += '\n🖊' + all[2]
            else:
                text += '\n' + equip.shand[all[1]][0]
            if int(equip.shand[all[1]][1]) > 0:
                text += ' 🛡' + str(int(equip.shand[all[1]][1]))
            if int(equip.shand[all[1]][2]) > 0:
                text += ' ⚔️' + str(int(equip.shand[all[1]][2]))
        elif all[0] == 'amulet':
            if all[2]:
                text += '\n🖊' + all[2]
            else:
                text += '\n' + equip.amulet[all[1]][0]
        elif all[0] == 'potion':
            if all[1] in _potion:
                _potion[all[1]] += 1
            else:
                _potion[all[1]] = 1
        text += '\nНадеть : ' + '/equip_' + str(all[3])
        text += '\nВыкинуть : ' + '/drop_{}'.format(all[3])
    for _all in _potion:
        text += '\n' + equip.potion[_all][0] + ' x' + str(_potion[_all])
        text += '\nВыпить : ' + '/potion_' + _all
    button.append(['Назад'])
    set_hand(user_id, equip_inventory_new)
    send_message(user_id, text, button)

def equip_inventory_new(user_id, message):
    _inventory = db.get_inventory(user_id)
    _equip = db.get_equip(user_id)
    if message.startswith('/equip_') or message.startswith('/drop_'):
        message = message.split('_')
        _inventorrr = db.get_inventory_id(user_id)
        if message[1] in _inventorrr:
            if message[0] == '/equip':
                if _equip[_inventorrr[message[1]]]:
                    db.off_equip(_inventorrr[message[1]])
                db.add_equip(message[1])
                text = 'Вы быстро напялили это шмотье.'
            else:
                db.del_inventory_item(message[1])
                text = 'Вы выкинули данный предмет.'
            send_message(user_id, text)
        else :
            text = 'У тебя такого нет'
            send_message(user_id, text)
    elif message.startswith('/potion_'):
        _data = message.split('_')
        _buff = get_all_buff(user_id)
        if _data[1] in equip.potion and ['potion', _data[1]] in _inventory and _data[1] not in _buff:
            i_hero_add_buff(user_id, _data[1])
            _potion = equip.potion[_data[1]]
            if _potion[1] != 0:
                db.add_atk(user_id, _potion[1])
                bd_adventure.append(['db.add_atk', _potion[4], [user_id, -_potion[1]]])
            if _potion[2] != 0:
                db.add_def(user_id, _potion[2])
                bd_adventure.append(['db.add_def', _potion[4], [user_id, -_potion[2]]])
            if _potion[3] != 0:
                db.add_max_hp(user_id, _potion[3])
                bd_adventure.append(['db.add_max_hp', _potion[4], [user_id, -_potion[3]]])
            if _potion[5] != 0:
                db.add_svamp(user_id, _potion[5])
                bd_adventure.append(['db.add_svamp', _potion[4], [user_id, -_potion[5]]])
            

            db.del_inventory_item(user_id, 'potion', _data[1])
            bd_adventure.append(['i_hero_del_buff', _potion[4], [user_id, _data[1]]])
            text = '🧪Ты выпил *{}*'.format(_potion[0])
            send_message(user_id, text, parse_mode='Markdown')
        elif _data[1] in _buff:
            send_message(user_id, 'Ты уже употреблял это зелье недавно.', parse_mode='Markdown')
        elif len(_buff) > 2:
            send_message(user_id, 'Ты выпил слишком много разной выпивки.', parse_mode='Markdown')
        else:
            send_message(user_id, '*Произошла ошибка.*\nВозможно у тебя уже нет данного зелья.', parse_mode='Markdown')
            
    elif message.lower() == 'назад':
        start_game(user_id)
    else :
        pass
