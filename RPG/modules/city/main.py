def bot_city(user_id):
    text = 'Вы входите в центр города. Куда бы вы хотели пойти дальше?'
    button = [['🏚Магазины'], ['🍺Таверна', '⬅️ Домой']]
    send_message(user_id, text, button)
    set_hand(user_id, bot_city_hand)

def bot_city_hand(user_id, message):
    if message == '🏚Магазины':
        bot_shop(user_id)
    elif message == '🍺Таверна':
        city_tavern(user_id)
    elif message == '⬅️ Домой':
        start_game(user_id)
    else:
        pass