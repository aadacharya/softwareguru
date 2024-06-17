from django import forms
from .models import ProductData , ProductImage
from django.forms import modelformset_factory

class ProductDataForm(forms.ModelForm):
    class Meta:
        model = ProductData
        fields = ["product_summary","product_categories","product_pros","product_cons","product_usecases","product_toolfor","product_pricing","product_rating","product_name","product_unique_id","product_pricing_available","product_affiliate_available","product_url"]

ProductImageFormSet = modelformset_factory(
    ProductImage,
    fields=('image', 'caption'),
    extra=2  # Adjust the number of extra forms as needed
)