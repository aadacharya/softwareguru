from django.contrib import admin
from .models import ProductData, ProductImage, CategoryData , CategoryMain

admin.site.register(ProductData)
admin.site.register(ProductImage)
admin.site.register(CategoryData)
admin.site.register(CategoryMain)

# Register your models here.
