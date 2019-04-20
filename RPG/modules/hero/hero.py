def bot_hero(user_id):
    text = get_hero(user_id)
    text += i_hero_buff(user_id)
    text += '\n\n🎒Инвентарь {}'.format(len(db.get_inventory(user_id)))
    #text += '\n📦Склад 99/1000'
    text += '\n\n' + i_hero_equip(user_id)
    send_message(user_id, text,[['🎒Инвентарь', '🐣Скиллы'], ['🔨Крафт', '🧪Алхимия'], ['📦Склад ресурсов', '⬅️ Назад']])
    set_hand(user_id, hero_hand)

def hero_hand(user_id, message):
    if message == '🎒Инвентарь':
        i_hero_inventory(user_id)
    elif message == '📦Склад ресурсов':
        hero_store(user_id)
    elif message == '🔨Крафт':
        game_craft(user_id)
    elif message == '🧪Алхимия':
        game_alchemy(user_id)
        return
    elif message == '⬅️ Назад':
        start_game(user_id)
    elif message == '🐣Скиллы':
        bot_hero_skill(user_id)
    else :
        pass


def i_hero_equip(user_id):
    _equip = db.get_equip(user_id)
    text = '🎽Экипировка:'
    if _equip['head']:
        item = _equip['head']
        if len(item) == 1:
            text += '\n' + equip.head[item[0]][0]
        else:
            text += '\n🖊' + item[1]
        if int(equip.head[item[0]][1]) > 0:
            text += ' 🛡' + str(int(equip.head[item[0]][1]))
        if int(equip.head[item[0]][2]) > 0:
            text += ' ⚔️' + str(int(equip.head[item[0]][2]))

    if _equip['mask']:
        item = _equip['mask']
        if len(item) == 1:
            text += '\n' + equip.mask[item[0]][0]
        else:
            text += '\n🖊' + item[1]
        if int(equip.mask[item[0]][1]) > 0:
            text += ' 🛡' + str(int(equip.mask[item[0]][1]))
        if int(equip.mask[item[0]][2]) > 0:
            text += ' ⚔️' + str(int(equip.mask[item[0]][2]))

    if _equip['body']:
        item = _equip['body']
        if len(item) == 1:
            text += '\n' + equip.body[item[0]][0]
        else:
            text += '\n🖊' + item[1]
        if int(equip.body[item[0]][1]) > 0:
            text += ' 🛡' + str(int(equip.body[item[0]][1]))
        if int(equip.body[item[0]][2]) > 0:
            text += ' ⚔️' + str(int(equip.body[item[0]][2]))

    if _equip['legs']:
        item = _equip['legs']
        if len(item) == 1:
            text += '\n' + equip.legs[item[0]][0]
        else:
            text += '\n🖊' + item[1]
        if int(equip.legs[item[0]][1]) > 0:
            text += ' 🛡' + str(int(equip.legs[item[0]][1]))
        if int(equip.legs[item[0]][2]) > 0:
            text += ' ⚔️' + str(int(equip.legs[item[0]][2]))

    if _equip['gun']:
        item = _equip['gun']
        if len(item) == 1:
            text += '\n' + equip.gun[item[0]][0]
        else:
            text += '\n🖊' + item[1]
        if int(equip.gun[item[0]][1]) > 0:
            text += ' 🛡' + str(int(equip.gun[item[0]][1]))
        if int(equip.gun[item[0]][2]) > 0:
            text += ' ⚔️' + str(int(equip.gun[item[0]][2]))

    if _equip['shand']:
        item = _equip['shand']
        if len(item) == 1:
            text += '\n' + equip.shand[item[0]][0]
        else:
            text += '\n🖊' + item[1]
        if int(equip.shand[item[0]][1]) > 0:
            text += ' 🛡' + str(int(equip.shand[item[0]][1]))
        if int(equip.shand[item[0]][2]) > 0:
            text += ' ⚔️' + str(int(equip.shand[item[0]][2]))

    if _equip['amulet']:
        item = _equip['amulet']
        if len(item) == 1:
            text += '\n' + equip.amulet[item[0]][0]
        else:
            text += '\n🖊' + item[1]

    return (text)


def hero_store(user_id):
    _store = db.get_user_inventory(user_id)
    enable_hero_store = False
    text = 'Ваши ресурсы:'
    #if _store['stick'] != 0 :
    #    enable_hero_store = True
    #    text += '\nВеток: ' + str(_store['stick']) + ' штук'
    for _item in _store:
        if _store[_item] != 0 and _item != 'user_id' and _item != 'logic':
            enable_hero_store = True
            text += '\n{}: {} штук'.format(names.item[_item], _store[_item])
    if not enable_hero_store:
        text = 'У вас нету ресурсов.'
    send_message(user_id, text)
