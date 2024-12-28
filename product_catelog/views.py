from django.shortcuts import render
from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer

# Create your views here.


class ProductListViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get("category", None)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset
