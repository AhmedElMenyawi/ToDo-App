from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDo_Item
import datetime


def todolist(request):
    All_ToDo_Items = ToDo_Item.objects.all()
    context = {'All_ToDo_Items': All_ToDo_Items}
    return render(request, 'todolist.html', context)

def addtodo(request):
    new_item = ToDo_Item(content=request.POST['content'], datecreated=datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    new_item.save()
    return HttpResponseRedirect('/todo/')

def removetodo(request, todo_id):
    item = ToDo_Item.objects.get(id=todo_id)
    item.delete()
    return HttpResponseRedirect('/todo/')