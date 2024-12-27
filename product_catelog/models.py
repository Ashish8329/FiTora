from django.db import models
from base.base_model import BaseModel
from django.utils.translation import gettext_lazy as _

class Product(BaseModel):
    name = models.CharField(
        max_length=255,
        help_text='Name of the product',
        verbose_name= _('Product Name')
        )
    description = models.TextField(
        blank=True, 
        null=True,
        )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2
        )
    image = models.ImageField(
        upload_to='products/', 
        blank=True, 
        null=True
        )
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class ProductCategory(BaseModel):
    name = models.CharField(
        max_length=255
        )
    description = models.TextField(
        blank=True, 
        null=True
        )
    image = models.ImageField(
        upload_to='product_categories/', 
        blank=True, 
        null=True
        )

    def __str__(self):
        return self.name