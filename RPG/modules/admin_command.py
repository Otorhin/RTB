def admin_notify(user_id, message):
    import time
    i = 0

    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT * FROM `user`"
        cursor.execute(sql)
        result = cursor.fetchall()
    for alluser in result:
        try:
            send_message(alluser['user_id'], message)
        except:
            pass
        i += 1
        if i == 5:
            i = 0
            time.sleep(1.5)
    db.close()

    send_message(user_id, 'Done')
    clear_hand(user_id)



def clear_hand_player(user_id,message):
    text = get_hero(message)
    button = get_start_button(message)
    send_message(message, text, button)

    send_message(user_id, 'Done')
    clear_hand(user_id)