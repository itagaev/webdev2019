from django.http import JsonResponse
from django.shortcuts import render
from api.models import Task, TaskList

def task_lists(request):
    try:
        tasklists1 = TaskList.objects.all()
    except TaskList.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)
    tasklistsjson = [c.to_json() for c in tasklists1]
    return JsonResponse(tasklistsjson, safe=False)

def task_lists_id(request, pk):
    try:
        taskList = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)
    return JsonResponse(taskList.to_json(), safe=False)

def task_lists_id_tasks(request, pk):
    try:
        tasks = TaskList.objects.get(id=pk).task_set.all()
    except Task.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)
    tasksjson = [c.to_json() for c in tasks]
    return JsonResponse(tasksjson, safe=False)