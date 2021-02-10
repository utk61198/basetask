
from django.shortcuts import render

from urllib.request import Request, urlopen
import shutil
import zipfile
import csv
from redis import Redis
from datetime import date, timedelta
import time
import os





# Create your views here.
def index(request):
    redisClient =Redis(
host='ec2-54-90-33-141.compute-1.amazonaws.com',
port=14819,
password='p1937634a5571715925d58b71f8080ef1024f125eafa2edf0a9b5c270de498664')

 
    
    header = {
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4',
        'Host': 'www.bseindia.com',
        'Referer': 'https://www.bseindia.com/',
        'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    def download_file(link, file_name, length):
        try:
            req = Request(link, headers=header)
            with open(file_name, 'wb') as writer:
                request = urlopen(req, timeout=3)
                shutil.copyfileobj(request, writer, length)
        except Exception as e:
            print('File cannot be downloaded:', e)
        finally:
            print('File downloaded with success!')

    file_name = 'new_file.zip'
    length = 1024
    print()
    today=date.today()
    d1 = today.strftime("%d%m%y")

    timenow=time.strftime("%H")
    weekday=today.strftime("%A")
    print(weekday)

    if weekday=="Monday" and int(timenow)<18:
            today=date.today()-timedelta(days=3)
            d1=today.strftime("%d%m%y")
    elif weekday=="Saturday":
            today=date.today()-timedelta(days=1)
            d1=today.strftime("%d%m%y")
    elif weekday=="Sunday":
            today=date.today()-timedelta(days=2)
            d1=today.strftime("%d%m%y")

    if int(timenow) < 18:
            today=date.today()-timedelta(days=1)
            d1=today.strftime("%d%m%y")
    
    print(d1)


    
    download_file("https://www.bseindia.com/download/BhavCopy/Equity/EQ"+d1+"_CSV.ZIP", file_name, length)
    with zipfile.ZipFile("new_file.zip", 'r') as zip_ref:
        zip_ref.extractall()
    dc=[]
    redisClient.rpush("hello","world")
    print(redisClient.lpop("hello"))
    with open("EQ"+d1+".CSV", 'r') as file:
        
        reader = csv.reader(file)
        for row in reader:
            dc.append({"Name":row[1],"Code":row[0],"OPEN":row[4],"HIGH":row[5],"LOW":row[6],"CLOSE":row[7]})
            # redisClient.rpush(row[1],row[1],row[4])
            
            
        final={"dict":dc,"filename":d1}
        

    
    os.remove("EQ"+d1+".CSV")
    os.remove("new_file.zip")
    return render(request, 'index.html',final)