from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Product(models.Model):
    
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    createdTime=models.DateTimeField(auto_now_add=True)
    fields =['desc','price']
 
    def __str__(self):
           return self.desc
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now)

class Order(models.Model):
    amount = models.IntegerField(null=True)
    desc = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2,null=True)
# {'id': 9, 'amount': 2, 'desc': 'm', 'price': '2.00'}
    # class Meta:
    #     unique_together = ['user', 'product']

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'