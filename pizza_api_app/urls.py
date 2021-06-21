
from django.urls import path
from .views import *

urlpatterns = [
    path('add_pizza/',add_pizza),
    path('pizza/',show_pizza),
    path('pizza_detail/<int:pk>/',update_pizza),
    path('pizza_update/<int:pk>',update_pizza)
]
