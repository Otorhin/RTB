def get_hero(user_id):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT * FROM `user` WHERE `user_id` = '" + str(user_id) + "'"
        cursor.execute(sql)
        result = cursor.fetchone()
    db.close()
    if result:
        if result['emoji']:
            result['nick'] = result['emoji'] + result['nick']
        if result['guild_id']:
            result['nick'] = '[' + get_guild(result['guild_id'])['tag'] + ']' + result['nick']
        return (result)
    else:
        return False


def add_rating(user_id, rating):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user` SET `rating` = rating + %s WHERE user_id = %s"
        cursor.execute(sql, (rating, user_id))
    db.commit()
    db.close()

def create_hero(user_id):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "INSERT INTO `user` (`user_id`, `nick`, `ach`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (user_id, otrh_f.nick_generator(), 'start'))

        sql = "INSERT INTO `user_equip` (`user_id`) VALUES (%s)"
        cursor.execute(sql, (user_id))

        sql = "INSERT INTO `user_inventory` (`user_id`) VALUES (%s)"
        cursor.execute(sql, (user_id))

        sql = "INSERT INTO `user_skill` (`user_id`) VALUES (%s)"
        cursor.execute(sql, (user_id))
    db.commit()
    db.close()
    return (get_hero(user_id))