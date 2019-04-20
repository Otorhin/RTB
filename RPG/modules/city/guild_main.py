def guild_info(user_id):
	_hero = db.get_hero(user_id)
	if _hero['guild_id'] :
		_quest = db.get_quest(user_id)
		if _quest['monster'] and _quest['monster'] == 'guild':
			db.change_quest(user_id,quest = _quest['quest'], monster = _quest['monster'], killed = int(_quest['killed']) + 1, need = _quest['need'], allquest = _quest['allquest'])
		_guild = db.get_guild(_hero['guild_id'])
		text = 'Название: [{tag}]{name}'
		text += '\nЛидер гильдии: {}'.format(db.get_hero(_guild['creator'])['nick'])
		text += '\n💰{gold}💎{diamond}'
		text += '\nЗдания гильдии /guild_build'
		text += '\nСделать пожертования своей гильдии /gdonate'
		if _guild['creator'] == user_id:
			text += '\n\nПароль гильдии: <code>{password}</code>'
			text += '\nCменить пароль /change_gpass'
		else:
			text += '\nПокинуть гильдию /gleave'
		text = text.format(**_guild)
		send_message(user_id, text, parse_mode = 'Html')
	else:
		text = 'Ты не состоишь в гильдии.\nЕсли знаешь пароль гильдии, введи его.\n\nТакже ты можешь создать гильдию.\nСтоимость 175💎'
		send_message(user_id, text, [['⬅️ Назад'], ['🕊Создать альянс']])
		set_hand(user_id, guild_handler)

fast_command['/gleave'] = 'inguild_handler'
fast_command['/gleave_yep'] = 'inguild_handler'
def inguild_handler(user_id, message):
	_hero = db.get_hero(user_id)
	if message == '/gleave':
		text = 'Подтверди выход из гильдии /gleave_yep'
		send_message(user_id, text)
	elif message == '/gleave_yep':
		_guild = db.get_guild(_hero['guild_id'])
		if _guild['creator'] == user_id:
			text = 'Ты не можешь покинуть гильдию, созданную тобой.'
		else:
			text = 'Ты покинул стены своей гильдии, и ведь даже слезы не пустил.'
			db.change_guild(user_id, None)
			send_message(_guild['creator'], '{} вышел из гильдии.'.format(_hero['nick']))
		send_message(user_id, text)
	else:
		pass

def guild_handler(user_id, message):
	if message == '⬅️ Назад':
		start_game(user_id)
		return
	_hero = db.get_hero(user_id)
	try:
		_guild_pass = db.get_guild_pass(message)
	except:
		_guild_pass = False
	if message == '🕊Создать альянс' and not _hero['guild_id']:
		if _hero['diamond'] < 175:
			text = 'Дядь, у тебя на бутылку пива не хватает, а ты про альянс заикнулся.'
		else:
			text = 'Введи тег и название гильдии в формате [tag]name\nТег - 2-3 символа, Название - 4-20 символов.\n\nПримеры:\n[BT]BlueTouch\n[HUB]PornHub\n[COC]ATb'
			temp[user_id] = {}
			set_hand(user_id, guild_create_handler)
		send_message(user_id, text)
	elif _guild_pass and not _hero['guild_id']:
		db1 = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password, db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
		with db1.cursor() as cursor:
			sql = "SELECT * FROM `user` WHERE `guild_id` = %s"
			cursor.execute(sql, (_guild_pass['id']))
			result = cursor.fetchall()
		if len(result) > 24:
			send_message(user_id, 'Гильдия заполнена людьми, поищи другую.')
			return
		_quest = db.get_quest(user_id)
		if _quest['monster'] and _quest['monster'] == 'guild':
			db.change_quest(user_id,quest = _quest['quest'], monster = _quest['monster'], killed = int(_quest['killed']) + 1, need = _quest['need'], allquest = _quest['allquest'])
		db.change_guild(user_id, _guild_pass['id'])
		text = 'Ты присоединился к {name}'.format(**_guild_pass)
		send_message(user_id, text)
		send_message(_guild_pass['creator'], '{} присоединился к Гильдии.'.format(_hero['nick']))
		start_game(user_id)
	else:
		pass

