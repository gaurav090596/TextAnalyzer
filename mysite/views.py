# created by gaurav
import urllib
from django.http import HttpResponse
from django.shortcuts import render
import time
from datetime import datetime
import smtplib
from email.message import EmailMessage
import mysql.connector


def index(request):
    time1=datetime.today().now
    # while(True):
    #     t1=datetime.today().hour
    #     t2=datetime.today().minute
    #     t3=datetime.today().second
    #     time.sleep(1)
        # params={"hour": t1,"minutes": t2,"seconds": t3}
    times = {"timee" : time1}
    return render(request, 'index.html',times)

    # return HttpResponse("Home")

def analyze(request):
    #get the text
    eid=request.GET.get('emailid' , 'name@example.com')
    djtext=request.GET.get('text','default')
    removepunc =request.GET.get('removepunc','off')
    up = request.GET.get('up', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover=request.GET.get('extraspaceremover', 'off')
    # print(djtext)
    # print(removepunc)

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if (removepunc=='on'):
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations' ,'analyzed_text': analyzed , 'email' : eid }
        djtext=analyzed
    #analyze the text
        # return render(request ,'analyze.html', params)

    if(up=='on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Upper case', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if (newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'upper case', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if (extraspaceremover == 'on'):
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] ==" ":
                pass
            else:
                analyzed = analyzed + char
                params = {'purpose': 'upper case', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
    # else:
    #     return HttpResponse("Error")
def aboutme(request):
    return render(request,"aboutme.html")

def contach(request):
    djtext=request.GET.get("name1")
    params={"name11" : djtext}
    return render(request,'contach.html',params)
def search(request):
    sr=request.GET.get("srch")
    params={"s1":sr}
    return render(request,"search.html",params)


def bmi(request):
    weight = request.GET.get("weight",1/10000)
    height = request.GET.get("height",1)
    weight = float(weight)
    height = float(height)
    height = height/100
    print(weight,height)
    bmi1 = (weight/(height * height))
    if(bmi1<18.5 and bmi1>1):
        c1="Underwieght"
    elif(bmi1>=18.5 and bmi1<=24.9):
        c1="Normal Weight"
    elif(bmi1>=25 and bmi1<=29.9):
        c1="Overweight"
    elif(bmi1>=30):
        c1="Obese"
    elif(bmi1==1):
        c1="none"
    params={"bmi2": bmi1,"index": c1}
    return render(request,"bmi.html",params)

def sql(request):
    # mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="pythondb")
    # v1 = request.GET.get("name")
    # v2 = request.GET.get("college")
    # v3 = request.GET.get("phno")


    # if mydb.is_connected():
    #     print("connected succesfully")
    # cur = mydb.cursor()
    # # return render(request, "sql.html")
    # # v1 = request.GET.get("name")
    # # v2 = request.GET.get("college")
    # # v3 = request.GET.get("phno")
    #
    # querry = "INSERT INTO student(name,college,phno) values('{}','{})".format(v1,v2)
    #
    # cur.execute(querry)
    # mydb.commit()
    # print("querry fired succesfully")
    return render(request, "sql.html")

def sqlfire(request):
    v1 = request.GET.get("name")
    v2 = request.GET.get("college")






























    v3 = request.GET.get("phno")
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="pythondb")
    if mydb.is_connected():
        print("connected succesfully")
    cur = mydb.cursor()

    querry = "INSERT INTO student(name,college,phno) values('{}','{}',{})".format(v1, v2, v3)

    cur.execute(querry)
    mydb.commit()
    print("entred succesfully")

    return render(request, "sqlfire.html")

# def capfirst(request):
#     return HttpResponse("capfirst")
#
# def newlineremove(request):
#     return HttpResponse("newlineremove")
#
# def spaceremove(request):
#     return HttpResponse("spaceremove <a href='/'>back</a>")
#
# def charcount(request):
#     return HttpResponse("charcount")
#

# def text(text):
#     with open('D:\\pythonProject\\mysite\\mysite\\text.txt') as f:
#         a = f.read()
#         return HttpResponse(a)
# def domail(sendmail):
#     # importing module
#     import os
#
#
#     # taking email id pass and storing in a varibale
#     path = ('C:\\Users\\91636\\Desktop\\email.txt')
#     path1 = ('C:\\Users\\91636\\Desktop\\pass.txt')
#     with open(path) as f:
#         user = f.read()
#     with open(path1) as f:
#         passwd = f.read()
#
#     # creating email Body
#     msg = EmailMessage()
#     msg['Subject'] = 'this is a test mail'
#     msg['From'] = user
#     msg['To'] = 'stargaurav.singh0@gmail.com'
#     msg.set_content('this a mail sent form python')
#
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#         smtp.login(user, passwd)
#         smtp.send_message(msg)
#     return HttpResponse('email sent')

