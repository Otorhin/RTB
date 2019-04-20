def start_tutorial(user_id, ref = None):
    send_sticker(user_id, 'CAADAgADWgADP1c0GpzyckP3XK1hAg')
    if ref:
        db.change_ref(user_id, ref)
    text = '`Приветствую тебя, путешественник. Рад видеть тебя, готового к приключениям. Кто знает, какая судьба тебя ждёт? Станешь ли ты великим воином, или сдашься и падёшь на пол пути? Это зависит только от тебя. Но могучему герою нужно имя, подобающее его свершениям. \nКак же к тебе будут обращатся?`'
    send_message(user_id, text, parse_mode = 'Markdown')
    set_hand(user_id, nick_tutorial)


def nick_tutorial(user_id, message):
    if len(otrh_f.switch_chars(message)) < 4 or len(otrh_f.switch_chars(message)) > 20:
        send_message(user_id, 'Твой ник должен соответсвовать идеалам. От 4-ех до 20-ти символов.\nА также содержать только буквы и цифры.')
        return
    temp[user_id] = {}
    temp[user_id]['new_nick'] = otrh_f.switch_chars(message)
    text = 'Твое имя: ' + temp[user_id]['new_nick'] + '?'
    send_message(user_id, text, [['Да', 'Нет']])
    set_hand(user_id, nick_tutorial2)


def nick_tutorial2(user_id, message):
    _hero = db.get_hero(user_id)
    if message.lower() == 'да':
        db.change_nick(user_id, temp[user_id]['new_nick'])
        del temp[user_id]
        bot_end_tutorial(user_id)
    if message.lower() == 'нет':
        text = '`Так назови свое настоящее имя.`'
        send_message(user_id, text, parse_mode = 'Markdown')
        set_hand(user_id, nick_tutorial)
    else :
        pass