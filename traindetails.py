import mysql.connector

class details:
    def _init_(self):
        self.conn= mysql.connector.connect(
            host = "localhost",
            user="root",
            password="Dheeraj@123",
            database= "railway2")
    def insertdetails(self,tno,src,dst,tname):
        self.cur = self.conn.cursor()
        self.cur.execute(f"INSERT INTO train_details VALUES({tno},'{src}','{dst}','{tname}')")
        self.conn.commit()
        print("data has been inserted successfully")
    def trainofetch(self):
        self.cur=self.conn.cursor()
        self.cur.execute('''select train_details.train_no from train_details
                         left join train_capacity on
                         train_details.train_no=train_capacity.train_no
                         Where stop1 is null''')
        print(self.cur.fetchall())


