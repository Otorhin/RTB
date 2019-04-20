def add_gold(user_id, gold):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user` SET `gold` = gold + %s WHERE user_id = %s"
        cursor.execute(sql, (gold, user_id))
    db.commit()
    db.close()


def add_diamond(user_id,diamond):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user` SET `diamond` = diamond + %s WHERE user_id = %s"
        cursor.execute(sql, (diamond, user_id))
    db.commit()
    db.close()


def add_pizza(user_id,pizza):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user` SET `pizza` = pizza + %s WHERE user_id = %s"
        cursor.execute(sql, (pizza, user_id))
    db.commit()
    db.close()


def add_exp(user_id,exp):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user` SET `exp` = exp + %s WHERE user_id = %s"
        cursor.execute(sql, (exp, user_id))
    db.commit()
    db.close()


def new_lvl(user_id, new_exp):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user` SET `lvl` = lvl + 1 WHERE user_id = %s"
        cursor.execute(sql, (user_id))
        sql = "UPDATE `user` SET `new_exp` = %s WHERE user_id = %s"
        cursor.execute(sql, (new_exp, user_id))
        sql = "UPDATE `user` SET `gold` = gold + 300 WHERE user_id = %s"
        cursor.execute(sql, (user_id))
        sql = "UPDATE `user` SET `diamond` = diamond + 10 WHERE user_id = %s"
        cursor.execute(sql, (user_id))
    db.commit()
    db.close()