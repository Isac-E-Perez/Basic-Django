from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Product(models.Model): 
    name = models.CharField(max_length=220) # A string field, for small to large sized strings 
    date = models.DateTimeField(auto_now_add=True) # a combination of a date and a time

    def __str__(self):
        return str(self.name) 

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # When an object referenced by a ForeignKey is deleted, Django will 
    # emulate the behavior of the SQL constraint specified by the on_delete argument  
    
    price = models.PositiveIntegerField() # the integer must be positive or zero 
    quantity = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField(blank=True) # if True, the field is allowed to be blank 
    salesman = models.ForeignKey(User, on_delete=models.CASCADE) 
    date = models.DateTimeField(default=timezone.now) 

    # overide the save method
    def save(self, *args, **kwargs):
        self.total_price = self.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return "Sold {} - {} items for ${}".format(self.product.name, self.quantity, self.total_price)  
