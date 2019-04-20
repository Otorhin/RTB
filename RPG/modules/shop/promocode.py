def use_promocode(user_id, code):
    _promocode = db.get_promocode(code)
    if not _promocode:
        return

    text = 'Вы получили : '

    if _promocode[0] == 'diamond':
        db.add_diamond(user_id, int(_promocode[1]))
        text += '\n' + str(_promocode[1]) + ' алмазов'
    elif _promocode[0] == 'gold':
        db.add_gold(user_id, int(_promocode[1]))
        text += '\n' + str(_promocode[1]) + ' золота'
    elif _promocode[0] in ['head', 'body', 'legs', 'mask', 'gun']:
        db.add_inventory_item(user_id, _promocode[0], _promocode[1])
        _name_equip = eval('equip.' + _promocode[0])[_promocode[1]][0]
        text += '\n' + _name_equip
    else :
        pass

    db.del_promocode(code)
    send_message(user_id, text)


def use_refcode(user_id, ref_id):
    try :
        text = 'Вы ввели пригласительный промокод ' + db.get_hero(ref_id)['nick']
        text += '\nВам выдан пригласительный бонус : '
        text += '\n50 золота и 5 алмазов'
    
        ref_text = db.get_hero(user_id)['nick'] + ' ввел ваш промокод.'
        ref_text += '\nВам выдан бонус : '
        ref_text += '\n100 золота и 15 алмазов'
    
        send_message(ref_id, ref_text)

    except:
        return


    send_message(user_id, text)
    db.add_diamond(ref_id, 15)  
    db.add_diamond(user_id, 5)

    db.add_gold(ref_id, 100)
    db.add_gold(user_id, 50) 

    db.change_ref(user_id, ref_id)


def use_update_code(user_id, code):
    _promocode = db.get_promocode(code)
    if not _promocode:
        return

    if user_id in temp :
        if 'update' in temp[user_id]:
            return

    text = 'Вы получили : '

    if _promocode[0] == 'diamond':
        db.add_diamond(user_id, int(_promocode[1]))
        text += '\n' + str(_promocode[1]) + ' алмазов'
    elif _promocode[0] == 'gold':
        db.add_gold(user_id, int(_promocode[1]))
        text += '\n' + str(_promocode[1]) + ' золота'
    elif _promocode[0] in ['head', 'body', 'legs', 'mask', 'gun']:
        db.add_inventory_item(user_id, _promocode[0], _promocode[1])
        _name_equip = eval('equip.' + _promocode[0])[_promocode[1]][0]
        text += '\n' + _name_equip
    else :
        pass

    db.del_promocode(code)
    send_message(user_id, text, get_start_button(user_id))
    if user_id in temp:
        temp[user_id]['update'] = 'Bla-Bla'
    else:
        temp[user_id] = {'update':'Bla-Bla'}