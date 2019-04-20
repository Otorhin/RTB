def traveler(user_id):
    _quest = db.get_quest(user_id)
    _inventory = db.get_inventory(user_id)
    if len(_inventory) >= 30:
        send_message(user_id, '"К сожалению мне нечего тебе предложить.\nОсвободи рюкзачек."')
        return
    text = '"Здравствуй, славный воин! Что-же тебе понадобилось?"'
    button = []

    text += '\n\nАлюминиевый меч - 400💰'
    button.append(['Алюминиевый меч'])
    text += '\n\nАлюминиевый топор - 400💰'
    button.append(['Алюминиевый топор'])

    text += '\n\nМедный топор - 800💰 20💎'
    button.append(['Медный топор'])
    text += '\n\nМедный меч - 800💰 20💎'
    button.append(['Медный меч'])

    if int(_quest['allquest']) > 18:
        text += '\n\nИнструменты кузнеца - x💰 x💎'
        button.append(['Инструменты кузнеца'])

    button.append(['Назад'])
    send_message(user_id, text, button, parse_mode='markdown')
    set_hand(user_id, traveler_hand)


traveler_gun1 = {
    'алюминиевый меч' : '1',
    'алюминиевый топор': '2'
}

traveler_gun2 = {
    'медный топор': '4',
    'медный меч' : '3'
}


def traveler_hand(user_id, message):
    _quest = db.get_quest(user_id)
    _hero = db.get_hero(user_id)
    _inventory = db.get_inventory(user_id)
    if message == 'Назад':
        bot_shop(user_id)

    elif _hero['gold'] >= 400 and len(_inventory) <= 30 and message.lower() in traveler_gun1:
        db.add_gold(user_id, -400)
        db.add_inventory_item(user_id, 'gun', traveler_gun1[message.lower()])
        _text = equip.gun[traveler_gun1[message.lower()]][0]
        send_message(user_id, 'Вы приобрели ' + _text)

    elif _hero['gold'] >= 800 and _hero['diamond'] >= 20 and len(_inventory) <= 30 and message.lower() in traveler_gun2:
        db.add_gold(user_id, -800)
        db.add_diamond(user_id, -20)
        db.add_inventory_item(user_id, 'gun', traveler_gun2[message.lower()])
        _text = equip.gun[traveler_gun2[message.lower()]][0]
        send_message(user_id, 'Вы приобрели ' + _text)

    elif _hero['gold'] >= 500 and _hero['diamond'] >= 25 and message == 'Инструменты кузнеца' and int(_quest['allquest']) > 18:
        db.add_gold(user_id, -500)
        db.add_diamond(user_id, -25)
        db.add_inventory(user_id, 'blacksmithtools', 1)
        send_message(user_id, 'Вы приобрели кузнечные инструменты.')

    else:
        send_message(user_id, 'У тебя не достаточно денег, или нет места.')