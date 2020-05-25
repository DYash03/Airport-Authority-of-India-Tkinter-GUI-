from tkinter import *
import pyqrcode
from pyzbar.pyzbar import decode
import pyzbar.pyzbar as pyzbar
from PIL import Image
import sqlite3
import cv2
import smtplib
import base64
import numpy as np
import random as r
scr0=Tk()
scr0.title("QR Handler")
scr0.configure(bg="#5F64EE")
canvas = Canvas(width=1000,height=1000)
canvas.pack()
photo = PhotoImage(file='C:\\Users\\hp\\Desktop\\Python Projects\\tkinter projects\\AAI00.png')
canvas.create_image(210,200,image=photo ,anchor=NW)

a=" अतिथि   देवो   भव: "
lq=Label(scr0,text="AIRPORTS  AUTHORITY OF INDIA",bg="black",fg="blue",font=('time','71','bold'))
lq.place(x=1,y=2)
l=Label(scr0,text=a,bg="#5F64EE",fg="blue",font=('time','89','bold'))
l.place(x=265,y=665)
b0=Button(scr0,text="LOGIN",bg="red",fg="black",font=('Time','20','bold'),command=lambda:mainpage())
b0.place(x=700,y=550)
conn=sqlite3.connect('Details.db')
c=conn.cursor()
global SR
SR=""
def mainpage():
    scr=Toplevel()
    scr.configure(bg="#306EFF")
    f="FOUNDED IN APRIL 1995"
    l=Label(scr,text="AIRPORTS AUTHORITY OF INDIA ",bg="brown",fg="pink",font=('time','71','bold'))
    l.place(x=2,y=2)
    l2=Label(scr,text=f,bg="#306EFF",fg="yellow",font=('time','60','bold'))
    l2.place(x=300,y=700)
    b=Button(scr,text="Admin",bg="red",fg="pink",font=('Time','50','bold'),command=lambda:lsadmin())
    b.place(x=100,y=200)
    b2=Button(scr,text="Worker",bg="blue",fg="pink",font=('Time','50','bold'),command=lambda:luser())
    b2.place(x=1100,y=200)
    b2=Button(scr,text="SCAN QR",bg="green",fg="pink",font=('Time','40','bold'),command=lambda:homeQR())
    b2.place(x=100,y=500)
    b3=Button(scr,text="Required",bg="black",fg="pink",font=('Time','40','bold'),command=lambda:RequireD())
    b3.place(x=1100,y=500)

    def RequireD():
        scrr=Toplevel()
        scrr.configure(bg="#306EFF")
        a="Complain Id"+"\t\t"+"Phone No."+"\t\t"+"Required"+"\n\n"
        l=Label(scrr,text="REQUIREMENTS",bg="black",fg="yellow",font=('time','80','bold'))
        l.place(x=300,y=2)  
        textr=Text(scrr,width=101,height=17,wrap=WORD,font=('Time','20','bold'),selectbackground="grey")
        textr.place(x=7,y=150)
        c.execute("SELECT * from REQUIREMENTS")
        for row in c.fetchall():
            a=a+str(row)+"\n"
        textr.insert(0.0,a)
    
    def homeQR():
        cap = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_PLAIN

        while True:
            _, frame = cap.read()

            decodedObjects = pyzbar.decode(frame)
            for obj in decodedObjects:
                SR1=obj.data
                cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                            (255, 0, 0), 3)

            cv2.imshow("Frame", frame)

            key = cv2.waitKey(1)
            if key ==ord('q'):
                break;
        cap.release()        
        cv2.destroyAllWindows
        SR=SR1.decode("utf-8")
        c.execute("SELECT Contents FROM QRDetails WHERE SR = ?",[SR])
        p=c.fetchone()
        texts=Text(scr,width=25,height=6,wrap=WORD,font=('Time','20','bold'),selectbackground="grey")
        texts.place(x=550,y=300)
        texts.insert(0.0,p[0])
    

    def lsadmin():
        scr1=Toplevel()
        scr1.configure(bg="blue")
        scr1.geometry('400x105')
        l=Label(scr1,text="KEY",bg="blue",fg="white",font=('time','20','bold'))
        l.place(x=5,y=5)
        e=Entry(scr1,bg="white",fg="black",font=('time','20','bold'),show="*")
        e.place(x=80,y=5)
        b=Button(scr1,text="Login",bg="green",fg="black",font=('Time','20','bold'),command=lambda:sadmin())
        b.place(x=140,y=45)
        def sadmin():
            t=e.get()
            c.execute("SELECT Key FROM Superadmin")
            p=c.fetchone()
            if(p[0]==t):
                scr1.destroy()
                scr2=Toplevel()
                scr2.configure(bg="#306EFF")
                l=Label(scr2,text="WELCOME TO SUPER ADMIN'S DESK ",bg="brown",fg="pink",font=('time','62','bold'))
                l.place(x=2,y=2)
                l1=Label(scr2,text="CREATE ADMIN",bg="#306EFF",fg="green",font=('time','40','bold'))
                l1.place(x=150,y=120)      
                l2=Label(scr2,text="DISSOLVE MEMBERS",bg="#306EFF",fg="red",font=('time','40','bold'))
                l2.place(x=900,y=120)
                l3=Label(scr2,text="Enter Name",bg="#306EFF",fg="black",font=('time','30','bold'))
                l3.place(x=2,y=220)
                l4=Label(scr2,text="Enter Email",bg="#306EFF",fg="black",font=('time','30','bold'))
                l4.place(x=2,y=300)
                l5=Label(scr2,text="Enter Mob",bg="#306EFF",fg="black",font=('time','30','bold'))
                l5.place(x=2,y=380)
                l6=Label(scr2,text="Enter Key",bg="#306EFF",fg="black",font=('time','28','bold'))
                l6.place(x=2,y=460)
                l7=Label(scr2,text="Enter Key",bg="#306EFF",fg="black",font=('time','28','bold'))
                l7.place(x=900,y=220)
                l8=Label(scr2,text="Reason",bg="#306EFF",fg="black",font=('time','28','bold'))
                l8.place(x=900,y=300)
                e5=Entry(scr2,bg="white",fg="black",font=('time','30','bold'))
                e5.place(x=1090,y=220)
                e1=Entry(scr2,bg="white",fg="black",font=('time','30','bold'))
                e1.place(x=250,y=220)
                e2=Entry(scr2,bg="white",fg="black",font=('time','30','bold'))
                e2.place(x=250,y=300)
                e3=Entry(scr2,bg="white",fg="black",font=('time','30','bold'))
                e3.place(x=250,y=380)
                e4=Entry(scr2,bg="white",fg="black",font=('time','30','bold'))
                e4.place(x=250,y=460)
                text=Text(scr2,width=29,height=3,wrap=WORD,font=('Time','20','bold'),selectbackground="grey")
                text.place(x=1090,y=300)
                text1=Text(scr2,width=29,height=8,wrap=WORD,font=('Time','20','bold'),selectbackground="grey")
                text1.place(x=1090,y=500)
                b=Button(scr2,text="CREATE",bg="green",fg="black",font=('Time','20','bold'),command=lambda:screate())
                b.place(x=300,y=550)
                b1=Button(scr2,text="DISSOLVE",bg="red",fg="black",font=('Time','20','bold'),command=lambda:dissolve())
                b1.place(x=1090,y=410)
                b2=Button(scr2,text="ADMIN'S LIST",bg="black",fg="pink",font=('Time','20','bold'),command=lambda:alist())
                b2.place(x=880,y=700)
                def screate():
                    Name=e1.get()
                    Mob=e3.get()
                    Key=e4.get()
                    Email=e2.get()
                    c.execute("INSERT INTO Admin(Name, Email, Key , Mob) VALUES(?,?,?,?)",(Name,Email,Key,Mob))
                    conn.commit()
                    content="AIRPORT AUTHORITY OF INDIA\n"+"From SuperAdmin's Desk\n"+"Your Account has been successfully created!\n"+"Now you are an Admin and your login key is :\n"+Key+"\nKindly don't share your Key with anyone."+"\nHave a nice day ahead."
                    mail=smtplib.SMTP('smtp.gmail.com',587)
                    mail.ehlo()
                    mail.starttls()
                    mail.login('sender email','password')
                    mail.sendmail('sender email',Email,content)
                    mail.close()
                
                def dissolve():
                    K=e5.get()
                    c.execute("SELECT Email FROM Admin WHERE Key = ?",[K])
                    Email=c.fetchone()
                    c.execute("DELETE FROM Admin WHERE Key = ?",[K])
                    conn.commit()
                    reasonn=text.get(0.0,"end")
                    content="AIRPORT ATHORITY OF INDIA\n"+"From SuperAdmin's Desk\n"+"Your Account has been successfully removed reason being:\n"+reasonn+"\nContact AAI for more details."
                    mail=smtplib.SMTP('smtp.gmail.com',587)
                    mail.ehlo()
                    mail.starttls()
                    mail.login('sender email','password')
                    mail.sendmail('sender email',Email[0],content)
                    mail.close()
                    
                    

                def alist():
                    c.execute("SELECT Name FROM Admin")
                    p=c.fetchall()
                    for i in p:
                        text1.insert(0.0,i)
                        text1.insert(0.0,"\n")
            else:
                c.execute("SELECT Key FROM Admin")
                p=c.fetchall()
                for i in p:
                    if(t==i[0]):
                        flag=1
                        break;
                if(flag==1):
                    scr1.destroy()
                    scr4=Toplevel()
                    scr4.configure(bg="#306EFF")
                    l=Label(scr4,text="WELCOME TO ADMIN'S DESK ",bg="brown",fg="pink",font=('time','78','bold'))
                    l.place(x=3,y=2)
                    l1=Label(scr4,text="CREATE USERS",bg="#306EFF",fg="red",font=('time','40','bold'))
                    l1.place(x=150,y=140)      
                    l2=Label(scr4,text="CREATE QR-CODE",bg="#306EFF",fg="yellow",font=('time','40','bold'))
                    l2.place(x=900,y=140)
                    l3=Label(scr4,text="Enter Name",bg="#306EFF",fg="black",font=('time','30','bold'))
                    l3.place(x=2,y=240)
                    l4=Label(scr4,text="Enter Email",bg="#306EFF",fg="black",font=('time','30','bold'))
                    l4.place(x=2,y=320)
                    l5=Label(scr4,text="Enter Mob",bg="#306EFF",fg="black",font=('time','30','bold'))
                    l5.place(x=2,y=400)
                    l6=Label(scr4,text="Enter Key",bg="#306EFF",fg="black",font=('time','28','bold'))
                    l6.place(x=2,y=480)
                    e1=Entry(scr4,bg="white",fg="black",font=('time','30','bold'))
                    e1.place(x=250,y=240)
                    e2=Entry(scr4,bg="white",fg="black",font=('time','30','bold'))
                    e2.place(x=250,y=320)
                    e3=Entry(scr4,bg="white",fg="black",font=('time','30','bold'))
                    e3.place(x=250,y=400)
                    e4=Entry(scr4,bg="white",fg="black",font=('time','30','bold'))
                    e4.place(x=250,y=480)
                    b=Button(scr4,text="CREATE",bg="red",fg="black",font=('Time','20','bold'),command=lambda:acreate())
                    b.place(x=300,y=550)
                    l7=Label(scr4,text="Enter S/N",bg="#306EFF",fg="black",font=('time','30','bold'))
                    l7.place(x=900,y=240)
                    l8=Label(scr4,text="Details",bg="#306EFF",fg="black",font=('time','30','bold'))
                    l8.place(x=900,y=320)
                    e5=Entry(scr4,bg="white",fg="black",font=('Time','30','bold'))
                    e5.place(x=1090,y=240)
                    text=Text(scr4,width=29,height=7,wrap=WORD,font=('Time','20','bold'),selectbackground="grey")
                    text.place(x=1090,y=320)
                    b1=Button(scr4,text="CreateQR",bg="yellow",fg="black",font=('Time','20','bold'),command=lambda:createqr())
                    b1.place(x=1090,y=555)

                
                def createqr():
                    a=e5.get()
                    b=a+".png"
                    Contents=text.get(0.0,"end")
                    qr=pyqrcode.create(a)
                    qr.png(b,scale=8)
                    c.execute('CREATE TABLE IF NOT EXISTS QRDetails(SR TEXT ,Contents TEXT)')
                    conn.commit()
                    c.execute("INSERT INTO QRDetails(SR,Contents) VALUES(?,?)",(a,Contents))
                    conn.commit()
                def acreate():
                    Name=e1.get()
                    Mob=e3.get()
                    Key=e4.get()
                    Email=e2.get()
                    c.execute('CREATE TABLE IF NOT EXISTS User(Name TEXT ,Email TEXT,Key TEXT , Mob REAL)')
                    conn.commit()
                    c.execute("INSERT INTO User(Name, Email, Key , Mob) VALUES(?,?,?,?)",(Name,Email,Key,Mob))
                    conn.commit()
                    content="AIRPORT AUTHORITY OF INDIA\n"+"From Admin's Desk\n"+"Your Account has been successfully created!\n"+"Now you are a User and your login key is :\n"+Key+"\nKindly don't share your Key with anyone."+"\nHave a nice day ahead."
                    mail=smtplib.SMTP('smtp.gmail.com',587)
                    mail.ehlo()
                    mail.starttls()
                    mail.login('sender email','password')
                    mail.sendmail('sender email',Email,content)
                    mail.close()


    def luser():
        scr5=Toplevel()
        scr5.geometry('400x105')
        scr5.configure(bg="blue")
        l=Label(scr5,text="KEY",bg="blue",fg="white",font=('time','20','bold'))
        l.place(x=5,y=5)
        e=Entry(scr5,bg="white",fg="black",font=('time','20','bold'),show="*")
        e.place(x=80,y=5)
        b=Button(scr5,text="Login",bg="green",fg="black",font=('Time','20','bold'),command=lambda:user())
        b.place(x=140,y=45)

        def user():
            t=e.get()
            flag=0
            c.execute("SELECT Key FROM User")
            p=c.fetchall()
            for i in p:
                if(t==i[0]):
                    flag=1
                    break;
            if(flag==1):
                scr5.destroy()
                scr6=Toplevel()
                scr6.configure(bg="#306EFF")
                l=Label(scr6,text="WELCOME TO USER'S DESK ",bg="brown",fg="pink",font=('time','82','bold'))
                l.place(x=3,y=2)
                l=Label(scr6,text="SCAN AND UPDATE",bg="#306EFF",fg="black",font=('time','30','bold'))
                l.place(x=1000,y=150)
                l1=Label(scr6,text="REQUIREMENTS",bg="#306EFF",fg="black",font=('time','30','bold'))
                l1.place(x=200,y=150)
                b2=Button(scr6,text="SCAN QR",bg="red",fg="black",font=('Time','20','bold'),command=lambda:userQR())
                b2.place(x=1000,y=480)
                textu1=Text(scr6,width=35,height=8,wrap=WORD,font=('Time','20','bold'),selectbackground="grey")
                textu1.place(x=1000,y=210)
                textu2=Text(scr6,width=50,height=15,wrap=WORD,font=('Time','20','bold'),selectbackground="grey")
                textu2.place(x=10,y=210)
                b4=Button(scr6,text="SUBMIT",bg="yellow",fg="black",font=('Time','20','bold'),command=lambda:Usubmit())
                b4.place(x=635,y=700)
                ep=Entry(scr6,bg="white",fg="black",font=('Time','30','bold'))
                ep.place(x=150,y=700)
                l=Label(scr6,text="Phno.",bg="#306EFF",fg="black",font=('time','30','bold'))
                l.place(x=10,y=700)
                def userQR():
                    
                    cap = cv2.VideoCapture(0)
                    font = cv2.FONT_HERSHEY_PLAIN

                    while True:
                        _, frame = cap.read()

                        decodedObjects = pyzbar.decode(frame)
                        for obj in decodedObjects:
                            SR1=obj.data
                            cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                                    (255, 0, 0), 3)

                        cv2.imshow("Frame", frame)

                        key = cv2.waitKey(1)
                        if key ==ord('q'):
                            break;
                    cap.release()        
                    cv2.destroyAllWindows
                    SR=SR1.decode("utf-8")
                    c.execute("SELECT Contents FROM QRDetails WHERE SR = ?",[SR])
                    p=c.fetchone()
                    Z=p[0]
                    textu1.insert(0.0,Z)
                    b3=Button(scr6,text="UPDATE",bg="green",fg="black",font=('Time','20','bold'),command=lambda:Uupdate())
                    b3.place(x=1390,y=480)
                    def Uupdate():
                        u=textu1.get(0.0,"end")
                        c.execute("UPDATE QRDetails SET Contents=? WHERE Contents=?",[u,Z])
                        conn.commit()


                def Usubmit():
                    c.execute('CREATE TABLE IF NOT EXISTS Requirements(ComplainID TEXT ,Pno REAL , Req TEXT)')
                    conn.commit()
                    ComplainID=""
                    for i in range(0,8):
                        ComplainID=ComplainID+str(r.randint(0,9))
                    Us=textu2.get(0.0,"end")
                    Pno=ep.get()
                    c.execute("INSERT INTO Requirements(ComplainID,Pno,Req) VALUES(?,?,?)",(ComplainID,Pno,Us))
                    conn.commit()
                    

scr0.mainloop()
