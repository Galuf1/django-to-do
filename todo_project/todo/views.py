from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Todo

def index(request):
    data = Todo.objects.all()

    return render(request, 'todo/index.html',{'data':data})

@csrf_exempt
def create(request):
    print('is this working?')
    if request.method == 'GET':
        return render(request, 'todo/new.html')
    elif request.method == 'POST':
        title_new = request.POST['title']
        description_new = request.POST['description']
        n_item = Todo(title=title_new, description=description_new)
        n_item.full_clean()
        n_item.save()
        
        return render(request, 'todo/detail.html', {'data':n_item})
   
def detail(request,id_query):
    data = Todo.objects.get(id = id_query)

    return render(request, 'todo/detail.html' ,{'data': data})
def update(request,id_query):
    if request.method == 'GET':
        data = Todo.objects.get(id = id_query)
        return render(request, 'todo/edit.html', {'data': data})
    elif request.method == 'POST':
        print(request)
        item = Todo.objects.get(id = id_query)
        item.title = request.POST['title']
        item.description = request.POST['description']
        item.save()
        return render(request,'todo/detail.html',{'data': item})

def delete(request,id_query):
    Todo.objects.get(id = id_query).delete()
    return HttpResponseRedirect('/todos/')