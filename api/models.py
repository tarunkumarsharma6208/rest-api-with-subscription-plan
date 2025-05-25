from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
    
class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    limit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name}"

class Subscription(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    api_limit = models.PositiveIntegerField(default=100)  # e.g. 100 hits
    api_usage = models.PositiveIntegerField(default=0)    # count of used hits
    is_expire = models.BooleanField(default=False)

    

    def increment_usage(self):
        self.api_usage += 1
        if self.api_usage == self.api_limit:
            self.is_expire = True
        self.save()

    def has_hits_left(self):
        return self.api_usage < self.api_limit
