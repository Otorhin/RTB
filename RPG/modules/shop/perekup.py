def perekup(user_id):
    text = 'Да здравствует, славный воин! Что тебе надобно?'
    button = [['Продать ресурсы'], ['Купить ресурсы'], ['Назад']]
    send_message(user_id, text, button)
    set_hand(user_id, perekup_hand)


def perekup_hand(user_id, message):
   if message.lower() == 'продать ресурсы':
       perekup_sell(user_id)
   elif message.lower() == 'купить ресурсы':
       perekup_buy(user_id)
   elif message.lower() == 'назад':
       bot_shop(user_id)
   else:
       pass


def perekup_sell(user_id):
    _storee = db.get_user_inventory(user_id)
    text = 'Что ты желаешь продать?'
    text += '\nЦена продажи всех ресурсов - 4 золота.'
    button = []
    text = 'Что вы желаете продать?'
    if _storee['stick'] != 0 :
        button.append(['Ветка'])
    if _storee['coal'] != 0 :
        button.append(['Уголь'])
    if _storee['iron'] != 0 :
        button.append(['Железо'])
    if _storee['stone'] != 0 :
        button.append(['Камень'])
    if len(button) == 0:
        send_message(user_id, 'К сожалению, у тебя нет ресурсов')
        return
    button.append(['Назад'])
    send_message(user_id, text, button)
    set_hand(user_id, perekup_sell_hand)


def perekup_sell_hand(user_id, message):
    _hero = db.get_hero(user_id)
    _store = db.get_user_inventory(user_id)

    if message.lower() == 'ветка' and _store['stick'] != 0:
        db.add_inventory(user_id, 'stick', -1)
        db.add_gold(user_id, 4)
        text = 'Вы продали ветку за 4💰.'
        text += '\nТеперь у тебя ' + str(_store['stick']) + ' веток'
        text += 'Осталось ' + str(_hero['gold'] + 4) + '💰'
        send_message(user_id, text)

    elif message.lower() == 'уголь' and _store['coal'] != 0:
        db.add_inventory(user_id, 'coal', -1)
        db.add_gold(user_id, 4)
        text = 'Вы продали угль за 4💰.'
        text += '\nТеперь у тебя ' + str(_store['coal']) + ' угля'
        text += 'Осталось ' + str(_hero['gold'] + 4) + '💰'
        send_message(user_id, text)

    elif message.lower() == 'камень' and _store['stone'] != 0:
        db.add_inventory(user_id, 'stone', -1)
        db.add_gold(user_id, 4)
        text = 'Вы продали камень за 4💰.'
        text += '\nТеперь у тебя ' + str(_store['stone']) + ' камней'
        text += 'Осталось ' + str(_hero['gold'] + 4) + '💰'
        send_message(user_id, text)

    elif message.lower() == 'железо' and _store['iron'] != 0:
        db.add_inventory(user_id, 'iron', -1)
        db.add_gold(user_id, 4)
        text = 'Вы продали железо за 4💰.'
        text += '\nТеперь у тебя ' + str(_store['iron']) + ' железа'
        text += 'Осталось ' + str(_hero['gold'] + 4) + '💰'
        send_message(user_id, text)

    elif message.lower() == 'назад':
        perekup(user_id)
        return
    else:
        return
    perekup_sell(user_id)


def perekup_buy(user_id):
    text = 'Что ты желаешь купить?'
    text += '\nЦена покупки всех ресурсов - 5 золота.'
    button = [['Ветка', 'Уголь'], ['Камень', 'Железо'], ['Назад']]
    send_message(user_id, text, button)
    set_hand(user_id, perekup_buy_hand)


def perekup_buy_hand(user_id, message):
    _hero = db.get_hero(user_id)
    _storee = db.get_user_inventory(user_id)

    if message.lower() == 'ветка' and _hero['gold'] >= 5:
        db.add_inventory(user_id, 'stick', 1)
        db.add_gold(user_id, -5)
        text = 'Вы приобрели ветку за 5💰.'
        text += '\nТеперь у тебя ' + str(_storee['stick'] + 1) + ' веток'
        text += '\nОсталось ' + str(_hero['gold'] - 5) + '💰'
        send_message(user_id, text)

    elif message.lower() == 'уголь' and _hero['gold'] >= 5:
        db.add_inventory(user_id, 'coal', 1)
        db.add_gold(user_id, -5)
        text = 'Вы приобрели уголь за 5💰.'
        text += '\nТеперь у тебя ' + str(_storee['coal'] + 1) + ' угля'
        text += '\nОсталось ' + str(_hero['gold'] - 5) + '💰'
        send_message(user_id, text)

    elif message.lower() == 'камень' and _hero['gold'] >= 5:
        db.add_inventory(user_id, 'stone', 1)
        db.add_gold(user_id, -5)
        text = 'Вы приобрели камень за 5💰.'
        text += '\nТеперь у тебя ' + str(_storee['stone'] + 1) + ' камня'
        text += '\nОсталось ' + str(_hero['gold'] - 5) + '💰'
        send_message(user_id, text)

    elif message.lower() == 'железо' and _hero['gold'] >= 5:
        db.add_inventory(user_id, 'iron', 1)
        db.add_gold(user_id, -5)
        text = 'Вы приобрели железо за 5💰.'
        text += '\nТеперь у тебя ' + str(_storee['iron'] + 1) + ' железа'
        text += '\nОсталось ' + str(_hero['gold'] - 5) + '💰'
        send_message(user_id, text)

    elif message.lower() == 'назад':
        perekup(user_id)

    elif _hero['gold'] < 5:
        send_message(user_id, 'У тебя недостаточно денег.')

    else:
        pass
