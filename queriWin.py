import mysql.connector
class Mysql:
    def __init__(self):
        self.connectDB()
        self.createDB()
        self.createTb()

    def connectDB(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "your password enter"
        )
        self.cursor = self.mydb.cursor()

    def createDB(self):
        self.cursor.execute("create database if not exists avia")
        self.cursor.execute("use avia")

    def createTb(self):
        self.cursor.execute("""create table if not exists bilet(id int auto_increment primary key,
                        uchish_dv text,
                        qonish_dv text,
                        count_b int,
                        price real,
                        uchish_time text,
                        qonish_time text)""")
    def insertTb(self,uchish,qonish,count,price,u_time,q_time):
        self.cursor.execute(f'''insert into bilet(uchish_dv,
                            qonish_dv,
                            count_b,
                            price,
                            uchish_time,
                            qonish_time) values("{uchish}",
                            "{qonish}",
                            {count},
                            {price},
                            "{u_time}",
                            "{q_time}")''')
        self.mydb.commit()    
    
    def uch_dv(self):
        self.temp_lts = []
        self.cursor.execute("select distinct(uchish_dv) from bilet")
        self.result = self.cursor.fetchall()
        for i in self.result:
            self.temp_lts.append(i[0])
        return self.temp_lts
    def qon_dv(self): 
        self.temp2_lts = [] 
        self.cursor.execute("select distinct(qonish_dv) from bilet")
        self.result1 = self.cursor.fetchall()
        for i in self.result1:
            self.temp2_lts.append(i[0])
        return self.temp2_lts 
    def celect_data(self,qayerdan,qayerga):
        self.cursor.execute(f'select count_b, price, uchish_time, qonish_time From bilet where uchish_dv = "{qayerdan}" and qonish_dv="{qayerga}"')
        self.countrs = self.cursor.fetchall()
        return self.countrs
    def buy_select(self,count,qayerdan,qayerga):
        self.cursor.execute(f'select count_b from bilet where count_b >= {count} and uchish_dv = "{qayerdan}" and qonish_dv="{qayerga}"')
        self.temp_count = self.cursor.fetchone()
        if self.temp_count:
            self.soni()
            self.countbilet = self.temp_count[0] - int(count)
            self.cursor.execute(f'update bilet set count_b = {self.countbilet} where uchish_dv = "{qayerdan}" and qonish_dv="{qayerga}"')
            return self.countbilet
        else:
            self.cursor.execute(f'select count_b from bilet where uchish_dv = "{qayerdan}" and qonish_dv="{qayerga}"')
            self.temp_acs = self.cursor.fetchone()
            return self.temp_acs[0]
    def soni(self):
        if self.temp_count is None or len(self.temp_count) == 0:
            return 0
        elif self.temp_count:
            return self.temp_count[0]
    def times_data(self,qayerdan,qayerga):
        self.cursor.execute(f'select uchish_time, qonish_time from bilet where uchish_dv = "{qayerdan}" and qonish_dv="{qayerga}"')
        self.temp_time = self.cursor.fetchall()

        return self.temp_time
cre = Mysql()
