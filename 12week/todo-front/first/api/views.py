from django.http import JsonResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from api.serializers import TaskListSerializer, TaskListSerializer2, TaskSerializer

from api.models import Task, TaskList
"""
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
    return JsonResponse(tasksjson, safe=False) """

@csrf_exempt
def task_lists(request):
    if request.method == 'GET':
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer(task_lists, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = TaskListSerializer2(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors)

@csrf_exempt
def task_lists_id(request, pk):
    try:
        task_lists = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if(request.method == 'GET'):
        serializer = TaskListSerializer2(task_lists)
        return JsonResponse(serializer.data, status=200)
    elif(request.method=='PUT'):
        data = json.loads(request.body)
        serializer = TaskListSerializer(instance=task_lists, data= data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        task_lists.delete()
        return JsonResponse({}, safe=False, status=204)

@csrf_exempt
def task_lists_id_tasks(request, pk):
    try:
        tasks_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    tasks = tasks_list.task_set.all()
    serializer = TaskSerializer(tasks, many=True)
    return JsonResponse(serializer.data, safe=False)