from django.contrib import admin

# Register your models here.
from .models import AnimalType, Reward, Breed, Exhibition, Animal

admin.site.register(AnimalType)
admin.site.register(Reward)
admin.site.register(Animal)
admin.site.register(Breed)
admin.site.register(Exhibition)
