from django.urls import path
from myapp2.views import home, products, catalog

urlpatterns = [
    path("homepage/", home),
    path("products/<slug:product_id>", products),
    path("catalog/", catalog),

]
