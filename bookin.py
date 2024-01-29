import mysql.connector
class book:
    def init(self):
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Dheeraj@123",
            database="railway2")
    def trainfetch(self,src,dest):
        cur= self.conn.cursor()
        cur.execute(f'''select ROUTES.TRAIN_NO,SOURCE,STOP1,STOP2,STOP3,STOP4,DESTINATION FROM ROUTES INNER JOIN TRAIN_DETAILS ON
                    ROUTES.TRAIN_NO=train_details.TRAIN_NO
                    WHERE SOURCE='{src}' OR STOP1='{src}' OR STOP2='{src}' OR STOP3='{src}' OR STOP4='{src}';''')
        dt=cur.fetchall()
        try:
            tr=[]
            for i in dt:
                for j in i[i.index(src)+1:]:
                    if j==dest:
                        tr.append(i)

        except:
            pass
        print(tr)
    def addpassenger(self,pid,pname,age,gen,mn):
        self.cur = self.conn.cursor()
        self.cur.execute(f"INSERT INTO PASSENGERS VALUES({pid},'{pname}',{age},'{gen}',{mn})")
        self.conn.commit()
        print("passenger added sucessfully")
    def addtransaction(self,tid,pid,amount,mode):
        self.cur = self.conn.cursor()
        self.cur.execute(f"INSERT INTO TRANSACTIONS VALUES({tid},{pid},{amount},'{mode}')")
        self.conn.commit()
        print("transaction sucessfully")
    
    def bookticket(self,bid,pid,cls,stno,tid,source,dest,train_no):
        self.cur = self.conn.cursor()
        self.cur.execute(f"INSERT INTO BOOK_TICKETS VALUES({bid},{pid},'{cls}',{stno},{tid},'{source}'','{dest}',{train_no})")
        self.conn.commit()
        print("ticket has been booked")
        print(pid,stno,bid,cls,source,dest,train_no,tid)

    
    


        
    