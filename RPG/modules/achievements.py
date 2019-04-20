def get_all_ach(user_id):
    _hero = db.get_hero(user_id)
    if _hero['ach']:
    	_ach = _hero['ach']
    	_ach = _ach.split('_')
    else:
    	_ach = []
    return (_ach)


def add_new_ach(user_id, name):
    if name in get_all_ach(user_id):
        return
    _ach = get_all_buff(user_id)
    _ach.append(name)
    _ach = '_'.join(_ach)
    db.change_ach(user_id, _ach)
    send_sticker(user_id, 'CAADAgADXgADP1c0GqcPuEWzcgFfAg')
    text = '🏆Новое достижение: {}'.format( names.ach_name[name] )
    send_message(user_id, text)


fast_command['/ach'] = 'bot_achiv'
def bot_achiv(user_id, message):
    _ach = get_all_ach(user_id)
    text = 'Твои достижения:\n'
    for ach in _ach:
        text += '{}\n'.format(names.ach_name[ach])
    send_message(user_id, text)