from django.shortcuts import render
from django.http import JsonResponse
from .forms import ProductDataForm , ProductImageFormSet
from .models import ProductData , ProductImage
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
