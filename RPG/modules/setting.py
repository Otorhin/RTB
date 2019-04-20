def bot_setting(user_id):
    _hero = db.get_hero(user_id)
    text = 'Что вы желаете сделать?'
    button = [['🖊Сменить ник'],['🗯Пригласить друга'], ['⬅️ Назад']]
    if int(_hero['pizza']) > 2:
        button[0].append('🍕Сменить ник')
    send_message(user_id, text,button)
    set_hand(user_id, bot_setting_hand)

def bot_setting_hand(user_id, message):
    _hero = db.get_hero(user_id)
    if message == '🖊Сменить ник':
        send_message(user_id, 'Введите ваш новый ник.', [[otrh_f.nick_generator()]])
        set_hand(user_id, new_nick)
    if message == '🍕Сменить ник' and int(_hero['pizza']) > 2:
        send_message(user_id, 'Введите ваш новый ник.', [[otrh_f.nick_generator()]])
        set_hand(user_id, new_nick_donat)
    elif message == '🗯Пригласить друга':
        text = '\nСсылка для приглашения вашего друга : t.me/rogtorbot?start=' + str(user_id)
        send_message(user_id, text)
    elif message == '⬅️ Назад':
        start_game(user_id)
    else :
        pass

def new_nick(user_id, message):
    if len(otrh_f.switch_chars(message)) < 4 or len(otrh_f.switch_chars(message)) > 20:
        send_message(user_id, 'Твой ник должен соответсвовать идеалам. От 4-ех до 20-ти символов.\nА также содержать только буквы и цифры.')
        return
    temp[user_id] = {}
    temp[user_id]['new_nick'] = otrh_f.switch_chars(message)
    text = 'Ваш новый ник : ' + temp[user_id]['new_nick']
    send_message(user_id, text, [['Да', 'Нет']])
    set_hand(user_id, new_nick_hand)

def new_nick_hand(user_id, message):
    _hero = db.get_hero(user_id)
    if message.lower() == 'да':
        new_nickname = temp[user_id]['new_nick']
        db.change_nick(user_id, new_nickname)
        text = 'Поздравляю, вы сменили ник на ' + new_nickname
        del temp[user_id]
        send_message(user_id, text)
        start_game(user_id)
    if message.lower() == 'нет':
        start_game(user_id)
    else :
        pass




def new_nick_donat(user_id, message):
    if len(otrh_f.switch_chars_donat(message)) < 2 or len(otrh_f.switch_chars_donat(message)) > 40:
        send_message(user_id, 'Твой ник должен соответсвовать идеалам. От 2-ех до 40-ти символов.\nА также содержать только буквы и цифры, ну и не более одного пробела подряд.')
        return
    temp[user_id] = {}
    temp[user_id]['new_nick'] = otrh_f.switch_chars_donat(message)
    text = 'Ваш новый ник : ' + temp[user_id]['new_nick']
    send_message(user_id, text, [['Да', 'Нет']])
    set_hand(user_id, new_nick_hand_donat)

def new_nick_hand_donat(user_id, message):
    _hero = db.get_hero(user_id)
    if message.lower() == 'да':
        new_nickname = temp[user_id]['new_nick']
        db.change_nick(user_id, new_nickname)
        text = 'Поздравляю, вы сменили ник на ' + new_nickname
        del temp[user_id]
        send_message(user_id, text)
        db.add_pizza(user_id, -3)
        start_game(user_id)
    if message.lower() == 'нет':
        start_game(user_id)
    else :
        pass