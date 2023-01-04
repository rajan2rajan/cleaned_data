from django.shortcuts import render,HttpResponseRedirect
from .forms import Todoforms
from .models import Todo
from django.contrib import messages

# Create your views here.

def home(request):
    # this page just show save and change button
    return render(request, 'home.html')

def save(request):
    if request.method=="POST":
        data=Todoforms(request.POST)
        if data.is_valid():
            topic = data.cleaned_data['topic']
            describe = data.cleaned_data['describe']
            time_remaning = data.cleaned_data['time_remaning']
            result=Todo(topic=topic,describe=describe,time_remaning=time_remaning)
            result.save()
            
            return HttpResponseRedirect('/save/sucessfull')
    else:
        data = Todoforms()
    return render(request,'save.html',{'forms':data})


# data save sucessfully
def sucessfull(request):
    data = Todo.objects.all()
    return render(request,'sucessfull.html',{'form':data})


def change(request):
    data = Todo.objects.all()
    return render(request, 'change.html',{'form':data})

def edit(request,pk):

    # we can do this step too but if we do then we cannot get cleaned data but we can get data

    # forms= Todoforms()    
    # data = Todo.objects.get(id=pk)
    # if request.method=="POST":
    #     data.topic = request.POST.get('topic')
    #     data.describe = request.POST.get('describe')
    #     data.time_remaning = request.POST.get('time_remaning')
    #     result = Todo(topic =data.topic,describe=data.describe,time_remaning=data.time_remaning)

    #     data.save()
    #     return HttpResponseRedirect('/save/sucessfull')
    # return render(request, 'edit.html',{'form':data})




# OR



    # if request.method =="POST":
    #     data = Todo.objects.get(id=pk)
    #     result = Todoforms(request.POST , instance=data)
    #     if result.is_valid():
    #         result.save()
    #         return HttpResponseRedirect('/save/sucessfull')
    # else:
    #     data = Todo.objects.get(id=pk)
    #     result = Todoforms(instance=data)
    #     return render(request,'edit.html',{'form':result})



# OR


    if request.method =="POST":
        data = Todo.objects.get(id=pk)
        result = Todoforms(request.POST)
        if result.is_valid():
            result.save()
            data.delete()
            return HttpResponseRedirect('/save/sucessfull')
    else:
        data = Todo.objects.get(id=pk)
        result = Todoforms(instance=data)
        return render(request,'edit.html',{'form':result})


def delete_data(request,pk):
    data=Todo.objects.get(id=pk)
    data.delete()
    result = Todo.objects.all()


    return render(request, 'sucessfull.html',{'form':result})


