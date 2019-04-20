def change_nick(user_id, nick):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user` SET `nick` = %s WHERE user_id = %s"
        cursor.execute(sql, (nick, user_id))
    db.commit()
    db.close()

def change_buff(user_id, buff):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user` SET `buff` = %s WHERE user_id = %s"
        cursor.execute(sql, (buff, user_id))
    db.commit()
    db.close()

def change_ach(user_id, ach):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user` SET `ach` = %s WHERE user_id = %s"
        cursor.execute(sql, (ach, user_id))
    db.commit()
    db.close()
    