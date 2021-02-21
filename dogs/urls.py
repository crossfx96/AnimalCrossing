from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from dogs.views import AnimalViews, AnimalTypeView, BreedView, RewardViews, ExhibitionViews
router = DefaultRouter()
router.register(r'animal_types', AnimalTypeView)
router.register(r'breed', BreedView)
router.register(r'animals', AnimalViews)
router.register(r'reward', RewardViews)
router.register(r'exhibition', ExhibitionViews)

urlpatterns = [
    path('', include(router.urls)),
]
