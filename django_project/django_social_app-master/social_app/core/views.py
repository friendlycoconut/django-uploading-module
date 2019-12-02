
# core/views.py
from multiprocessing import Process, Queue
from time import sleep
import multiprocessing.dummy as multiprocessing
import time
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from datetime import datetime

from .models import File

# Create your views here.
def login(request):
  return render(request, 'login.html')





def dummyTask():
 time.sleep(3)
 fileSet = File.objects.filter(status="Pending")

 for file in fileSet:


   file.status = 'Ready'
   file.save(update_fields=['status'])

  
@login_required
def upload(request):
  context = {}
  if request.method == 'POST':
    uploaded_file = request.FILES['document']
    fs = FileSystemStorage()
    fs.save(uploaded_file.name, uploaded_file)
    name = fs.save(uploaded_file.name, uploaded_file)
    size_bytes = uploaded_file.size
    size_kbytes = size_bytes/1000

    datetime_file= datetime.now()
    datetime_str = datetime_file.strftime("%Y-%m-%d-%H-%M-%S")
    status = 'Pending'
    print(name)
    print(uploaded_file.size)
    print(datetime_str)
    url = fs.url(name)
    file = File.objects.create(filename=name,size=size_kbytes,datetime_file=datetime_str,status=status,url=url)

    file.save()


    allvideos = File.objects.all()
    context['files'] = allvideos
    #context['name'] = name
  else:
    context = {}
    allvideos = File.objects.all()
    if File.objects.filter(status="Pending"):
      dummyTask() #многопоточность не удалась


    context['files'] = allvideos

  return render(request, 'upload.html', context)



