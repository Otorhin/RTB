def game_alchemy1(user_id, message):
	if message == '⬅️ Назад':
		start_game(user_id)
		return
	_hero = db.get_hero(user_id)
	#_prof = db.get_prof(user_id)
	_inventory = db.get_inventory(user_id)
	_store = db.get_user_inventory(user_id)
	_data = message.replace('/', '').lower().split('_')
	if _data[0] == 'cook':
		if len(_inventory) > 29:
			text = '⁉️У тебя заполнен инвентарь'
		elif _data[1] in alchemy:
			_craft_item = alchemy[_data[1]]
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

			_text = equip.potion[_craft_item['result']][0]
			db.add_inventory_item(user_id, 'potion', _craft_item['result'])

			text = 'Ты сварил ' + _text
			text += '\nТы получил 1💡'
			i_get_exp(user_id, 1)
			send_message(user_id, text)
		else:
			pass
	else:
		return


def game_alchemy(user_id):
	_hero = db.get_hero(user_id)
	_prof = db.get_prof(user_id)
	text = 'Доступные рецепты крафта:\n'
	text += '\nБодрящий напиток /cook_1'
	text += '\n<code>Волчьи ягоды х5, Ягоды голубики х5, Старые желуди х7</code>'
	text += '\nСлабое зелье Берсерка /cook_2'
	text += '\n<code>Волчьи ягоды х5, Ягоды голубики х5, Галюциногенных грибы х7</code>'
	text += '\nКостерост /cook_3'
	text += '\n<code>Железо х3, Рубин </code>'
	text += '\nЗелье Вампира /cook_4'
	text += '\n<code>Снежноцвет, Голубика, Кость х20, Рубин</code>'
	send_message(user_id, text, parse_mode='Html')


alchemy = {
	'1' : {
		'result': '1',
		'need' : [['wolfberri', 5], ['blueberri', 5], ['oldacorn', 7]]
	}, '2' : {
		'result' : '2',
		'need' : [['wolfberri', 5], ['blueberri', 5], ['hallucberri', 7]]
	}, '3' : {
		'result' : '3',
		'need' : [['iron', 3], ['ruby', 1]]
	}, '4' : {
		'result' : '4',
		'need' : [['ruby', 1], ['bone', 20], ['blueberri', 1], ['snowflower', 1]]
	}
}