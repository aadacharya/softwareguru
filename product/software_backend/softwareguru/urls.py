from django.urls import path
from . import views
from . import properties

urlpatterns = [
    # Get_Product
    path("get_product", views.Get_Product, name="get_product"),
    path("get_featured_products", views.Get_Featured_Products, name="get_featured_products"),
    path("get_similar_products", views.Get_Similar_Products, name="get_similar_products"),
    path("get_products", views.Get_All_Products, name="get_all_products"),
    path(f"{properties.get_csfr_token}", views.Set_CSRF_Cookie, name="get_csrf_token"),
    path(
        f"{properties.upload_product_data}",
        views.Upload_Product_Data,
        name="upload_product_data",
    ),
    path(
        f"{properties.upload_product_image}",
        views.Upload_Product_Image,
        name="upload_product_image",
    ),
    path(
        f"{properties.delete_product_data}",
        views.Delete_Product_Data,
        name="delete_product_data",
    ),
    path(
        f"{properties.delete_product_image}",
        views.Delete_Product_Image,
        name="delete_product_image",
    ),
    path("search", views.Search_Products, name="search_products"),
    path(
        f"{properties.upload_product_data}",
        views.Upload_Product_Data,
        name="upload_product_data",
    ),
    path(
        f"{properties.update_category_data}",
        views.upload_category_data,
        name="update_category_data",
    ),
]
