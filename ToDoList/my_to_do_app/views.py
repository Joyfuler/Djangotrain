from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    # return HttpResponse("my_to_do_app first page")
    todos = Todo.objects.all() #모두부름
    content = {
        'todos': todos
        }
    return render(request, 'my_to_do_app/index.html', content)

def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    new_todo.save() #DB에 실제로 저장할 시 사용.
    return HttpResponseRedirect(reverse('index'))
    #return HttpResponse("Create To do 수행 => " + user_input_str)

def doneTodo(request):
    done_todo_id = request.GET['todoNum']
    todo = Todo.objects.get(id = done_todo_id)
    print("보이지 않게 하려는 todo의 id는 :", done_todo_id)
    todo.isDone = True
    todo.save()
    return HttpResponseRedirect(reverse('index'))

# def doneTodo(request):
#     done_todo_id = request.GET['todoNum']
#     todo = Todo.objects.get(id = done_todo_id)
#     todo.isDone = True
#     todo.save()
#     return HttpResponseRedirect(reverse('index'))