fast_command['/ashdasifhubewvhovnwe'] = 'hero_weapon'
def hero_weapon(user_id, message):
    #_weapon = db.get_user_weapon(user_id)
    _weapon = {
        'sword' : 0,
        'axe' : 0,
        'knife' : 5
    }

    text = 'Твое мастерство владеть оружием:'

    text += '\n\nВладение мечами: '
    text += get_lvl_weapon(_weapon['sword'])

    text += '\n\nВладение топорами: '
    text += get_lvl_weapon(_weapon['axe'])

    text += '\n\nВладение ножами: '
    text += get_lvl_weapon(_weapon['knife'])

    send_message(user_id, text)


def get_lvl_weapon(exp):
    if exp < 100:
        text = '0 уровень (' + str(exp) + '/100)'
    elif exp < 500:
        text = '1 уровень (' + str(exp) + '/500)'
    elif exp < 1000:
        text = '2 уровень (' + str(exp) + '/1000)'
    elif exp < 2000:
        text = '3 уровень (' + str(exp) + '/2000)'
    elif exp < 3000:
        text = '4 уровень (' + str(exp) + '/3000)'
    else:
        text = '5 уровень (' + str(exp) + '/3000)'
    return (text)


def hero_battle_skill(user_id):
    text = 'Твои боевые приемы:'
    text += '\n\nУдар оружием (1 уровень)'
    text += '\n`Удар противника оружием.`'
    text += '\n\nПнуть противника (1 уровень)'
    text += '\n`Пинок под зад противника`'
    text += '\n\nБлокирование удара (1 уровень)'
    text += '\n`Попытка защититься от удара противника`'
    text += '\n\nЛенивое блокирование удара (1 уровень)'
    text += '\n`Сонная попытка защититься от удара противника`'
    text += '\n\nСон (1 уровень)'
    text += '\n`Сон посреди боя.`'
    send_message(user_id, text, parse_mode = 'Markdown')