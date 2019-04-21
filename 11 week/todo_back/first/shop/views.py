from django.http import JsonResponse
from django.shortcuts import render
from shop.models import Category

def category_list(request):
    categories = Category.objects.all()
    json_categories = [c.to_json() for c in categories]
    data = {
        'categories': json_categories
    }
    return JsonResponse(data, safe=False)

def category_detail(request, pk):
    try:
        c = Category.objects.get(id=pk)
    except Category.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)
    return JsonResponse(c.to_json())

def category_products(request, pk):
    try:
        c = Category.objects.get(id=pk)
    except Category.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)

    products = c.product_set.all()
    products1 = [c.to_json() for c in products]
    data = {
        'data': products1
    }
    return JsonResponse(data, safe = False)
