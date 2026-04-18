from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to="images/", null = True, blank=True)

    def __str__(self):
        return self.name

