from django.contrib import admin
from product_catelog.models import Product, ProductCategory
 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'price', 'image', 'category', 'created_at', 'updated_at')
    list_display = ('name', 'category', 'price',)
    list_filter = ('name','created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name',)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'image', 'created_at', 'updated_at')
    list_display = ('name', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name',)
