def game_crafting(user_id, message):
	_hero = db.get_hero(user_id)
	_inventory = db.get_inventory(user_id)
	#_prof = db.get_prof(user_id)
	_store = db.get_user_inventory(user_id)
	_data = message.replace('/', '').lower().split('_')
	if _data[0] == 'craft':
		if len(_inventory) > 29:
			text = '⁉️У тебя заполнен инвентарь'
			send_message(user_id, text)
		elif _data[1] in craft:
			_craft_item = craft[_data[1]]
			for _item in _craft_item['need']:
				if _store[_item[0]] >= _item[1]:
					pass
				else:
					text = '⁉️У тебя недостаточно ресурсов'
					text += '\n{}/{} {}'.format(_store[_item[0]], _item[1], names.item[_item[0]])
					send_message(user_id, text)
					return

			for _item in _craft_item['need']:
				db.add_inventory(user_id, _item[0], -_item[1])

			if _craft_item['type'] == 'item':
				db.add_inventory(user_id, _craft_item['result'], 1)
				_text = names.item[_craft_item['result']]
			else:
				_text = 'equip.' + _craft_item['type']
				_text = eval(_text)[_craft_item['result']][0]
				db.add_inventory_item(user_id, _craft_item['type'], _craft_item['result'])

			text = 'Ты сделал ' + _text
			text += '\nТы получил 1💡'
			i_get_exp(user_id, 1)
			send_message(user_id, text)

		elif False:
			if _store['stick2'] > 4 and _store['thread'] > 11:
				db.add_inventory(user_id, 'stick2', -5)
				db.add_inventory(user_id, 'thread', -12)
				db.add_inventory_item(user_id, 'gun', '0')
				text = '🔨Ты сделал ножку стола.'
			else:
				text = '⁉️У тебя недостаточно ресурсов'
		else:
			pass
	else:
		return
	


def craft_menu(user_id, message):
	_quest = db.get_quest(user_id)
	text = 'Доступные рецепты крафта:\n'
	if message == '⬅️ Назад':
		start_game(user_id)
		return
	elif message == '⚔️Оружие':
		text += '\nНожка стола /craft_2'
		text += '\n<code>Палки х5, Веревки х12</code>'
		if int(_quest['allquest']) > 18:
			text += '\nЖелезный меч /craft_7'
			text += '\n<code>Железо x 20, Уголь x 25, Инструменты кузнеца</code>'
	elif message == '🛡Шлемы':
		text += '\nКожанная обвязка /craft_8'
		text += '\n<code>Кожа x 5, Кость x 4</code>'
		if int(_quest['allquest']) > 18:
			text += '\nЖелезный шлем /craft_3'
			text += '\n<code>Железо x 15, Уголь x 20, Инструменты кузнеца</code>'
	elif message == '🛡Маски':
		text += '\nКожаная маска /craft_9'
		text += '\n<code>Кожа x 5, Кость x 4</code>'
		if int(_quest['allquest']) > 18:
			text += '\nЖелезная маска /craft_4'
			text += '\n<code>Железо x 10, Уголь x 15, Инструменты кузнеца</code>'
	elif message == '🛡Нагрудники':
		text += '\nФутболка из кожи /craft_10'
		text += '\n<code>Кожа x 15, Кость x 6, Ветка х6</code>'
		if int(_quest['allquest']) > 18:
			text += '\nЖелезный нагрудник /craft_5'
			text += '\n<code>Железо x 30, Уголь x 35, Инструменты кузнеца</code>'
	elif message == '🛡Ботинки':
		text += '\nКожаные ботинки /craft_11'
		text += '\n<code>Кожа x 13, Кость x 6, Ветка х6</code>'
		if int(_quest['allquest']) > 18:
			text += '\nПодкованные железом ботинки /craft_6'
			text += '\n<code>Железо x 20, Уголь x 22, Инструменты кузнеца</code>'
	elif message == '📿Прочее':
		text += '\nПалка /craft_1'
		text += '\n<code>Ветка х3</code>'
	else:
		return
	send_message(user_id, text, parse_mode = 'Html')



def game_craft(user_id):
	_hero = db.get_hero(user_id)
	_prof = db.get_prof(user_id)
	text = 'Выбери категорию'
	
	button = [
	['⚔️Оружие', '🛡Шлемы', '🛡Маски'],
	['🛡Нагрудники', '🛡Ботинки', '📿Прочее'],
	['⬅️ Назад']]	

	send_message(user_id, text, button, parse_mode='Html')
	set_hand(user_id, craft_menu)


craft = {
	'1' : {
		'type' : 'item',
		'result': 'stick2',
		'need' : [['stick' , 3]]
	}, '2' : {
		'type' : 'gun',
		'result' : '0',
		'need' : [['stick2', 5], ['thread', 12]]
	}, '3' : {
		'type' : 'head',
		'result' : '4',
		'need' : [['iron', 15], ['coal', 20], ['blacksmithtools', 1]]
	}, '4' : {
		'type' : 'mask',
		'result' : '4',
		'need' : [['iron', 10], ['coal', 15], ['blacksmithtools', 1]]
	}, '5' : {
		'type' : 'body',
		'result' : '4',
		'need' : [['iron', 30], ['coal', 35], ['blacksmithtools', 1]]
	}, '6' : {
		'type' : 'legs',
		'result' : '4',
		'need' : [['iron', 20], ['coal', 22], ['blacksmithtools', 1]]
	}, '7' : {
		'type' : 'gun',
		'result' : '6',
		'need' : [['iron', 20], ['coal', 25], ['blacksmithtools', 1]]
	}, '8' : {
		'type' : 'head',
		'result' : '1',
		'need' : [['leather', 5], ['bone', 4]]
	}, '9' : {
		'type' : 'mask',
		'result' : '1',
		'need' : [['leather', 5], ['bone', 4]]
	}, '10' : {
		'type' : 'body',
		'result' : '1',
		'need' : [['leather', 15], ['bone', 6], ['stick', 6]]
	}, '11' : {
		'type' : 'legs',
		'result' : '1',
		'need' : [['leather', 13], ['bone', 6], ['stick', 6]]
	}
}