from django.shortcuts import render
from django.http import JsonResponse
from .forms import ProductDataForm, ProductImageFormSet
from .models import ProductData, ProductImage, CategoryData
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.serializers import serialize
import json
from .serializers import ProductMetaDataSerializer, ProductDataSerializer
from rest_framework.decorators import api_view
from rest_framework import response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .search import get_categories_from_prompt
import uuid

from random import shuffle


@ensure_csrf_cookie
def Set_CSRF_Cookie(request):
    return JsonResponse({})



@api_view(["GET"])
def Get_Product(request):
    product_filter = request.GET.get("product_unique_id", None)
    try:
        products = ProductData.objects.get(product_unique_id=product_filter)
        serializer = ProductDataSerializer(
            products, many=False, context={"request": request}
        )
        return JsonResponse(serializer.data, safe=False)
    except:
        return JsonResponse({})



@api_view(["GET"])
def Get_All_Products(request):
    products = ProductData.objects.all()
    paginator = Paginator(products, 10)  # Show 10 objects per page
    page_number = request.GET.get("page") if request.GET.get("page") else 1
    try:
        product_page_objects = paginator.page(page_number)
    except PageNotAnInteger:
        product_page_objects = paginator.page(1)
    except EmptyPage:
        product_page_objects = paginator.page(paginator.num_pages)
    serializer = ProductMetaDataSerializer(
        product_page_objects, many=True, context={"request": request}
    )
    return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
def Get_Featured_Products(request):
    print("---------> Finding the featured products")
    products = ProductData.objects.filter(product_featured = True)
    paginator = Paginator(products, 20)  # Show 10 objects per page
    page_number = request.GET.get("page") if request.GET.get("page") else 1
    try:
        product_page_objects = paginator.page(page_number)
    except PageNotAnInteger:
        product_page_objects = paginator.page(1)
    except EmptyPage:
        product_page_objects = paginator.page(paginator.num_pages)
    serializer = ProductMetaDataSerializer(
        product_page_objects, many=True, context={"request": request}
    )
    return JsonResponse(serializer.data, safe=False)
@api_view(["GET"])
def Get_Similar_Products(request):
    products = ProductData.objects.all()
    paginator = Paginator(products, 3)  # Show 10 objects per page
    page_number = request.GET.get("page") if request.GET.get("page") else 1
    try:
        product_page_objects = paginator.page(page_number)
    except PageNotAnInteger:
        product_page_objects = paginator.page(1)
    except EmptyPage:
        product_page_objects = paginator.page(paginator.num_pages)
    serializer = ProductMetaDataSerializer(
        product_page_objects, many=True, context={"request": request}
    )
    return JsonResponse(serializer.data, safe=False)


def Upload_Product_Data(request):
    if request.method == "POST":
        product_form = ProductDataForm(request.POST)
        image_formset = ProductImageFormSet(
            request.POST, request.FILES, queryset=ProductImage.objects.none()
        )

        if product_form.is_valid() and image_formset.is_valid():
            product = product_form.save()
            for form in image_formset.cleaned_data:
                if form:
                    image = form["image"]
                    caption = form.get("caption", "")
                    ProductImage.objects.create(
                        product=product, image=image, caption=caption
                    )
            return JsonResponse(
                {"status": "success", "product_id": product.id}, status=201
            )
        else:
            # Print errors for debugging
            print("Product Form Errors:", product_form.errors)
            for form in image_formset.forms:
                print("Image Form Errors:", form.errors)
            errors = {
                "product_form_errors": product_form.errors,
                "image_formset_errors": [form.errors for form in image_formset.forms],
            }
            return JsonResponse({"status": "error", "errors": errors}, status=400)


def upload_category_data(request):
    if request.method == "POST":
        product_data = ProductData.objects.all()
        for product in product_data:
            print("------> Updating for product " , product.product_name)
            category_list = product.product_categories
            uuid = product.product_unique_id
            for category in category_list:
                category = category.lower()
                category_item = CategoryData.objects.filter(
                    category_name=category
                ).first()
                if not category_item:
                    new_category_item = CategoryData.objects.create(
                        category_name=category, product_uuid_list=[uuid]
                    )
                else:
                    category_item.product_uuid_list.append(uuid)
                    category_item.save()
    return JsonResponse({"success": True})


def Search_Products(request):

    def search_function(category):
        categories = CategoryData.objects.filter(category_name__contains=category)
        products = ProductData.objects.filter(product_name__contains=category)
        print("Length ----> " , len(categories) , len(products) , category)
        product_unique_id_list = []
        for each_catergory in categories:
            product_unique_id_list.extend(each_catergory.product_uuid_list)
        for each_product in products:
            product_unique_id_list.append(each_product.product_unique_id) 
        product_data = ProductData.objects.filter(
            product_unique_id__in=product_unique_id_list
        )
        product_map = {product.product_unique_id: product for product in product_data}
        product_data = [product_map[unique_id] for unique_id in product_unique_id_list]
        return product_data
    prompt = request.GET.get("prompt", None)
    categories_list = (request.GET.get("categories_list", None).lower()).split(",")
    search_id = request.GET.get("search_id", None)
    sort_by = request.GET.get("sort_by", None)
    limit = request.GET.get("limit", 10)
    offset = request.GET.get("offset", 1)
    product_data = []
    if search_id:
        # Redis Logic
        product_data = None
        return
    elif categories_list and len(categories_list[0])!=0:
        search_category = []
        for each_category in categories_list:
            product_data.extend(search_function(each_category))
            product_data = list(set(product_data))
            search_category.append(each_category)
        for each_category in categories_list:
            for each_splitted in each_category.split(" "): 
                if each_splitted not in search_category: 
                    product_data.extend(search_function(each_splitted))
                    product_data = list(set(product_data))
                    search_category.append(each_splitted)
    else:
        product_data = ProductData.objects.all() 
    if not search_id:
        search_id = uuid.uuid4()
        # Redis Logic
    print("--------> Total products" , len(product_data))
    paginator = Paginator(product_data, limit)  # Show 10 objects per page
    try:
        product_page_objects = paginator.page(offset)
    except PageNotAnInteger:
        product_page_objects = paginator.page(1)
    except EmptyPage:
        product_page_objects = paginator.page(paginator.num_pages)
    serializer = ProductMetaDataSerializer(
        product_page_objects, many=True, context={"request": request}
    )
    import random
    data = serializer.data
    return JsonResponse(data, safe=False)

@api_view(["GET"])
def Get_Gemini_Categories(request):
    prompt = request.GET.get("prompt", None)
    categories = get_categories_from_prompt(prompt)
    print("------> " , prompt , categories)
    return JsonResponse(categories, safe=False)
