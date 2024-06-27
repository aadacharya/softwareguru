from django.urls import path
from . import views
from . import properties

urlpatterns = [
    # Get_Product
    
    path('/get_featured_products', views.Get_Feature_Products, name='get_featured_products'),
    path('/get_product', views.Get_Product, name='get_product'),
    path('/get_products', views.Get_All_Products, name='get_all_products'),
    path(f"{properties.get_csfr_token}",views.Set_CSRF_Cookie,name="get_csrf_token"),
    path(f'{properties.upload_product_data}',views.Upload_Product_Data,name="upload_product_data"),
    path(f'{properties.upload_product_image}',views.Upload_Product_Image,name="upload_product_image"),
    path(f'{properties.delete_product_data}',views.Delete_Product_Data,name="delete_product_data"),
    path(f'{properties.delete_product_image}',views.Delete_Product_Image,name="delete_product_image")

]

