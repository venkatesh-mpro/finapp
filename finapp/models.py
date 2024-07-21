from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    total_amount = models.IntegerField()
    paid_amount = models.IntegerField()
    join_date = models.DateField()
