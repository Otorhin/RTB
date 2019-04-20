def bot_shop(user_id):
    text = 'Заходя на территорию магазина, вы видите несколько прилавков'
    text += '\n\nПрилавок старого кузнеца - старик уже и забыл как делать что-то кроме алюминиевого шмотья'
    text += '\n\nПрилавок дальнего путешественника - данный человек потратил всю свою жизнь на поиск неизведанного.'
    text += '\n\nПрилавок алхимика - прилавок с вкусными зельями'
    send_message(user_id, text,[['К старому кузнецу'],['К путешественнику'], ['К алхимику'], ['Назад']])
    set_hand(user_id, bot_shop_hand)

def bot_shop_hand(user_id, message):
    if message.lower() == 'к старому кузнецу' :
        old_smith(user_id)
    elif message.lower() == 'к путешественнику' :
        traveler(user_id)
    elif message.lower() == 'к алхимику' :
        bartender(user_id)
    elif message.lower() == 'назад':
        bot_city(user_id)
    else:
        pass