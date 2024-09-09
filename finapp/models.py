from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=30)
    loan_amount = models.IntegerField()
    paid_amount = models.IntegerField(null=True, blank=True)
    join_date = models.DateField(auto_now_add=True)
    loan_history = models.JSONField(default=dict)
