#models/city.py
from django.db import models #Import base class from django stdlib


class City(models.Model):#must inherit from this base class
    name = models.CharField(max_length=155) #define all non-id fields

