# Create your views here.

from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import List, Item

def home_page(request):
    return render(request, 'home.html')    
        
def view_list(request, list_id):
    list = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list})

def new_list(request):
    list = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list)
    return redirect('/lists/%d/' % (list.id,))

def add_item(request, list_id):
    list = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list)
    return redirect('/lists/%d/' % (list.id,))
