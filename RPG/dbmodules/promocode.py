def get_promocode(code) :
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT * FROM `promocode` WHERE code = %s"
        cursor.execute(sql, (code))
        result = cursor.fetchone()
    db.close()
    if result:
        _promocode = [result['action'], result['number']]
        return (_promocode)
    else:
        return False


def del_promocode(code):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "DELETE FROM `promocode` WHERE code = %s"
        cursor.execute(sql, (code))
    db.commit()
    db.close()

def change_ref(user_id, ref_id):
    db = pymysql.connect(host=config.mysql_server, user=config.mysql_user, password=config.mysql_password,
                         db=config.mysql_bd, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `user` SET `referal` = %s WHERE user_id = %s"
        cursor.execute(sql, (ref_id, user_id))
    db.commit()
    db.close()
