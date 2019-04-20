def get_mob_atk(atk_mob, def_user):
    return (ceil(atk_mob * 19 / (def_user + 19) + 0.05))


def monster_battle(user_id, monster):

    _hero = db.get_hero(user_id)
    _user_hp = _hero['hp']
    _skill = db.get_skill(user_id)
    _equip = db.get_equip(user_id)
    _user_atk = get_atk(user_id)
    _user_def = get_def(user_id)

    if monsters[monster]['level'] == 'easy':
        _mob_hp = random.randint(round(_user_hp * 0.6), round(_user_hp * 1.15))
        _mob_damage = [round(_user_atk * 0.8), round(_user_atk * 1.15)]
    elif monsters[monster]['level'] == 'medium':
        _mob_hp = random.randint(round(_user_hp * 0.6), round(_user_hp * 1.4))
        _mob_damage = [round(_user_atk * 0.8), round(_user_atk * 1.4)]
    else:
        _mob_hp = random.randint(round(_user_hp * 0.6), round(_user_hp * 1.7))
        _mob_damage = [round(_user_atk * 0.8), round(_user_atk * 1.7)]


    _bleed = False

    text = 'Сражение с ' + monsters[monster]['name'] + '\n'

    while _mob_hp > 0 and _user_hp > 0:
        if len(text) > 2700 :
            break
        _crit = False
        _vamp = False
        _temp_atk = int(_user_atk)
        _ttemp_atk = _temp_atk
        _temp_atk = random.randint(round(_temp_atk * 0.8), round(_temp_atk * 1.2))

        if _bleed:
            _bleed_result = random.randint(round(_temp_atk * 0.3), round(_temp_atk * 0.5))
            text += '\n{} истек кровью на {}❤️'.format(monsters[monster]['name'], _bleed_result)
            _mob_hp -= _bleed_result

        if random.random() < 0.025:
            text += '\nТы промахнулся по монстру\n'
        else:
            if int(_skill['crit']) > 0 and random.random() > ( 1 - ( int(_skill['crit']) * 0.005 ) ) and not _bleed and not _vamp:
                _temp_atk += random.randint(round(_ttemp_atk * 0.8), round(_ttemp_atk * 1.2))
                _crit = True
                text += '\n💫Ты нанес удар на ' + str(_temp_atk) + '💪\n'
            else:
                text += '\nТы нанес удар на ' + str(_temp_atk) + '💪\n'
            _mob_hp -= _temp_atk
            if int(_skill['vamp']) > 0 and random.random() > ( 1 - ( int(_skill['vamp']) * 0.005 ) ) and not _bleed and not _crit:
                _vamp_result = random.randint(1, _temp_atk)
                _vamp = True
                text += 'Также ты восстановил себе {}🖤\n'.format( _vamp_result )
                _user_hp += _vamp_result

            if int(_skill['bleed']) > 0 and random.random() > ( 1 - ( int(_skill['bleed']) * 0.005 ) ) and not _crit and not _vamp:
                _bleed = True
        #_wayyyyy = get_mob_atk(random.randint(*_mob_damage), _user_def)
        _wayyyyy = random.randint(*_mob_damage)
        if _mob_hp > 0 :
            if random.random() < 0.05:
                text += monsters[monster]['name'] + ' промахнулся по тебе.'
            else:
                text += monsters[monster]['name'] + ' нанес тебе ' + str(_wayyyyy) + '💥 урона'
                _user_hp -= _wayyyyy

    if _mob_hp <= 0 :
        text += '\n\nТы смог одолеть ' + monsters[monster]['name']

        _quest = db.get_quest(user_id)
        if _quest['monster']:
            if _quest['monster'] not in ['forest', 'mount', 'desert', 'tavern', 'guild'] and monsters[_quest['monster']]['name'] == monsters[monster]['name']:
                db.change_quest(user_id,quest = _quest['quest'], monster = _quest['monster'], killed = int(_quest['killed']) + 1, need = _quest['need'], allquest = _quest['allquest'])

        if monsters[monster]['gold'] and int(_user_hp) < int(_hero['hp']) * 0.6:
            _gggggold = i_get_gold(user_id, wars=random.randint(*monsters[monster]['gold']))
            text += '\nПолучено : ' + str(_gggggold) + ' золота'
            temp[user_id]['gold'] += _gggggold
        elif monsters[monster]['gold']:
            _gggggold = i_get_gold(user_id, wars=ceil(random.randint(*monsters[monster]['gold']) * 0.4))
            text += '\nПолучено : ' + str(_gggggold) + ' золота'
            temp[user_id]['gold'] += _gggggold
            
        if monsters[monster]['diamond'] and random.random() < 0.1:
            text += '\nПолучено : ' + str(i_get_diamond(user_id, wars=random.randint(*monsters[monster]['diamond']))) + ' алмазов'
        if monsters[monster]['loot']:
            _res = random.choice(monsters[monster]['loot'])
            _inventory = db.get_inventory(user_id)
            if _res[0] == 'resource':
                _number = random.randint(*_res[2])
                db.add_inventory(user_id, _res[1], _number)
                text += '\nПолучено: ' + names.item[_res[1]] + ' x' + str(_number)

            elif _res[0] in ['head', 'mask', 'body', 'gun', 'legs'] and len(_inventory) < 30 and random.random() < 0.3:
                text += '\nПолучено: ' + eval('equip.' + _res[0])[_res[1]][0]
                db.add_inventory_item(user_id, _res[0], _res[1])

        if int(_user_hp) < int(_hero['hp']) * 0.4:
            #text += '\nТы получил 1💡'
            db.add_rating(user_id, 1)
            #i_get_exp(user_id, 1)

        db.add_rating(user_id, 1)
        text = adventure.header(user_id) + text
        send_message(user_id, text)

        if 'room' in monsters[monster]:
            eval(monsters[monster]['room'])(user_id)
            return

    elif _user_hp <= 0:
        send_sticker(user_id, 'CAADAgADXQADP1c0GhOSdTV19-FaAg')
        text += '\n\n' + monsters[monster]['name'] + ' одолел тебя.\nТебе должно быть стыдно.'
        _minigold_azaza = random.randint(1, round(_hero['gold'] * 0.3) + 2)
        if _hero['gold'] >= _minigold_azaza:
            i_get_gold(user_id, wars = -_minigold_azaza)
            temp[user_id]['gold'] -= _minigold_azaza
            text += '\nПотеряно : ' + str(_minigold_azaza) + ' золота'
        temp[user_id]['count_item'] = 0
        db.add_rating(user_id, -1)
        text = adventure.header(user_id) + text
        send_message(user_id, text)
    else :
        text += '\n\nВаша битва длилась слишком долго, вам пришлось её прервать.'
        text = adventure.header(user_id) + text
        send_message(user_id, text)


