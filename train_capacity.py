import mysql.connector
class details:
    def init(self):
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Dheeraj@123",
            database="railway2")
    def capacityinsert(self,train_no,AC_1,AC_2,AC_3,SL,GENERAL):
        self.cur=self.conn.cursor()
        self.cur.execute(f"insert into train_capacity values({train_no},'{AC_1}','{AC_2}','{AC_3}','{SL}','{GENERAL}')")
        self.conn.commit()
        print("Data is Inserted sucessfully")