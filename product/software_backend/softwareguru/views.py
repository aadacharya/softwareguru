from django.shortcuts import render
from django.http import JsonResponse
from .forms import ProuctDataForm
from django.views.decorators.csrf import ensure_csrf_cookie
import json

@ensure_csrf_cookie
def Set_CSRF_Cookie(request):
    return JsonResponse({})

# Create your views here.
def Get_All_Products(request):
    return JsonResponse({})
def Upload_Product_Data(request): 
    if request.method == 'POST':
        # data = json.loads(request.body.decode('utf-8'))
        # print(data.keys())
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        form = ProuctDataForm(data)
        if form.is_valid():
            product = form.save()
            return JsonResponse({'status':'success','product_name':product.product_name,'product_unique_id':product.product_unique_id})
        else:
            return JsonResponse({'status':'error','errors':form.errors})    
def Delete_Product_Data(request):
    pass
def Upload_Product_Image(request):
    pass
def Delete_Product_Image(request):
    pass
