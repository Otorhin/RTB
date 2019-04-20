def bot_hero_skill(user_id):
    _hero = db.get_hero(user_id)
    if _hero['atk'] < 0 or _hero['def'] < 0:
        text = 'Приходи как отрезвеешь'
        send_message(user_id, text)
        return

    button = []
    _skill = db.get_skill(user_id)
    text = 'Твои скиллы:'
    text += '\n👝Сумочка [{}/15 уровень]'.format(_skill['bag'])
    if _skill['bag'] < 15:
        text += '\nСтоимость улучшения {}💎'.format( ((int(_skill['bag']) - 4) * 5) )
        if _hero['diamond'] >= ((int(_skill['bag']) - 4) * 5):
            button.append(['👝Сумочка'])
    text += '\n💰Утка [{}/10 уровень]'.format(_skill['gold'])
    if _skill['gold'] < 10:
        text += '\nСтоимость улучшения {}💎'.format( ((int(_skill['gold']) + 1) * 7) )
        if _hero['diamond'] >= ((int(_skill['gold']) + 1) * 7):
            button.append(['💰Утка'])

    text += '\n\nТвои характеристики:'
    text += '\n💪Сила кулаков [{}/50]'.format(_hero['atk'])
    if _hero['atk'] < 50:
        text += '\nСтоимость улучшения {}💰'.format( ((int(_hero['atk']) - 4) * 25) )
        if _hero['gold'] > ((int(_hero['atk']) - 4) * 25):
            button.append(['💪Атака'])
    text += '\n🛡Толщина спины [{}/75]'.format(_hero['def'])
    if _hero['def'] < 75:
        text += '\nСтоимость улучшения {}💰'.format( ((int(_hero['def']) - 4) * 20) )
        if _hero['gold'] > ((int(_hero['def']) - 4) * 20):
            button.append(['🛡Защита'])
    text += '\n❤️Заморозка сердца [{}/250]'.format(_hero['hp'])
    if _hero['hp'] < 250:
        text += '\nСтоимость улучшения {}💰'.format( (int(_hero['hp']) - 90) * 25)
        if _hero['gold'] > ((int(_hero['hp']) - 90) * 25) and _hero['hp'] < 250:
            button.append(['❤Здоровье'])

    _quest = db.get_quest(user_id)
    if int(_quest['allquest']) > 10:
        text += '\n\nТвои боевые умения:'
        text += '\n💫Усиленный удар [{}/20]'.format(_skill['crit'])
        if _skill['crit'] < 20:
            text += '\nСтоимость улучшения {}💎'.format( ((int(_skill['crit']) + 1) * 8) )
            if _hero['diamond'] >= ((int(_skill['crit']) + 1) * 8):
                button.append(['💫Усиленный удар'])
        text += '\n💔Ловкий удар [{}/20]'.format(_skill['bleed'])
        if _skill['bleed'] < 20:
            text += '\nСтоимость улучшения {}💎'.format( ((int(_skill['bleed']) + 1) * 8) )
            if _hero['diamond'] >= ((int(_skill['bleed']) + 1) * 8):
                button.append(['💔Ловкий удар'])
        text += '\n🖤Подозрительный удар [{}/20]'.format(_skill['vamp'])
        if _skill['vamp'] < 20:
            text += '\nСтоимость улучшения {}💎'.format( ((int(_skill['vamp']) + 1) * 8) )
            if _hero['diamond'] >= ((int(_skill['vamp']) + 1) * 8):
                button.append(['🖤Подозрительный удар'])


    button.append(['⬅️Вернуться'])
    send_message(user_id, text, button)
    set_hand(user_id, upgrade_hero)


def upgrade_hero(user_id, message):
    _hero = db.get_hero(user_id)
    _skill = db.get_skill(user_id)

    if message == '💪Атака' and (_hero['gold'] >= ((int(_hero['atk']) - 4) * 25) and _hero['atk'] < 50):
        db.add_gold(user_id, -((int(_hero['atk']) - 4) * 25))
        db.add_atk(user_id, 1)
        text = '💪Тяжелые тренировки дают свои результаты - ты явно стал сильнее.'
    elif message == '🛡Защита' and (_hero['gold'] >= ((int(_hero['def']) - 4) * 20) and _hero['def'] < 75):
        db.add_gold(user_id, -((int(_hero['def']) - 4) * 20))
        db.add_def(user_id, 1)
        text = '🛡Кости сросшиеся заново - крепче прежних. А твои теперь очень крепкие.'
    elif message == '❤Здоровье' and (_hero['gold'] >= ((int(_hero['hp']) - 90) * 25) and _hero['hp'] < 250):
        db.add_gold(user_id, -((int(_hero['hp']) - 90) * 25))
        db.add_max_hp(user_id, 10)
        text = '❤Чем крепче тело, тем большую потерю крови оно сможет пережить. Как вы это провернули? Все вопросы к селезёнке.'


    elif message == '💰Утка' and (_hero['diamond'] >= ((int(_skill['gold']) + 1) * 7) and _skill['gold'] < 10):
        db.add_diamond(user_id, -((int(_skill['gold']) + 1) * 7))
        db.add_sgold(user_id, 1)
        text = '💰Глаз, намётанный во время участия в утиных боях уже машинально подмечает лишние монетки...'
    elif message == '👝Сумочка' and (_hero['diamond'] >= ((int(_skill['bag']) - 4) * 5) and _skill['bag'] < 15):
        db.add_diamond(user_id, -((int(_skill['bag']) - 4) * 5))
        db.add_sbag(user_id, 1)
        text = '👝С новым Bag Of Holding™ вы сможете унести на 10% горы больше! (Мы не несем ответственности за неправильное использование полученного пространства)'


    elif message == '💫Усиленный удар' and (_hero['diamond'] >= ((int(_skill['crit']) + 1) * 8) and _skill['crit'] < 20):
        db.add_diamond(user_id, -((int(_skill['crit']) + 1) * 8))
        db.add_scrit(user_id, 1)
        text = '💫Точность нужна только пи... только лучникам? Ха! Теперь вы можете одним точным ударом уложить противника, иногда даже случайно.'
    elif message == '💔Ловкий удар' and (_hero['diamond'] >= ((int(_skill['bleed']) + 1) * 8) and _skill['bleed'] < 20):
        db.add_diamond(user_id, -((int(_skill['bleed']) + 1) * 8))
        db.add_sbleed(user_id, 1)
        text = '💔Бестиарий Монстров И Подземных Тварей подсказывает, где находятся артерии у монстров, подсвинков и каменных горгулий.'
    elif message == '🖤Подозрительный удар' and (_hero['diamond'] >= ((int(_skill['vamp']) + 1) * 8) and _skill['vamp'] < 20):
        db.add_diamond(user_id, -((int(_skill['vamp']) + 1) * 8))
        db.add_svamp(user_id, 1)
        text = '🖤... Ничего не изменилось? Но от меча словно исходит злая аура... И почему солнце так палит?'


    elif message == '⬅️Вернуться':
        bot_hero(user_id)
        return
    else:
        text = 'Произошла ошибка.\nВозможно у вас недостаточно средств или вы достигли совершенства.'
    send_message(user_id, text)
