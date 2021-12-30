from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request,'index.html',)

def record(request):
    eid = request.GET.get('text','default')
    print(eid)
    params = {"ID": eid}
    return render(request,'analyze.html',params)
def aboutme(request):
    return render(request,"aboutme.html")

def contach(request):
    djtext=request.GET.get("name1")
    params={"name11" : djtext}
    return render(request,'contach.html',params)