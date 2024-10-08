from django.db import models

from base.models import BaseModel

class Category(BaseModel):
    category_name =  models.CharField(max_length=50)
    slug = models.SlugField(unique=True , null=True, blank= True)
    category_image = models.ImageField(upload_to="categories")


class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="products")
    slug = models.SlugField(unique=True , null=True , blank=True)    # slug is used because we don't want it write as 1 ,2,3.......it shoud write as mobile, bed-sheet , pillow
    price = models.IntegerField()
    product_description = models.TextField()


#The slug field is used in Django to create a URL-friendly version of a string. It is often used in URLs to make them more readable and search engine friendly

class ProductImage(BaseModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name="product_image")
    image = models.ImageField(upload_to="product")

# Create your models here.
