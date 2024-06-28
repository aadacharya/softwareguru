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
    product_rating = models.FloatField()
    product_name = models.CharField(max_length=100)
    product_unique_id = models.CharField(max_length=36)
    product_pricing_available = models.BooleanField(default=False)
    product_affiliate_available = models.BooleanField(default=False)
    product_url = models.URLField(max_length=200)


class ProductImage(models.Model):
    product = models.ForeignKey(
        ProductData, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="product_images/")
    caption = models.CharField(max_length=255, blank=True)


class CategoryData(models.Model):
    category_name = models.TextField()
    product_uuid_list = models.JSONField()