def boss_battle(users_id):

    _atk = 0
    _def = 0
    _hp = 0
    _guild_tag = None
    _guild_text = 'Воины которые учавствовали в сражении: '

    for _user in users_id:
        _hero = db.get_hero(_user)
        _hp += _hero['hp']
        _def += get_def(_user)
        _atk += get_atk(_user)
        if not _guild_tag:
            _guild_tag = db.get_guild(_hero['guild_id'])['tag']
        _guild_text += '{}; '.format(_hero['nick'])

    _mob_hp = random.randint(round(_hp * 0.6), round(_hp * 1.7))
    _mob_damage = random.randint(round(_atk * 0.8), round(_atk * 1.7))

    _mob_get_damage = 0
    _guild_get_damage = 0

    while _mob_hp > 0 and _hp > 0:
        _temp_atk = random.randint(round(_atk * 0.8), round(_atk * 1.2))
        _mob_hp -= _temp_atk
        _mob_get_damage += _temp_atk
        _wayyyyy = random.randint(round(_mob_damage * 0.9), round(_mob_damage * 1.2))
        _hp -= _wayyyyy
        _guild_get_damage += _wayyyyy


    if _mob_hp <= 0 :

        text = '{} был(а) повержена славными воинами гильдии [{}]\n\n'.format('😈Ведьма', _guild_tag)
        text += _guild_text

        text += '\n\nВаша гильдия нанесла {} урона.'.format(_mob_get_damage)
        text += '\nВаша гильдия получила {} урона.'.format(_guild_get_damage)

        for _user in users_id:
            _user_text = '\n\nТы получил: '
            _getted_exp = random.randint(5,15)
            _user_text += '{}💡 '.format(_getted_exp)
            i_get_exp(_user, _getted_exp)

            _gggggold = random.randint(150,400)
            _user_text += '{}💰 '.format(_gggggold)
            i_get_gold(_user, wars=_gggggold)

            _diamond = random.randint(3,10)
            _user_text += '{}💎 '.format(_diamond)
            i_get_diamond(_user, wars=_diamond)

            _user_text += '20🏆 '
            db.add_rating(_user, 20)

            send_message(_user, text + _user_text)


    else:

        text = 'Воины гильдии [{}] были повержены под напором {}\n\n'.format(_guild_tag, '😈Ведьма')
        text += _guild_text

        text += '\n\nВаша гильдия нанесла {} урона.'.format(_mob_get_damage)
        text += '\nВаша гильдия получила {} урона.'.format(_guild_get_damage)


        for _user in users_id:
            _hero = db.get_hero(_user)
            _user_text = '\n\nТы потерял: '
            if _hero['exp'] > 8:
                _getted_exp = random.randint(5,8)
                _user_text += '{}💡 '.format(_getted_exp)
                i_get_exp(_user, -_getted_exp)

            _gggggold = random.randint(1, round(_hero['gold'] * 0.3) + 2)
            if _hero['gold'] >= _gggggold:
                _user_text += '{}💰 '.format(_gggggold)
                i_get_gold(_user, wars = -_gggggold)

            _user_text += '20🏆 '
            db.add_rating(_user, -20)

            send_sticker(_user, 'CAADAgADXQADP1c0GhOSdTV19-FaAg')
            send_message(_user, text + _user_text)


