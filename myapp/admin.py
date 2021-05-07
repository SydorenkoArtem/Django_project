from django.contrib import admin
from myapp.models import Product, Category, Comment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ["category", "product", "amount"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ["category"]


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    fields = ["product", "comment"]

