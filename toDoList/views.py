from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect



list = ['Create a To Do List']
message = ''

# Create your views here.
def toDoList(request):
    if request.method == 'POST':
        item = request.POST['item'] # get the new item from the form

        if item.strip():
            # add the item to the list or database
            list.append(item)
        else:
            message = 'Submit an Entry'
    elif request.method == 'GET':
        if 'remove_item' in request.GET:
            item = request.GET['remove_item'] 
            if item in list:
                list.remove(item)
    return render(request, 'toDoList.html',{'my_list':list})
    

def list_view(request):
    # retrieve the list or database
    context = {'list': list} # pass the list to the template
    return render(request, 'toDoList.html', context)
