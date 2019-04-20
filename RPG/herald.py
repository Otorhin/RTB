#Herald
import telebot
import config
import db
from otrh import function as otrh_f
from otrh import names
from otrh import game_config as gcfg
from otrh import equip
import traceback
from telebot import apihelper
from telebot import types

API_TOKEN = config.herald_token
bot = telebot.TeleBot(API_TOKEN, threaded = True)


@bot.channel_post_handler(func=lambda message: True)
def post_handler(post):
	_main_chat = '-1001270742403'
	bot.forward_message(_main_chat, post.chat.id, post.message_id)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

    _data = call.data.split('_')
    if bot.get_chat_member(_data[1], call.from_user.id).status  not in ['creator', 'administrator']:
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Не админ, не жми!")
    if _data[0] == 'yes':
        bot.restrict_chat_member(_data[1], _data[2], _data[3], False)
        bot.delete_message(_data[1], call.message.message_id)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Я верю что бан был обоснован.")
    else:
        bot.delete_message(_data[1], call.message.message_id)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Миссклик? Ну и ладно, без бана тоже хорошо")

    if call.data.startswith('buy_'):
        if str(call.from_user.id) == _data[1]:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Ты не можешь купить сам у себя!")
        elif call.chat_instance != '-1848070246900715408':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Торговля в данном чате запрещена!")
            bot.edit_message_text(inline_message_id=call.inline_message_id, text="Торговля в данном чате запрещена!")
        else:
            if db.get_user_inventory(_data[1])[_data[2]] < 1:
                bot.edit_message_text(inline_message_id=call.inline_message_id, text="У игрока закончился данный предмет.")
            elif db.get_hero(call.from_user.id)['gold'] >= int(_data[3]):
                db.add_inventory(call.from_user.id, _data[2], 1)
                db.add_inventory(_data[1], _data[2], -1)
                db.add_gold(call.from_user.id, -int(_data[3]))
                db.add_gold(_data[1], int(_data[3]))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Ты приобрел данный предмет!")



_ref_text = 'Привет путник 🧙‍♂️, кажется ты что-то слышал в кустах🌳, скорее жми /catch и отправься в невероятное приключение по миру RogTor✨ в котором ты найдёшь много приятных собеседников👨‍💻, опробуешь уникальную механику игры🎮и наконец-то поймёшь, что значит быть задротом🕑\nПодними свой меч во имя короля! 👑\n\nТебя тут ждут,<a href ="http://t.me/rogtorbot?start={}">жми</a>! \n<a href ="http://t.me/rogtorbot?start={}">Начать игру!</a>'

@bot.inline_handler(func=lambda query: True)
def query_text(query):
    results = []
    i = 2
    test = types.InlineQueryResultArticle(id='1', title="Пригласить друга в игру.",description="Кидает рекламный текст, с вашей реф.ссылкой",input_message_content=types.InputTextMessageContent(message_text=_ref_text.format(query.from_user.id, query.from_user.id), parse_mode='Html', disable_web_page_preview=True))
    results.append(test)

    black_list_item = ['user_id', 'logic', 'lost_cargo', 'blacksmithtools']

    if len(query.query.split(' ')) == 2 and query.query.split(' ')[0] in names.item and query.query.split(' ')[0] not in black_list_item and int(db.get_user_inventory(query.from_user.id)[query.query.split(' ')[0]]) > 0:
        try:
            _store = db.get_user_inventory(query.from_user.id)
            if int(query.query.split(' ')[1]) == round(int(query.query.split(' ')[1])) and int(query.query.split(' ')[1]) > 0 and int(query.query.split(' ')[1]) < 1001 and not (query.query.split(' ')[1].startswith('0') or query.query.split(' ')[1].startswith('+')):
                _buy_text = 'Купить у {nick}'.format(**db.get_hero(query.from_user.id))
                _buy_text += '\n{} за {}💰'.format(names.item[query.query.split(' ')[0]], query.query.split(' ')[1])
                kb = types.InlineKeyboardMarkup()
                _callback = 'buy_{}_{}_{}'.format(query.from_user.id, query.query.split(' ')[0], query.query.split(' ')[1])
                kb.add(types.InlineKeyboardButton(text="💰Купить", callback_data=_callback))
                single_msg = types.InlineQueryResultArticle(
                    id="2", title="💰Продать {} за {}".format(names.item[query.query.split(' ')[0]], query.query.split(' ')[1]),
                    input_message_content=types.InputTextMessageContent(message_text=_buy_text),
                    reply_markup=kb)
                results.append(single_msg)
        except Exception as e:
            print(e)
            pass
    bot.answer_inline_query(query.id, results, cache_time=1)


_admin = '439637823'
def listener3(messages):
    for m in messages:
        try:

            if str(m.chat.id) == '-1001434073497':
                if m.content_type != 'text' or 'Купить у' not in m.text:
                    bot.delete_message(m.chat.id, m.message_id)
                    bot.restrict_chat_member(m.chat.id, m.from_user.id, int(m.date) + (30 * 60), False)
                return

            if m.content_type != 'text':
                return

            if m.text.lower().startswith('/ro') and 'reply_to_message' in m.json and bot.get_chat_member(m.chat.id, m.from_user.id).status in ['creator', 'administrator']:
                _data = m.text.split(' ')
                _data = [x for x in _data if x]
                try:
                    _data[1] = int(_data[1])
                    text = 'Дать юзеру RO на {} минут?'.format(_data[1])
                    _data[1] = int(_data[1]) * 60
                    _timess = int(m.date) + _data[1]
                except:
                    _timess = 666
                    text = 'Дать юзеру RO навсегда?'
                markup = telebot.types.InlineKeyboardMarkup()
                markup.row_width = 1
                _callback = '_{}_{}_{}'.format(m.chat.id, m.json['reply_to_message']['from']['id'], _timess)
                markup.add(telebot.types.InlineKeyboardButton("Забанить", callback_data="yes" + _callback), telebot.types.InlineKeyboardButton("Отменить", callback_data="no" + _callback))
                bot.send_message(m.chat.id, text=text, reply_to_message_id=m.reply_to_message.message_id, reply_markup=markup, parse_mode='Html')
                bot.delete_message(m.chat.id, m.message_id)
                return
            else:
                pass

            if m.text == '!id' and str(m.from_user.id) == '439637823':
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(439637823, str(m.chat.id))
                return

        except Exception:
            bot.send_message(439637823, str(traceback.format_exc()))
        #print(m)

bot.set_update_listener(listener3)


bot.polling()