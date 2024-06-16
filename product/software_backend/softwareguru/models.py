from django.db import models

# Create your models here.

class ProductData(models.Model): 
    product_summary = models.TextField()
    product_categories = models.JSONField()
    product_pros = models.JSONField()
    product_cons = models.JSONField()
    product_usecases = models.JSONField()
    product_toolfor = models.JSONField()
    product_pricing = models.JSONField()
    product_rating = models.IntegerField()
    product_name = models.CharField(max_length=100)
    product_unique_id = models.CharField(max_length=36)
    product_pricing_available = models.BooleanField(default=False)
    product_affiliate_available = models.BooleanField(default=False)
    product_url = models.URLField(max_length=200)






