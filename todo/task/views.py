from django.shortcuts import render,redirect
from .models import Task 
# Create your views here.
def index(request):

    if request.method == 'POST':
        data = request.POST['data']
        if data == "":
            pass
        else:
            Task.objects.create(title=data)

    task = Task.objects.all()
    context = {'task' : task}
    return render(request,'task/index.html', context)

def Update_task(request,pk):
    
    obj = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        new_data = request.POST['data']
        obj.title = new_data
        obj.save()
        return redirect('/')

    context ={'task':obj}
    return render(request,'task/update.html',context)


def delete_task(request,pk):
    obj = Task.objects.get(id=pk)

    if request.method == 'POST':
        obj.delete()
        return redirect('/')
    
    context ={'task':obj}
    return render(request,'task/delete.html',context)