def get_prof(user_id):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT * FROM `user_prof` WHERE `user_id` = '" + str(user_id) + "'"
        cursor.execute(sql)
        result = cursor.fetchone()
    db.close()
    if not result:
        return (create_prof(user_id))
    else:
        return (result)


def change_prof(user_id, need_p, need):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user_prof` SET `%s` = %s WHERE user_id = %s"
        cursor.execute(sql, (need_p, need, user_id))
    db.commit()
    db.close()


def create_prof(user_id):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "INSERT INTO `user_prof` (`user_id`) VALUES (%s)"
        cursor.execute(sql, (user_id))
    db.commit()
    db.close()
    return (get_quest(user_id))
