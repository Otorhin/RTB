def bartender(user_id):
    text = 'На моем прилавке ты можешь купить много разных напитков.'
    text += '\n\nЗелье атаки'
    text += '\nДает 50 очков силы на 30 минут'
    text += '\nЦена 1000💰'
    text += '\n\nЗелье защиты'
    text += '\nДает 50 очков защиты на 30 минут'
    text += '\nЦена 750💰'
    button = [
        ['Купить зелье атаки'],
        ['Купить зелье защиты'],
        ['Назад']
    ]
    send_message(user_id, text, button)
    set_hand(user_id, bartender_hand)



def bartender_hand(user_id, message):
    _hero = db.get_hero(user_id)

    if message.lower() == 'назад':
        bot_shop(user_id)

    elif message.lower() == 'купить зелье атаки':
        if 'atk' in get_all_buff(user_id):
            send_message(user_id, 'Ты уже под действием зелья.')
        elif _hero['gold'] < 1000:
            send_message(user_id, 'У тебя не достаточно монет.')
        else:
            db.add_gold(user_id, -1000)
            i_hero_add_buff(user_id, 'atk')
            db.add_atk(user_id, 50)
            bd_adventure.append(['i_hero_del_buff', 31, [user_id, 'atk']])
            bd_adventure.append(['db.add_atk', 31, [user_id, -50]])
            send_message(user_id, '🍸Выпито зелье атаки')

    elif message.lower() == 'купить зелье защиты':
        if 'def' in get_all_buff(user_id):
            send_message(user_id, 'Ты уже под действием зелья.')
        elif _hero['gold'] < 750:
            send_message(user_id, 'У тебя не достаточно монет.')
        else:
            db.add_gold(user_id, -750)
            i_hero_add_buff(user_id, 'def')
            db.add_def(user_id, 50)
            bd_adventure.append(['i_hero_del_buff', 31, [user_id, 'def']])
            bd_adventure.append(['db.add_def', 31, [user_id, -50]])
            send_message(user_id, '🍸Выпито зелье защиты')

    else:
        pass