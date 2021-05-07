from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=False, blank=True)

    def __str__(self):
        return self.category

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    fid = models.AutoField(primary_key=True)
    product = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.product


class Comment(models.Model):
    pid = models.AutoField(primary_key=True)
    comment = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.comment
