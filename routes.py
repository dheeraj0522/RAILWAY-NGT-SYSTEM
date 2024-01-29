import mysql.connector
class routes:
    def init(self):
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Dheeraj@123",
            database="railway2")
    def ruoutesinsert(self,train_no,stop1,stop2,stop3,stop4):
        self.cur=self.conn.cursor()
        self.cur.execute(f"insert into routes values({train_no},'{stop1}','{stop2}','{stop3}','{stop4}')")
        self.conn.commit()
        print("Data is Inserted sucessfully")