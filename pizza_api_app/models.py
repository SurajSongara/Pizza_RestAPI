from django.db import models

class Pizza(models.Model):
    TYPE_CHOICES=(
        ('Regular','Regular'),
        ('Square','Square')
    )

  
    type=models.CharField(max_length=10,choices=TYPE_CHOICES)
    size=models.CharField(max_length=20)
    topping = models.CharField(max_length=20)

