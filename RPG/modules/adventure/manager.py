def i_get_gold(user_id, wars = None, exp = 1):
    _hero = db.get_hero(user_id)
    _skill = db.get_skill(user_id)
    gold = random.randint(3, 9)
    gold = round(gold)
    gold += gold * _skill['gold'] * 0.5
    if _hero['guild_id']:
        _guild = db.get_guild(_hero['guild_id'])
        gold += gold * int(_guild['build1']) * 0.1
    gold = gold * exp

    _equip = db.get_equip(user_id)
    if _equip['amulet']:
        if _equip['amulet'][0] == 'insight':
            gold += round(gold * 0.05)

    if wars:
        gold = wars
    gold = round(gold)
    db.add_gold(user_id, gold)
    return (round(gold))


def i_get_diamond(user_id, wars = None, exp = 1):
    diamond = random.randint(1,4)
    diamond = diamond * exp
    if wars:
        diamond = wars
    db.add_diamond(user_id, diamond)
    return (diamond)


def i_get_exp(user_id,wars = None):
    _hero = db.get_hero(user_id)
    exp = 2
    exp += int(_hero['lvl']) * 0.7
    exp = round(exp) 
    if wars:
        exp = wars
    db.add_exp(user_id, exp)
    _hero = db.get_hero(user_id)
    if int(_hero['exp']) >= (int(_hero['new_exp'])) :
        db.add_atk(user_id, 1)
        db.add_def(user_id, 1)
        db.new_lvl(user_id, otrh_f.get_new_exp(_hero['lvl']))
        send_sticker(user_id, 'CAADAgADWwADP1c0GptE9B5Q1MCNAg')
        send_message(user_id, '🀄️Новый уровень.\nТы получил 300💰 и 10💎')
        if _hero['referal'] and _hero['lvl'] == 1:
            reftext = '{} достиг 2ого уровня. За это ты получаешь 10💰'.format( _hero['nick'] )
            i_get_gold(_hero['referal'], 10)
            send_message(_hero['referal'], reftext)
    return (exp)


def i_get_inventory(user_id):
    item = random.choice(['coal', 'stick', 'iron', 'stone'])
    number = random.randint(1,3)
    db.add_inventory(user_id, item, number)
    text = names.item[item] + ' x' + str(number)
    return (text)

def get_atk(user_id):
    _hero = db.get_hero(user_id)
    _equip = db.get_equip(user_id)
    atk = _hero['atk']
    if _equip['head']:
        item = _equip['head']
        atk += equip.head[item[0]][2]
    if _equip['mask']:
        item = _equip['mask']
        atk += equip.mask[item[0]][2] 
    if _equip['body']:
        item = _equip['body']
        atk += equip.body[item[0]][2] 
    if _equip['legs']:
        item = _equip['legs']
        atk += equip.legs[item[0]][2]
    if _equip['gun']:
        item = _equip['gun']
        atk += equip.gun[item[0]][2]
    if _equip['shand']:
        item = _equip['shand']
        atk += equip.shand[item[0]][2]
    if _hero['guild_id']:
        _guild = db.get_guild(_hero['guild_id'])
        atk += int(_guild['build2'])
    return (round(atk))

def get_def(user_id):
    _hero = db.get_hero(user_id)
    _equip = db.get_equip(user_id)
    defe = _hero['def']
    if _equip['head']:
        item = _equip['head']
        defe += equip.head[item[0]][1]
    if _equip['mask']:
        item = _equip['mask']
        defe += equip.mask[item[0]][1] 
    if _equip['body']:
        item = _equip['body']
        defe += equip.body[item[0]][1] 
    if _equip['legs']:
        item = _equip['legs']
        defe += equip.legs[item[0]][1]
    if _equip['gun']:
        item = _equip['gun']
        defe += equip.gun[item[0]][1]
    if _equip['shand']:
        item = _equip['shand']
        defe += equip.shand[item[0]][1]
    if _hero['guild_id']:
        _guild = db.get_guild(_hero['guild_id'])
        defe += int(_guild['build2'])
    return defe