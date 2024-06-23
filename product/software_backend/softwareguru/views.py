from django.shortcuts import render
from django.http import JsonResponse
from .forms import ProductDataForm , ProductImageFormSet
from .models import ProductData , ProductImage
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.serializers import serialize
import json
from .serializers import ProductMetaDataSerializer , ProductDataSerializer
from rest_framework.decorators import api_view
from rest_framework import response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@ensure_csrf_cookie
def Set_CSRF_Cookie(request):
    return JsonResponse({})

# Create your views here.
@api_view(['GET'])
def Get_Product(request):
    product_filter = request.GET.get('product_unique_id',None)
    try:
        products = ProductData.objects.get(product_unique_id=product_filter)
        serializer = ProductDataSerializer  (products, many=False , context={'request': request})
        return JsonResponse(serializer.data,safe=False)
    except: 
        return JsonResponse({})
@api_view(['GET'])
def Get_All_Products(request):
    products = ProductData.objects.all()
    paginator = Paginator(products, 10)  # Show 10 objects per page
    page_number = request.GET.get('page') if request.GET.get('page') else 1
    try:
        product_page_objects = paginator.page(page_number)
    except PageNotAnInteger:
        product_page_objects = paginator.page(1)
    except EmptyPage:
        product_page_objects = paginator.page(paginator.num_pages)
    serializer = ProductMetaDataSerializer  (product_page_objects, many=True , context={'request': request})
    return JsonResponse(serializer.data,safe=False)
def Upload_Product_Data(request): 
    if request.method == 'POST':
        product_form = ProductDataForm(request.POST)
        image_formset = ProductImageFormSet(request.POST, request.FILES, queryset=ProductImage.objects.none())

        if product_form.is_valid() and image_formset.is_valid():
            product = product_form.save()
            for form in image_formset.cleaned_data:
                if form:
                    image = form['image']
                    caption = form.get('caption', '')
                    ProductImage.objects.create(product=product, image=image, caption=caption)
            return JsonResponse({'status': 'success', 'product_id': product.id}, status=201)
        else:
            # Print errors for debugging
            print("Product Form Errors:", product_form.errors)
            for form in image_formset.forms:
                print("Image Form Errors:", form.errors)
            errors = {
                'product_form_errors': product_form.errors,
                'image_formset_errors': [form.errors for form in image_formset.forms]
            }
            return JsonResponse({'status': 'error', 'errors': errors}, status=400)
def Delete_Product_Data(request):
    pass
def Upload_Product_Image(request):
    pass
def Delete_Product_Image(request):
    pass
