def get_start_button(user_id):
    _hero = db.get_hero(user_id)
    set_hand(user_id, start_game_hand)
    button = [['👤Герой','🏕B приключeниe'],['🏛Город'],['⚙️Профиль', '👥Гильдия']]
    return button

def start_game(user_id):
    text = get_hero(user_id)
    button = get_start_button(user_id)
    send_message(user_id, text, button)

def start_game_hand(user_id, message):
    _hero = db.get_hero(user_id)
    if message == '👤Герой':
        bot_hero(user_id)
        return
    elif message == '👥Гильдия':
        guild_info(user_id)
        return
    elif message == '🏕B приключeниe':
        adventure().choice(user_id)
        return
    elif message == '🏛Город':
        bot_city(user_id)
        return
    elif message == '⚙️Профиль':
        bot_setting(user_id)
        return
    else :
        start_game(user_id)
        return