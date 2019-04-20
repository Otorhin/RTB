def add_atk(user_id, atk):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user` SET `atk` = atk + %s WHERE user_id = %s"
        cursor.execute(sql, (atk, user_id))
    db.commit()
    db.close()


def add_def(user_id, deff):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user` SET `def` = def + %s WHERE user_id = %s"
        cursor.execute(sql, (deff, user_id))
    db.commit()
    db.close()


def add_max_hp(user_id, max_hp):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user` SET `hp` = hp + %s WHERE user_id = %s"
        cursor.execute(sql, (max_hp, user_id))
    db.commit()
    db.close()


def add_sgold(user_id, gold):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user_skill` SET `gold` = gold + %s WHERE user_id = %s"
        cursor.execute(sql, (gold, user_id))
    db.commit()
    db.close()


def add_sbag(user_id, gold):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user_skill` SET `bag` = bag + %s WHERE user_id = %s"
        cursor.execute(sql, (gold, user_id))
    db.commit()
    db.close()


def add_stime(user_id, gold):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user_skill` SET `time` = time + %s WHERE user_id = %s"
        cursor.execute(sql, (gold, user_id))
    db.commit()
    db.close()
