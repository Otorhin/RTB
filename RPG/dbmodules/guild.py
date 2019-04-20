def get_guild(guild_id):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT * FROM `guild` WHERE `id` = '" + str(guild_id) + "'"
        cursor.execute(sql)
        result = cursor.fetchone()
    db.close()
    return (result)


def get_guild_pass(password):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT * FROM `guild` WHERE `password` = '" + str(password) + "'"
        cursor.execute(sql)
        result = cursor.fetchone()
    db.close()
    if result:
    	return (result)
    else:
    	return False


def change_guild(user_id, guild_id):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user` SET `guild_id` = %s WHERE user_id = %s"
        cursor.execute(sql, (guild_id, user_id))
    db.commit()
    db.close()

def create_guild(user_id, name, tag, _password):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "INSERT INTO `guild` (`name`, `tag`, `creator`, `password`) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (name, tag, user_id, _password))
    db.commit()
    db.close()


def change_gpass(guild_id, _password):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `guild` SET `password` = %s WHERE `id` = %s"
        cursor.execute(sql, (_password, guild_id))
    db.commit()
    db.close()







def add_guild_money(user_id, guild_id, money, count = None):
    _hero = get_hero(user_id)
    
    if money == 'gold':
        if count:
            _money = count
        else:
            _money = _hero['gold']
        add_gold(user_id, -_money)
    else:
        if count:
            _money = count
        else:
            _money = _hero['diamond']
        add_diamond(user_id, -_money)
    
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        if money == 'gold':
            sql = "UPDATE `guild` SET `gold` = gold + %s WHERE id = %s"
        else:
            sql = "UPDATE `guild` SET `diamond` = diamond + %s WHERE id = %s"
        cursor.execute(sql, (_money, guild_id))
    db.commit()
    db.close()


def _23_add_guild_money(user_id, guild_id, money, count = None):
    _hero = get_hero(user_id)
    
    if money == 'gold':
        add_gold(user_id, count)
    else:
        add_diamond(user_id, count)
    
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        if money == 'gold':
            sql = "UPDATE `guild` SET `gold` = gold - %s WHERE id = %s"
        else:
            sql = "UPDATE `guild` SET `diamond` = diamond - %s WHERE id = %s"
        cursor.execute(sql, (count, guild_id))
    db.commit()
    db.close()



def guild_upgrade_build1(guild_id):
    _guild = get_guild(guild_id)
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `guild` SET `build1` = build1 + 1 WHERE `id` = %s"
        cursor.execute(sql, (guild_id))
        sql = "UPDATE `guild` SET `gold` = gold - %s WHERE id = %s"
        cursor.execute(sql, ( ((_guild['build1'] + 1) * 750), guild_id))
        sql = "UPDATE `guild` SET `diamond` = diamond - %s WHERE id = %s"
        cursor.execute(sql, ( ((_guild['build1'] + 1) * 20), guild_id))
    db.commit()
    db.close()


def guild_upgrade_build2(guild_id):
    _guild = get_guild(guild_id)
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `guild` SET `build2` = build2 + 1 WHERE `id` = %s"
        cursor.execute(sql, (guild_id))
        sql = "UPDATE `guild` SET `gold` = gold - %s WHERE id = %s"
        cursor.execute(sql, ( ((_guild['build2'] + 1) * 2500), guild_id))
        sql = "UPDATE `guild` SET `diamond` = diamond - %s WHERE id = %s"
        cursor.execute(sql, ( ((_guild['build2'] + 1) * 50), guild_id))
    db.commit()
    db.close()


def guild_upgrade_build3(guild_id):
    _guild = get_guild(guild_id)
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `guild` SET `build3` = build3 + 1 WHERE `id` = %s"
        cursor.execute(sql, (guild_id))
        sql = "UPDATE `guild` SET `gold` = gold - %s WHERE id = %s"
        cursor.execute(sql, ( ((_guild['build3'] + 1) * 2500), guild_id))
        sql = "UPDATE `guild` SET `diamond` = diamond - %s WHERE id = %s"
        cursor.execute(sql, ( ((_guild['build3'] + 1) * 50), guild_id))
    db.commit()
    db.close()