def pvp_battle(user_atk, user_def):

    _user1_info = db.get_hero(user_atk)
    _user2_info = db.get_hero(user_def)

    _user1 = {'hp': _user1_info['hp'], 'atk': get_atk(user_atk), 'def': get_def(user_atk)}
    _user2 = {'hp': _user2_info['hp'], 'atk': get_atk(user_def), 'def': get_def(user_def)}


    text = '{} vs {}'.format(_user1_info['nick'], _user2_info['nick'])


    _user1_get_damage = 0
    _user2_get_damage = 0

    while _user1['hp'] > 0 and _user2['hp'] > 0:
        _temp_atk = random.randint(round(_user1['atk'] * 0.8), round(_user1['atk'] * 1.2))
        _user2['hp'] -= get_mob_atk(_temp_atk, _user1['def'])
        _user2_get_damage += _temp_atk

        _wayyyyy = random.randint(round(_user2['atk'] * 0.8), round(_user2['atk'] * 1.2))
        _user1['hp'] -= get_mob_atk(_wayyyyy, _user1['def'])
        _user1_get_damage += _wayyyyy


    text += '\n\n{} получил {} урона.'.format(_user1_info['nick'], _user1_get_damage)
    text += '\n{} получил {} урона.'.format(_user2_info['nick'], _user2_get_damage)

    if _user1['hp'] <= 0 :


        text += '\n\nВыиграл {}'.format(_user2_info['nick'])
        send_sticker(user_atk, 'CAADAgADXQADP1c0GhOSdTV19-FaAg')
        send_message(user_atk, text)
        send_message(user_def, text)


    else:

        text += '\n\nВыиграл {}'.format(_user1_info['nick'])
        send_sticker(user_def, 'CAADAgADXQADP1c0GhOSdTV19-FaAg')
        send_message(user_atk, text)
        send_message(user_def, text)

