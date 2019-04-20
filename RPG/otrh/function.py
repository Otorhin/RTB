import random
import emoji

def nick_generator():
    nicks = [
        'Васёк',
        'Геракл',
        'Фетида',
        'Зевс',
        'Врач',
        'Вкусняшка',
        'Л0ЛЬК0'
    ]
    return random.choice(nicks)

def switch_chars(txt):
    symbols = 'qwertyuiopasdfghjklzxcvbnm'
    symbols += 'йёцукенгшщзхъфывапролджэячсмитьбю'
    symbols += '1234567890'
    try:
        for symbol in txt:
            if symbol.lower() not in symbols:
                txt = txt.replace(symbol, "")
    except :
        pass
    return txt


def switch_chars_donat(txt):
    symbols = 'qwertyuiopasdfghjklzxcvbnm'
    symbols += 'йёцукенгшщзхъфывапролджэячсмитьбю'
    symbols += '1234567890'
    symbols += '|°•-_='
    try:
        _space = False
        for symbol in txt:
            if symbol in ' ' and not _space:
                _space = True
            elif symbol.lower() not in symbols:
                txt = txt.replace(symbol, "")
            else:
                _space = False
    except :
        pass
    return txt


def check_emoji(txt):
    if txt in str(emoji.UNICODE_EMOJI):
        return True
    else:
        return False


def new_guild_password(length):
    output = ""
    for x in range(length):
        output += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890')
    return output




def get_new_exp(lvl):
    new_exp = [10, 20, 75, 125, 250, 500, 850]
    if int(lvl) < 7:
        return (new_exp[lvl])
    else:
        return (99999999)