def get_skill(user_id):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT * FROM `user_skill` WHERE `user_id` = '" + str(user_id) + "'"
        cursor.execute(sql)
        result = cursor.fetchone()
    db.close()
    if not result:
        return (create_skill(user_id))
    return (result)


def create_skill(user_id):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "INSERT INTO `user_skill` (`user_id`) VALUES (%s)"
        cursor.execute(sql, (user_id))
    db.commit()
    db.close()
    return (get_skill(user_id))


def add_scrit(user_id, crit):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user_skill` SET `crit` = crit + %s WHERE user_id = %s"
        cursor.execute(sql, (crit, user_id))
    db.commit()
    db.close()


def add_sbleed(user_id, bleed):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user_skill` SET `bleed` = bleed + %s WHERE user_id = %s"
        cursor.execute(sql, (bleed, user_id))
    db.commit()
    db.close()


def add_svamp(user_id, vamp):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user_skill` SET `vamp` = vamp + %s WHERE user_id = %s"
        cursor.execute(sql, (vamp, user_id))
    db.commit()
    db.close()