from django.contrib import admin
from .models import Food, Consume, FoodManage

# Register your models here.
admin.site.register(Food)
admin.site.register(Consume)
admin.site.register(FoodManage)
