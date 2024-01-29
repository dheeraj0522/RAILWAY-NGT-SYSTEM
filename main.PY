#importing required modules
from traindetails import details
from train_capacity import details
from routes import routes
from bookin import book
import numpy as np
print ("***Welcome to railway managment system***")
print("****for Inserting the data enter-----1---")
print("****for Inserting the data enter-----2---")
print("****for Inserting the data enter-----3---")
print("****for Inserting the data enter-----4---")



opr=int(input("please Enter Your Operations  : "))
if opr==1:
    print("--- for inserting the data in train_details press _ 1 ")
    print("--- for inserting the data in train_capacity press _ 2 ")
    print("--- for inserting the data in Routes press _ 3 ")
    print("--- for Booking a ticket press _ 4 ")
    inopr=int(input("please select the above operations : "))
    if inopr==1:
        obj1=details()
        train_no=int(input("please enter train No : "))
        src=input("please enter the src name : ")
        dst=input("please enter the dst name : ")
        tname=input("please enter the train name : ")
        obj1.insertdetails(train_no,src,dst,tname)

    if inopr==2:
        obj1=details()
        train_no=int(input("please enter train No : "))
        AC_1=int(input("please enter the AC_1 name : "))
        AC_2=int(input("please enter the AC_2 name : "))
        AC_3=int(input("please enter the AC_3 name : "))
        SL=int(input("please enter the SL name : "))
        GENERAL=int(input("please enter the GENERAL name : "))
        obj1.capacityinsert(train_no,AC_1,AC_2,AC_3,SL,GENERAL)

    if inopr==3:
        obj1=routes()
        obj2=details()
        obj2.trainnofetchroutes()
        train_no=int(input("please enter train No : "))
        stop1=input("please enter the stop1 name : ")
        stop2=input("please enter the stop2 name : ")
        stop3=input("please enter the stop3 name : ")
        stop4=input("please enter the sto4 name : ")
        obj1.ruoutesinsert(train_no,stop1,stop2,stop3,stop4)
    if inopr==4:
        source=input('from:')
        dest=input('to:')
        obj=book()
        obj.trainfetch(source,dest)
        trainno=int(input("please enter trainno:"))
        cls=input('please enter your coach:')
        #passenger info
        pid=int(input('please enter id:'))
        pname=input("please enter name: ")
        age = int(input("please enter age: "))
        gen=input('please enter gender:')
        mn=int(input('please enter mobile number:'))
        obj.addpassenger(pid,pname,age,gen,mn)
        #making transaction
        tid = int(input('please enter id: '))
        amount=int(input("please enter amount:"))
        mode =input("please enter amount:")
        #booking ticket
        bid = np.random.randint(0,500000,1)[0]
        stno= np.random.randint(0,50,1)[0]
        obj.bookticket(bid,pid,cls,stno,tid,source,dest,trainno)







if opr==2:
    pass
if opr==3:
    pass   
if opr==4:
    pass








""""from traindetails import details
obj1=details()
train_no=int(input("please enter train No :"))
src=input("please enter the src name")
dst=input("please enter the dst name")
tname=input("please enter the train name")
obj1.insertdetails(train_no,src,dst,tname)
obj1."""