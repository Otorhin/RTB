def strange_man(user_id):
    text = 'На моем прилавке находятся, странные для многих вещей.'
    text += '\n\nЗелье быстрых приключений'
    text += '\nДает возможность ходить в приключения без остановки на 30 минут'
    text += '\nЦена 75💎'
    button = [
        ['Купить зелье быстрого приключения'],
        ['Назад']
    ]
    send_message(user_id, text, button)
    set_hand(user_id, strange_man_hand)


def strange_man_hand(user_id, message):
    _hero = db.get_hero(user_id)

    if message.lower() == 'назад':
        bot_shop(user_id)
    elif message.lower() == 'купить зелье быстрого приключения':
        if _hero['buff']:
            send_message(user_id, 'Ты уже под действием некоего зелья.')
        elif _hero['diamond'] < 75:
            send_message(user_id, 'У тебя не достаточно камней.')
        else:
            db.add_diamond(user_id, -75)
            db.change_buff(user_id, 'adventure')
            bd_adventure.append(['db.change_buff', 31, [user_id, None]])
            send_message(user_id, '🍸Выпито зелье быстрого приключения')
    else:
        pass