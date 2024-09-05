from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    loan_amount = models.IntegerField()
    paid_amount = models.IntegerField(null=True, blank=True)
    join_date = models.DateField(auto_now_add=True)
