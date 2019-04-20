def check_upgrade_city(user_id):  # Проверить не достроилась, ли там стена?
    _hero = db.get_hero(user_id)
    _city = db.get_city(_hero['city'])
    if _city['upgrade'] >= _city['max_upgrade']:
        db.city_upgrade(_hero['city'])


def check_atk_city(cityy):  # Проверить не сломалась ли стена города который атаковали.
    _city = get_city(cityy)
    if _city['hp'] >= _city['max_hp']:
        db.set_hp_city(cityy, 0)


def war_win_atk(atk_id, def_id, ccity):  # Прогоняем с поста дефера, дефер может потерять опыт и шмот.
    _defer = db.get_hero(def_id)
    _hero = db.get_hero(atk_id)
    city[_defer['city']]['defenders'].remove(def_id)
    text_atk = 'При попытке нападения, тебя попытался задержал ' + _defer['nick'] + '\nНо, твое оружие смогло сломать его щит правосудия.'
    text_def = 'Охраняя стены родного города ты увидел ' + _hero['nick'] + '\nТы не смог его остановить. Его оружие смогло одолеть твой могучий щит правосудия.'
    _gold = 0
    if _defer['gold'] > 0 :
        _gold = random.randrange(0, round(_defer['gold'] / 2), 1)
    text_atk += '\nТы получил : \n' + str(_gold) + ' золота'
    text_def += '\nТы потерял : \n' + str(_gold) + ' золота'
    i_get_gold(atk_id, _gold)
    i_get_gold(def_id, -_gold)
    db.add_hp_city(ccity, -get_atk(atk_id))

    send_message(atk_id, text_atk, get_start_button(atk_id))
    send_message(def_id, text_def, get_start_button(def_id))


def war_win_def(atk_id, def_id):  # Расход по домам, но с опытом.
    _defer = db.get_hero(def_id)
    _hero = db.get_hero(atk_id)
    city[_defer['city']]['defenders'].remove(def_id)
    text_atk = 'При попытке нападения, тебя задержал ' + _defer['nick']
    text_def = 'Охраняя стены родного города ты увидел ' + _hero['nick']
    text_atk += '\nВы вместе выпили отборного эля и разошлись по домам.'
    text_def += '\nВы вместе выпили отборного эля и разошлись по домам.'

    send_message(atk_id, text_atk, get_start_button(atk_id))
    send_message(def_id, text_def, get_start_button(def_id))


def war_win_fish(atk_id, def_id):  # Дефер выебал атакера. Атакер может потерять опыт и шмот.
    _defer = db.get_hero(def_id)
    _hero = db.get_hero(atk_id)
    text_atk = 'При попытке нападения, тебя задержал ' + _defer['nick'] + '\nОдин лишь взгляд на него, заставил тебя плакать от бессилия.'
    text_def = 'Охраняя стены родного города ты увидел ' + _hero['nick'] + '\nЭто был странный малый. Увидев тебя, он рассплаклся и убежал.'
    _gold = 0
    if _defer['gold'] > 0:
        _gold = random.randrange(0, round(_hero['gold'] / 2), 1)
    text_def += '\nТы получил : \n' + str(_gold) + ' золота'
    text_atk += '\nТы потерял : \n' + str(_gold) + ' золота'
    i_get_gold(def_id, _gold)
    i_get_gold(atk_id, -_gold)

    send_message(atk_id, text_atk, get_start_button(atk_id))
    send_message(def_id, text_def, get_start_button(def_id))


def success_war(atk_id, ccity):  # Просто успешная атака без попадания на глаза деферу.
    db.add_hp_city(ccity, -get_atk(atk_id))
    text = 'Ты успешно атаковал вражеские стены.'
    send_message(atk_id, text, get_start_button(atk_id))