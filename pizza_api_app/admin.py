from django.contrib import admin

from .models import Pizza

class ModelPizza(admin.ModelAdmin):
    list_display=['type','size','topping']

admin.site.register(Pizza,ModelPizza)




# Register your models here.
