from django.shortcuts import render, redirect
from .models import ToDo

# Create your views here.
def todo_list(request):
  todos = ToDo.objects.order_by('-id')
  return render(request, 'todo/index.html', {'todos': todos})

def create_todo(request):
  if request.method == 'POST':
    title = request.POST.get('title')
    ToDo.objects.create(title=title)
  
  return redirect('todo_list')

def complete_todo(request, todo_id):
  todo = ToDo.objects.get(id = todo_id)
  todo.completed = True
  todo.save()
  return redirect('todo_list')

def delete_todo(request, todo_id):
  todo = ToDo.objects.get(id = todo_id)
  todo.delete()
  return redirect('todo_list')
