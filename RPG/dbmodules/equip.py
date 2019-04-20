def add_equip(id):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user_inventory_2` SET `equipped` = '1' WHERE `id` = %s;"
        cursor.execute(sql, (id))
    db.commit()
    db.close()

def del_equip(id):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user_inventory_2` SET `equipped` = '0' WHERE `id` = %s;"
        cursor.execute(sql, (id))
    db.commit()
    db.close()

def off_equip(typee):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user_inventory_2` SET `equipped` = '0' WHERE `type` = %s;"
        cursor.execute(sql, (typee))
    db.commit()
    db.close()

def old_get_equip(user_id):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    _equip = {'head' : None, 'mask' : None, 'body' : None, 'gun' : None, 'legs' : None, 'shand' : None, 'amulet' : None}

    with db.cursor() as cursor:
        sql = "SELECT * FROM `user_equip` WHERE user_id = %s"
        cursor.execute(sql, (user_id))
        result = cursor.fetchone()
        if not result:
            sql = "INSERT INTO `user_equip` (`user_id`) VALUES (%s)"
            cursor.execute(sql, (user_id))
            sql = "SELECT * FROM `user_equip` WHERE user_id = %s"
            cursor.execute(sql, (user_id))
            result = cursor.fetchone()
    if result['head']:
        _equip['head'] = result['head'].split('_')
    if result['mask']:
        _equip['mask'] = result['mask'].split('_')
    if result['body']:
        _equip['body'] = result['body'].split('_')
    if result['gun']:
        _equip['gun'] = result['gun'].split('_')
    if result['legs']:
        _equip['legs'] = result['legs'].split('_')
    if result['shand']:
        _equip['shand'] = result['shand'].split('_')
    if result['amulet']:
        _equip['amulet'] = result['amulet'].split('_')

    db.close()
    return (_equip)


def get_equip(user_id):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    _equip = {'head' : None, 'mask' : None, 'body' : None, 'gun' : None, 'legs' : None, 'shand' : None, 'amulet' : None}

    with db.cursor() as cursor:
        sql = "SELECT * FROM `user_inventory_2` WHERE user_id = %s and `equipped` = 1"
        cursor.execute(sql, (user_id))
        result = cursor.fetchall()
    if result:
        for alluser in result:
            _equip[alluser['type']] = [alluser['name']]
            if alluser['rname']:
                _equip[alluser['type']].append(alluser['rname'])
    db.close()
    return (_equip)
