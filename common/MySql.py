import pymysql
from common.ConfigSend import conf

class MySqlDb:

    def __init__(self):
        self.conn = pymysql.connect(host=conf.get("mysql","host"), port=conf.get("mysql","port"),
                               user=conf.get("mysql","user"),
                               database=conf.get("mysql","database"),
                               password=conf.get("mysql","password"),
                               charset=conf.get("mysql","charset"),
                               cursorclass=pymysql.cursors.DictCursor)
        self.cur=self.conn.cursor()



    def select_one_data(self,sql):
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()




    def select_all_data(self,sql):
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    #向数据库提交，处理事务
    def update(self,sql):
        self.cur.execute(sql)
        self.conn.commit()


    def get_count(self,sql):
        self.conn.commit()
        return self.cur.execute(sql)


    def close(self):
        self.cur.close()
        self.conn.close()














