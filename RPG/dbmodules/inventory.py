def add_inventory_item(user_id, type, item, rname = None):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "INSERT INTO `user_inventory_2` (`user_id`, `type`, `name`, `rname`) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (user_id, type, item, rname))
    db.commit()
    db.close()


def get_inventory_id(user_id):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT * FROM `user_inventory_2` WHERE user_id = %s and `equipped` = 0"
        cursor.execute(sql, (user_id))
        result = cursor.fetchall()
    _inventory = {}
    if result:
        for alluser in result:
            _inventory[str(alluser['id'])] = alluser['type']
    db.close()
    return (_inventory)


def del_inventory_item(id):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "DELETE FROM `user_inventory_2` WHERE `id` = %s LIMIT 1"
        cursor.execute(sql, (id))
    db.commit()
    db.close()

def add_inventory(user_id, item, number):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user_inventory` SET " + item + " = " + item + " + %s WHERE user_id = %s"
        cursor.execute(sql, (number, user_id))
    db.commit()
    db.close()


def get_inventory(user_id):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT * FROM `user_inventory_2` WHERE user_id = %s and `equipped` = 0"
        cursor.execute(sql, (user_id))
        result = cursor.fetchall()
    _inventory = []
    if result:
        for alluser in result:
            _inventory.append([alluser['type'], alluser['name'], alluser['rname'], alluser['id']])
    db.close()
    return (_inventory)

def get_count_inv(user_id, type11, name):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT * FROM `user_inventory_2` WHERE `type` = %s and `name` = %s and `user_id` = %s"
        cursor.execute(sql, (type11, name, user_id))
        result = cursor.fetchall()
    db.close()
    if result:
        _i = len(result)
    else:
        _i = 0
    return (_i)


def get_user_inventory(user_id):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT * FROM `user_inventory` WHERE `user_id` = '" + str(user_id) + "'"
        cursor.execute(sql)
        result = cursor.fetchone()
    db.close()
    if not result:
        return (create_user_inventory(user_id))
    return (result)

def create_user_inventory(user_id):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "INSERT INTO `user_inventory` (`user_id`) VALUES (%s)"
        cursor.execute(sql, (user_id))
    db.commit()
    db.close()
    return (get_user_inventory(user_id))