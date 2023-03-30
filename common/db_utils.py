import pymysql


class DBUtils:
    conn = None

    @classmethod
    def __get_conn(cls):
        if cls.conn is None:
            cls.conn = pymysql.connect(host="192.168.1.156", port=3306, user="super", password="root",
                                       database="kyscene", charset="utf8")
        return cls.conn

    @classmethod
    def __close_conn(cls):
        if cls.conn is not None:
            cls.conn.close()
            cls.conn = None

    @classmethod
    def select_data(cls, sql):
        cursor = None
        res = None
        try:
            cls.conn = cls.__get_conn()
            cursor = cls.conn.cursor()
            cursor.execute(sql)
            res = cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            cls.__close_conn()
            return res

    @classmethod
    def udi_data(cls, sql):
        cursor = None
        try:
            cls.conn = cls.__get_conn()
            cursor = cls.conn.cursor()
            cursor.execute(sql)
            print("影响行数", cls.conn.affected_rows())
            cls.conn.commit()
        except Exception as e:
            cls.conn.rollback()
            print(e)

        finally:
            cursor.close()
            cls.__close_conn()

# if __name__ == '__main__':
#     db = DBUtils()
# sql1 = 'INSERT INTO user_subscribe(id,userid,subscribe_id) VALUES("1","2","3");'
# db.udi_data(sql1)
#     sql2 = 'DELETE from user_subscribe where id="1";'
#     db.udi_data(sql2)
