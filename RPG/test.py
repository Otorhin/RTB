import os

def damage_mob():
    defe = 2
    d_max = 30
    d_min = 20
    dmg = random.randint(d_min, d_max)
    dmg *= 1 - (defe/ (7 + defe))
    #dmg *= random.random()
    return (round(dmg))

def chance_upgrade(i):
    chance = (100 / i) * 3
    text = 'Уровень ' + str(i) + ' : ' + str(round(chance)) + '%'
    print(text)
    return (round(chance))


def monster_battle(user_id, monster):
    battle().pve_battle(user_id, monster)
    return

    _hero = db.get_hero(user_id)
    _user_hp = _hero['hp']
    _equip = db.get_equip(user_id)
    _mob_hp = monsters[monster]['hp']
    _mob_damage = monsters[monster]['damage']

    text = adventure_header(user_id)

    text += 'Сражение с ' + monsters[monster]['name'] + '\n'

    while _mob_hp > 0 and _user_hp > 0:
        if len(text) > 2700 :
            break
        _temp_atk = int(get_atk(user_id))

        if _equip['gun']:
            if _equip['gun'][0].endswith('_axe') and random.random() > 0.75:
                _temp_atk += int(get_atk(user_id))
                if random.random() > 0.75:
                    _temp_atk += int(get_atk(user_id))

        _temp_atk = random.randint(round(_temp_atk) * 0,8, round(_temp_atk * 1,2))

        if _temp_atk < 1:
            _temp_atk += 2

        text += '\nТы нанес удар на ' + str(_temp_atk) + '💪\n'
        _mob_hp -= _temp_atk
        _wayyyyy = get_mob_atk(random.randint(*_mob_damage), get_def(user_id))
        if _mob_hp > 0 :
            text += monsters[monster]['name'] + ' нанес тебе ' + str(_wayyyyy) + '💥 урона'
            _user_hp -= _wayyyyy

    if _mob_hp <= 0 :
        text += '\n\nТы смог одолеть ' + monsters[monster]['name']
        if monsters[monster]['gold'] or monsters[monster]['diamond'] or monsters[monster]['loot']:
            text += '\nПолучено : ' + str(i_get_gold(user_id, wars = random.randint(*monsters[monster]['gold']))) + ' золота'

        if 'room' in monsters[monster]:
            send_message(user_id, text)
            eval(monsters[monster]['room'])(user_id)
            return

    elif _user_hp <= 0:
        text += '\n\n' + monsters[monster]['name'] + ' одолел тебя.\nТебе должно быть стыдно.'
        text += '\nПотеряно : ' + str(i_get_gold(user_id, wars = -random.randint(-1, _hero['gold']))) + ' золота'
    else :
        text += '\n\nВаша битва длилась слишком долго, вам пришлось её прервать.'

        if 'room' in monsters[monster]:
            send_message(user_id, text)
            eval(monsters[monster]['room'])(user_id)
            return

    send_message(user_id, text, get_start_button(user_id))