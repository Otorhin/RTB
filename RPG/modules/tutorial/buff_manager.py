def get_all_buff(user_id):
    _hero = db.get_hero(user_id)
    if _hero['buff']:
    	_buff = _hero['buff']
    	_buff = _buff.split('_')
    else:
    	_buff = []
    return (_buff)


def i_hero_buff(user_id):
    _hero = db.get_hero(user_id)
    text = ''

    if _hero['buff']:
        _buff = get_all_buff(user_id)
        text = '\n'
        for _name_buff in _buff:
            text += '\n🧪'
            try:
                text += names.buff[_name_buff]
            except:
                text += equip.potion[_name_buff][0]

    return (text)


def i_hero_add_buff(user_id, buff):
    _buff = get_all_buff(user_id)
    _buff.append(buff)
    _buff = '_'.join(_buff)
    db.change_buff(user_id, _buff)


def i_hero_del_buff(user_id, buff):
    _hero = db.get_hero(user_id)
    if _hero['buff']:
        _buff = _hero['buff']
        _buff = _buff.split('_')
        if buff in _buff:
            _buff.remove(buff)
            if len(_buff) != 0:
                _buff = '_'.join(_buff)
                db.change_buff(user_id, _buff)
            else:
                db.change_buff(user_id, None)
    else:
        pass