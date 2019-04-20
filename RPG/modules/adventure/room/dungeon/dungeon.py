class unknown_dungeon():

    @staticmethod
    def on_entry(user_id):
        db.add_rating(user_id, -5)
        text = '🔥Ты упал в это подземелье. Не очень верится, что ты сможешь выйти отсюда живым, но удачи.'
        text += '\nПервое что ты тут встречаешь, это развилка. Выбирай куда ступишь, налево или направо.'
        button = [['Налево'], ['Направо']]
        text = adventure.header(user_id) + text
        send_message(user_id, text, button)
        set_hand(user_id, unknown_dungeon().handler)
        temp[str(user_id) + '_1'] = {}
        temp[str(user_id) + '_1']['room'] = 0

    @staticmethod
    def in_maze(user_id):
        text = 'Ты снова стоишь перед развилкой. Выбирай свой путь. Лево или право.'
        button = [['Налево'], ['Направо']]
        text = adventure.header(user_id) + text
        send_message(user_id, text, button)
        set_hand(user_id, unknown_dungeon().handler)

    @staticmethod
    def handler(user_id, message):
        _skill = db.get_skill(user_id)
        if message.lower() in ['налево', 'направо']:
            set_hand(user_id, unknown_dungeon().waiting)
            _random = random.random()
            send_message(user_id, 'Ты пошел {}.'.format(message.lower()))
            if (_random < 0.05 and temp[str(user_id) + '_1']['room'] > 5) or temp[str(user_id) + '_1']['room'] > 15:
                bd_adventure2.append(['unknown_dungeon().on_exit', 15, [user_id]])
                return
            if _random < 0.25 and temp[str(user_id) + '_1']['room'] > 0:
                temp[str(user_id) + '_1']['room'] += 1
                bd_adventure2.append(['unknown_dungeon().in_maze', 15, [user_id]])
                return
            else:
                temp[str(user_id) + '_1']['room'] += 1
                bd_adventure2.append(['unknown_dungeon().pve_battle', 15, [user_id]])
                return
        else:
            pass

    @staticmethod
    def pve_battle(user_id):
        _mob = random.choice(['witch', 'skeletons', 'troll', 'witch', 'ghost', 'rats'])
        text = adventure.header(user_id)
        text += '`' + monsters[_mob]['text'] + '`'
        send_message(user_id, text, [['Навалять мобу']], parse_mode='markdown')
        set_hand(user_id, unknown_dungeon().waiting)
        bd_adventure2.append(['monster_battle', 15, [user_id, _mob]])
        #monster_battle(user_id, _mob)

    @staticmethod
    def on_exit(user_id):
        _inventory = db.get_inventory(user_id)
        text = 'Ты смог выйти из этого приключения. Не каждый может его пройти без потерь.'
        text += '\n\nВ сундуке ты нашел :'
        if len(_inventory) < 0:
            text += '\n' + i_get_equip(user_id)

        _getting_gold = i_get_gold(user_id) + i_get_gold(user_id) + i_get_gold(user_id) + i_get_gold(user_id) + i_get_gold(user_id) + i_get_gold(user_id) + i_get_gold(user_id) + i_get_gold(user_id)
        text += '\nЗолота : ' + str(_getting_gold)

        text += '\nАлмазов : ' + str(i_get_diamond(user_id) + i_get_diamond(user_id))

        text += '\nРесурсов : ' + i_get_inventory(user_id) + ', ' + i_get_inventory(user_id) + ', ' + i_get_inventory(user_id)

        text = adventure_header(user_id) + text
        db.add_rating(user_id, 10)
        set_hand(user_id, start_game_hand)
        send_message(user_id, text, get_start_button(user_id))
        return

    @staticmethod
    def waiting(user_id, message):
        text = 'Ты занят. Ожидай.'
        send_message(user_id, text)


monsters['skeletons'] = {
    'name' : 'Скелеты',
    'level': 'easy',
    'gold' : False,
    'diamond' : False,
    'loot' : False,
    'room' : 'unknown_dungeon().in_maze',
    'text' : 'Кости... Столько костей! Не, ну здесь точно обитает тролль. А вон там что за горка... А, нет, опять кости. Ну и где же его носит? Подождите-ка...\nКогда ты наступил на кость, ты допустил большую ошибку. И, возможно, последнюю в своей жизни. Эти кости живые. Удачи в бою со скелетами!'
}

monsters['troll'] = {
    'name' : 'Тролль',
    'level': 'easy',
    'gold' : False,
    'diamond' : False,
    'loot' : False,
    'room' : 'unknown_dungeon().in_maze',
    'text' : 'Ого, какая большая дверь... Что внутри? Сейчас проверим...\nТолько приоткрыв дверь, нечто зловонное двумя пальцами взяло и отшвырнуло тебя в стену. Судя по всему, бой тебе предстоит непростой, ведь это - Тролль!'
}

monsters['witch'] = {
    'name' : 'Ведьма',
    'level': 'easy',
    'gold' : False,
    'diamond' : False,
    'loot' : False,
    'room' : 'unknown_dungeon().in_maze',
    'text' : 'Как же тут воняет... Может, здесь обитает тролль? Да вроде непохоже на него... нет ни экскрементов, ни обглоданных костей... А? Что это за смех доносится до тебя из конца комнаты? \nВсё-таки, запахи готовящихся зелий и кала гигантских троллей немного похожи друг на друга. А тебя я поздравляю. Ты наткнулся на Ведьму.'
}

monsters['ghost'] = {
    'name' : 'Призрак',
    'level': 'easy',
    'gold' : False,
    'diamond' : False,
    'loot' : False,
    'room' : 'unknown_dungeon().in_maze',
    'text' : 'Тут так... пусто. Будто здесь никогда и ничего не было, никакой мебели или картин, вообще не похоже, что по этому полу хоть раз ступала нога человека. Лишь толстый слой пыли, образовавшийся в результате пустования этого помещения много, много веков... Не слышно ничего, кроме биения твоего сердца... Но только пока твоего. Берегись, ты попался в ловушку бестелесного монстра - призрака!'
}

monsters['rats'] = {
    'name' : 'Крысы',
    'level': 'easy',
    'gold' : False,
    'diamond' : False,
    'loot' : False,
    'room' : 'unknown_dungeon().in_maze',
    'text' : 'По комнате к тебе напрямую бежит крыса. Причём, бежит очень бодро. Ты с искренним удивлением на лице принялся наблюдать, как она пытается как-то навредить тебе и твоим доспехам. Ты отшвырнул её одним ударом ботинка. Обычная крыса. Может, слегка глупая. Ничем особенным не отличается от других своих собратьев, стопившихся возле двери, через которую ты и вошел сюда... "Ага, отрезали путь к отступлению, значит? Да вы же всего лишь крысы, как вы можете навредить латным..." - хотел было произнести ты, как, внезапно, вся орава крыс с обоих концов комнаты побежала к тебе. Угадай, кто завтра не вернётся к ужину, если ты хоть раз споткнёшься или остановишься по пути к другой двери?'
}