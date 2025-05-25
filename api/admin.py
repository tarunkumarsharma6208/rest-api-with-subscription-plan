from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(Category)
admin.site.register(Product)



@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'api_limit', 'api_usage', 'is_expire']


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'limit', 'price']