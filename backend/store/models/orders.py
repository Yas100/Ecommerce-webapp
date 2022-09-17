from django.db import models
from .product import Product
# from .customer import Customer
import datetime


class Order(models.Model):
    orderProduct = models.ForeignKey(Product,
                                 on_delete=models.CASCADE, related_name='orderProduct', null=True)
                                
    # OrderCustomer = models.ForeignKey(Customer,
    #                              on_delete=models.CASCADE, related_name='OrderCustomer', null=True)
    quantity = models.IntegerField(default=1)
    orderPrice = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # orderAddress = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orderAddress', null=True)

    # address = models.CharField(max_length=50, default='', blank=True)
    # phone = models.CharField(max_length=50, default='', blank=True)
    # orderMobileNumber = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orderMobileNumber', null=True)
    orderCreatedAt = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=False)

   