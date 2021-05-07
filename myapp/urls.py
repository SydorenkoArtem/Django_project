from django.urls import path
from myapp.views import (homepage, product_list, product_detail)

urlpatterns = [
    path("", homepage, name="home"),
    path("product/", product_list, name="list"),
    path("product/<product_slug>/", product_detail, name="detail"),
]