def guild_create_handler(user_id, message):
	_data = message.split(']')
	if message == '❌Отменить создание':
		start_game(user_id)
	if len(_data) == 2:
		if len(otrh_f.switch_chars(_data[0])) < 2 or len(otrh_f.switch_chars(_data[0])) > 3 or len(otrh_f.switch_chars(_data[1])) < 4 or len(otrh_f.switch_chars(_data[1])) > 20:
			text = 'Введи тег и название гильдии в формате [tag]name\nТег - 2-3 символа, Название - 4-20 символов.\n\nПримеры:\n[BT]BlueTouch\n[HUB]PornHub\n[COC]ATbBCEM'
			button = [['❌Отменить создание']]
			send_message(user_id, text, button)
			return
		else:
			temp[user_id] = {}
			temp[user_id]['tag'] = otrh_f.switch_chars(_data[0])
			temp[user_id]['name'] = otrh_f.switch_chars(_data[1])
			set_hand(user_id, guild_create_handler2)
			text = 'Твоя будущая гильдия [{tag}]{name}?'.format(**temp[user_id])
			button = [['Да'], ['Нет']]
			send_message(user_id, text, button)
	else:
		text = 'Введи тег и название гильдии в формате [tag]name\nТег - 2-3 символа, Название - 4-20 символов.\n\nПримеры:\n[BT]BlueTouch\n[HUB]PornHub\n[COC]ATbBCEM'
		button = [['❌Отменить создание']]
		send_message(user_id, text, button)


def guild_create_handler2(user_id, message):
	if message == 'Да':
		text = 'Поздравляю с созданием гильдии [{tag}]{name}'.format(**temp[user_id])
		_password = uuid4().hex
		db.create_guild(user_id, temp[user_id]['name'], temp[user_id]['tag'], _password)
		db.change_guild(user_id, db.get_guild_pass(_password)['id'])
		db.add_diamond(user_id, -175)
		send_message(user_id, text)
		start_game(user_id)
	elif message == 'Нет':
		text = 'Введи тег и название гильдии в формате [tag]name\nТег - 2-3 символа, Название - 4-20 символов.\n\nПримеры:\n[BT]BlueTouch\n[HUB]PornHub\n[COC]ATbBCEM'
		button = [['❌Отменить создание']]
		send_message(user_id, text, button)
		set_hand(user_id, guild_create_handler)
	else:
		pass


from uuid import uuid4
fast_command['/change_gpass'] = 'bot_change_guild_password'
def bot_change_guild_password(user_id, message):
	_hero = db.get_hero(user_id)
	if not _hero['guild_id'] or db.get_guild(_hero['guild_id'])['creator'] != user_id:
		return
	_guild = db.get_guild(_hero['guild_id'])
	if _guild['creator'] == user_id:
		_password = uuid4().hex
		db.change_gpass(_hero['guild_id'], _password)
		text = 'Новый пароль гильдии: {}'.format(_password)
		bot.send_message(user_id, text)
	else:
		return


fast_command['/gdonate'] = 'bot_gdonate'
def bot_gdonate(user_id, message):
	_hero = db.get_hero(user_id)
	if not _hero['guild_id']:
		return
	text = 'Отдать гильдии все свое золото /gdonate_gold'
	text += '\nОтдать гильдии все свои алмазы /gdonate_diamond'
	send_message(user_id, text)


fast_command['/gdonate_gold'] = 'bbgdonate_gold'
def bbgdonate_gold(user_id, message):
	_hero = db.get_hero(user_id)
	if not _hero['guild_id'] or _hero['gold'] < 1:
		return
	_text = message.split(' ')
	_guild = db.get_guild(_hero['guild_id'])
	try:
		_money = int(_text[1])
		if _hero['gold'] >= _money and _money > 0:
			text = 'Ты успешно отдал своей гильдии {}💰'.format(_money)
			send_message(_guild['creator'], '{} отдал гильдии {}💰.'.format(_hero['nick'] , _money))
			db.add_guild_money(user_id, _hero['guild_id'], 'gold', _money)
		else:
			text = 'У тебя нет столько денег.'
		send_message(user_id, text)
		return
	except:
		pass
	db.add_guild_money(user_id, _hero['guild_id'], 'gold')
	send_message(_guild['creator'], '{} отдал гильдии {}💰.'.format(_hero['nick'] , _hero['gold']))
	text = 'Ты успешно отдал своей гильдии {gold}💰'.format(**_hero)
	send_message(user_id, text)


fast_command['/gdonate_diamond'] = 'bbgdonate_diamond'
def bbgdonate_diamond(user_id, message):
	_hero = db.get_hero(user_id)
	if not _hero['guild_id'] or _hero['diamond'] < 1:
		return
	_text = message.split(' ')
	_guild = db.get_guild(_hero['guild_id'])
	try:
		_money = int(_text[1])
		if _hero['diamond'] >= _money and _money > 0:
			text = 'Ты успешно отдал своей гильдии {}💎'.format(_money)
			send_message(_guild['creator'], '{} отдал гильдии {}💎.'.format(_hero['nick'] , _money))
			db.add_guild_money(user_id, _hero['guild_id'], 'diamond', _money)
		else:
			text = 'У тебя нет столько денег.'
		send_message(user_id, text)
		return
	except:
		pass
	db.add_guild_money(user_id, _hero['guild_id'], 'diamond')
	send_message(_guild['creator'], '{} отдал гильдии {}💎.'.format(_hero['nick'] , _hero['diamond']))
	text = 'Ты успешно отдал своей гильдии {diamond}💎'.format(**_hero)
	send_message(user_id, text)


fast_command['/guild_build'] = 'bot_guild_build'
def bot_guild_build(user_id, message):
	_hero = db.get_hero(user_id)
	if not _hero['guild_id']:
		return
	_guild = db.get_guild(_hero['guild_id'])

	text = 'Здания гильдии {name}:\n'
	text += '\n🏛Ратуша - {build1} уровень'
	if _guild['creator'] == user_id and _guild['build1'] < 25:
		_cost_upgrade = [  (_guild['build1'] + 1) * 750,  (_guild['build1'] + 1) * 20]
		text += '\nСтоимость улучшения - {}💰{}💎'.format( *_cost_upgrade )
		if _guild['gold'] >= _cost_upgrade[0] and _guild['diamond'] >= _cost_upgrade[1]:
			text += '\nУлучшить /guild_upgrade_build1'

	text += '\n🛡Оружейная - {build2} уровень'
	if _guild['creator'] == user_id and _guild['build2'] < 25 and _guild['build1'] > 2:
		_cost_upgrade = [  (_guild['build2'] + 1) * 2500,  (_guild['build2'] + 1) * 50]
		text += '\nСтоимость улучшения - {}💰{}💎'.format( *_cost_upgrade )
		if _guild['gold'] >= _cost_upgrade[0] and _guild['diamond'] >= _cost_upgrade[1]:
			text += '\nУлучшить /guild_upgrade_build2'

	text += '\n🔍Бюро находок - {build3} уровень'
	if _guild['creator'] == user_id and _guild['build3'] < 15 and _guild['build1'] > 5:
		_cost_upgrade = [  (_guild['build3'] + 1) * 2500,  (_guild['build3'] + 1) * 50]
		text += '\nСтоимость улучшения - {}💰{}💎'.format( *_cost_upgrade )
		if _guild['gold'] >= _cost_upgrade[0] and _guild['diamond'] >= _cost_upgrade[1]:
			text += '\nУлучшить /guild_upgrade_build3'
		
	text = text.format(**_guild)
	send_message(user_id, text)



fast_command['/guild_upgrade_build1'] = 'bot_guild_upgrade_build1'
def bot_guild_upgrade_build1(user_id, message):
	_hero = db.get_hero(user_id)
	if not _hero['guild_id'] or db.get_guild(_hero['guild_id'])['creator'] != user_id:
		return
	_guild = db.get_guild(_hero['guild_id'])
	_cost_upgrade = [  (_guild['build1'] + 1) * 750,  (_guild['build1'] + 1) * 20]
	if _guild['creator'] == user_id and (_guild['gold'] >= _cost_upgrade[0] and _guild['diamond'] >= _cost_upgrade[1] and _guild['build1'] < 25):
		db.guild_upgrade_build1(_hero['guild_id'])
		text = 'Здание успешно улучшено.'
		send_message(user_id, text)
	else:
		return


fast_command['/guild_upgrade_build2'] = 'bot_guild_upgrade_build2'
def bot_guild_upgrade_build2(user_id, message):
	_hero = db.get_hero(user_id)
	if not _hero['guild_id'] or db.get_guild(_hero['guild_id'])['creator'] != user_id:
		return
	_guild = db.get_guild(_hero['guild_id'])
	_cost_upgrade = [  (_guild['build2'] + 1) * 2500,  (_guild['build2'] + 1) * 50]
	if _guild['creator'] == user_id and (_guild['gold'] >= _cost_upgrade[0] and _guild['diamond'] >= _cost_upgrade[1] and _guild['build2'] < 25 and _guild['build1'] > 2):
		db.guild_upgrade_build2(_hero['guild_id'])
		text = 'Здание успешно улучшено.'
		send_message(user_id, text)
	else:
		return


