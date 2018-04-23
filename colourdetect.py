import cv2
import timeit
import numpy
import time
from datetime import date
import datetime
import MySQLdb as m
import serial
import types
import domc
#import rfidreader1
def fine(d1,m1,y1,d2,m2,y2):
    a=0
    d=date(y1,m1,d1)
    e=date(y2,m2,d2)
    delta=e-d
    a=delta.days
    return a
db=m.connect("localhost","root","","cap")
cur=db.cursor()
start_time=timeit.default_timer()
#myimg = cv2.imread('/home/pi/capstone_barcode-08-04-master/barcode_01.jpg')
#avg_color_per_row = numpy.average(myimg, axis=0)
#avg_color = numpy.average(avg_color_per_row, axis=0)
#avg=0
#for i in avg_color:
#    avg+=i
#print "Unique Identity for colour detection :",
avg=domc.colourdetect()
sql="select id,name,bookname,issuedate,returndate from f where bookid='%s' and status='1';" %avg
cur.execute(sql)
result=cur.fetchall()
if result==():
    print "None"
else:
    for row in result:
        Id=row[0]
        name=row[1]
        bookname=row[2]
        issuedate=row[3]
        returndate=row[4]
        print "Registration Number='%s'"%Id,
        print "Name='%s'"%name,
        print "Book Name='%s'"%bookname
        q=1
	l=[]
        l=returndate.split('/')
        now=time.strftime("%d/%m/%Y")
	k=[]
        k=now.split("/")
        j=map(int,k)
        p=map(int,l)
        g=fine(p[0],p[1],p[2],j[0],j[1],j[2])
        if g<0:
            g=0
        print "Fine=Rs.%s"%g
        sql="update f set status='0' where bookid='%s';"%avg
        try:
             cur.execute(sql)
             db.commit()
        except:
            db.rollback()
                
print "Book Returned Successfully"
elapsed_time=timeit.default_timer()-start_time
print "Time elapsed in average colour detection :",
print elapsed_time,
print "in seconds"
