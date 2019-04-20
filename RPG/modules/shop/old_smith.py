def old_smith(user_id):
    _inventory = db.get_inventory(user_id)
    if len(_inventory) >= 30:
        send_message(user_id, '"К сожалению, мне нечего тебе предложить.\nОсвободи рюкзачек."')
        return
    button = []
    text = '"Здравствуй, внучек величавый. Что в этот раз тебе нужно из моего скудного ассортимента?"'
    text += '\n\nКожаная коробочка - 300💰'
    text += '\n`Содержит в себе случайную броню`'
    button.append(['Кожаная коробочка'])

    text += '\n\nСеребряная коробочка - 600💰 10💎'
    text += '\n`Содержит в себе случайную броню`'
    button.append(['Серебряная коробочка'])


    button.append(['Назад'])
    send_message(user_id, text, button, parse_mode='markdown')
    set_hand(user_id, old_smith_hand)


def old_smith_hand(user_id, message):
    _hero = db.get_hero(user_id)
    _inventory = db.get_inventory(user_id)
    if _hero['gold'] >= 300 and len(_inventory) <= 30 and message.lower() == 'кожаная коробочка':
        db.add_gold(user_id, -300)
        _rar = '1'
        _rar1 = ['head', 'mask', 'body', 'legs']
        random.shuffle(_rar1)
        random.shuffle(_rar1)
        _rar1 = random.choice(_rar1)
        _text = 'equip.' + _rar1
        _text = eval(_text)[_rar][0]
        db.add_inventory_item(user_id, _rar1, _rar)
        send_message(user_id, 'Вы приобрели ' + _text)

    elif message.lower() == 'серебряная коробочка' and _hero['gold'] >= 600 and _hero['diamond'] >= 10 and len(_inventory) <= 30:
        db.add_gold(user_id, -600)
        db.add_diamond(user_id, -10)
        _rar = '2'
        _rar1 = ['head', 'mask', 'body', 'legs']
        random.shuffle(_rar1)
        random.shuffle(_rar1)
        _rar1 = random.choice(_rar1)
        _text = 'equip.' + _rar1
        _text = eval(_text)[_rar][0]
        db.add_inventory_item(user_id, _rar1, _rar)
        send_message(user_id, 'Вы приобрели ' + _text)
    elif message == 'Назад':
        bot_shop(user_id)
    else:
        send_message(user_id, 'У тебя не достаточно денег, или нет места.')