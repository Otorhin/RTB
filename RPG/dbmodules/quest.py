def get_quest(user_id):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT * FROM `quest` WHERE `user_id` = '" + str(user_id) + "'"
        cursor.execute(sql)
        result = cursor.fetchone()
    db.close()
    if not result:
        return (create_quest(user_id))
    else:
        return (result)


def change_quest(user_id = '', quest = '', monster = None, item = None, killed = None, need = '', allquest = 0, lastquest = None, inv = None):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `quest` SET `need` = %s WHERE user_id = %s"
        cursor.execute(sql, (need, user_id))
        sql = "UPDATE `quest` SET `quest` = %s WHERE user_id = %s"
        cursor.execute(sql, (quest, user_id))
        sql = "UPDATE `quest` SET `monster` = %s WHERE user_id = %s"
        cursor.execute(sql, (monster, user_id))
        sql = "UPDATE `quest` SET `killed` = %s WHERE user_id = %s"
        cursor.execute(sql, (killed, user_id))
        sql = "UPDATE `quest` SET `item` = %s WHERE user_id = %s"
        cursor.execute(sql, (item, user_id))
        sql = "UPDATE `quest` SET `allquest` = %s WHERE user_id = %s"
        cursor.execute(sql, (allquest, user_id))
        sql = "UPDATE `quest` SET `inv` = %s WHERE user_id = %s"
        cursor.execute(sql, (inv, user_id))
        if lastquest:
            sql = "UPDATE `quest` SET `lastquest` = %s WHERE user_id = %s"
            cursor.execute(sql, (lastquest, user_id))
    db.commit()
    db.close()


def create_quest(user_id):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "INSERT INTO `quest` (`user_id`) VALUES (%s)"
        cursor.execute(sql, (user_id))
    db.commit()
    db.close()
    return (get_quest(user_id))