fast_command['/guild_upgrade_build3'] = 'bot_guild_upgrade_build3'
def bot_guild_upgrade_build3(user_id, message):
	_hero = db.get_hero(user_id)
	if not _hero['guild_id'] or db.get_guild(_hero['guild_id'])['creator'] != user_id:
		return
	_guild = db.get_guild(_hero['guild_id'])
	_cost_upgrade = [  (_guild['build3'] + 1) * 2500,  (_guild['build3'] + 1) * 50]
	if _guild['creator'] == user_id and (_guild['gold'] >= _cost_upgrade[0] and _guild['diamond'] >= _cost_upgrade[1] and _guild['build3'] < 15 and _guild['build1'] > 5):
		db.guild_upgrade_build3(_hero['guild_id'])
		text = 'Здание успешно улучшено.'
		send_message(user_id, text)
	else:
		return


fast_command['/gpeople'] = 'bot_gpeople'
def bot_gpeople(user_id, message):
    _hero = db.get_hero(user_id)
    if not _hero['guild_id']:
        return
    db1 = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    i = 1

    _guild = db.get_guild(_hero['guild_id'])
    text = 'Состав гильдии [{tag}]{name}\n'.format( **_guild )
    with db1.cursor() as cursor:
        sql = "SELECT * FROM `user` WHERE `guild_id` = {}".format( _hero['guild_id'] )
        cursor.execute(sql)
        result = cursor.fetchall()
    for alluser in result:
        text += '\n<b>{nick}</b>\n<code>{exp}💡 {lvl}🀄</code>'
        if user_id == _guild['creator']:
        	text += '\n<code>{gold}💰 {diamond}💎 {rating}🏆</code>'
        text = text.format(**alluser)
        i += 1
    db1.close()

    send_message(user_id, text, parse_mode = 'Html')


fast_command['/ggive_gold'] = 'bbgive_gold'
def bbgive_gold(user_id, message):
	_hero = db.get_hero(user_id)
	if not _hero['guild_id'] or db.get_guild(_hero['guild_id'])['creator'] != user_id:
		return
	_text = message.split(' ')
	_guild = db.get_guild(_hero['guild_id'])
	try:
		_money = int(_text[2])
		_user_id = int(_text[1])
		if db.get_hero(_user_id)['guild_id'] != _hero['guild_id']:
			text = 'Игрок не в вашей гильдии. Ты чего?'
			send_message(user_id,text)
		elif _guild['gold'] >= _money and _money > 0:
			text_creator = '{} получил {}💰'.format(db.get_hero(_user_id)['nick'], _money)
			text_user = 'Руководство гильдии выдало тебе {}💰'.format(_money)
			send_message(user_id, text_creator)
			send_message(_user_id, text_user)
			db._23_add_guild_money(_user_id, _hero['guild_id'], 'gold', _money)
		else:
			text = 'У вашей гильдии нет столько денег.'
			send_message(user_id, text)
	except Exception as e:
		print(e)
		pass


fast_command['/ggive_diamond'] = 'bbgive_diamond'
def bbgive_diamond(user_id, message):
	_hero = db.get_hero(user_id)
	if not _hero['guild_id'] or db.get_guild(_hero['guild_id'])['creator'] != user_id:
		return
	_text = message.split(' ')
	_guild = db.get_guild(_hero['guild_id'])
	try:
		_money = int(_text[2])
		_user_id = int(_text[1])
		if db.get_hero(_user_id)['guild_id'] != _hero['guild_id']:
			text = 'Игрок не в вашей гильдии. Ты чего?'
			send_message(user_id,text)
		elif _guild['diamond'] >= _money and _money > 0:
			text_creator = '{} получил {}💎'.format(db.get_hero(_user_id)['nick'], _money)
			text_user = 'Руководство гильдии выдало тебе {}💎'.format(_money)
			send_message(user_id, text_creator)
			send_message(_user_id, text_user)
			db._23_add_guild_money(_user_id, _hero['guild_id'], 'diamond', _money)
		else:
			text = 'У вашей гильдии нет столько денег.'
			send_message(user_id, text)
	except:
		pass