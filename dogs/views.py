
from rest_framework import viewsets, permissions
from rest_framework.generics import get_object_or_404
from .serializers import AnimalTypeSerializer, BreedSerializer, AnimalSerializer, \
    RewardSerializer, ExhibitionSerializer
from dogs.models import AnimalType, Breed, Animal, Reward, Exhibition


class AnimalTypeView(viewsets.ModelViewSet):
    serializer_class = AnimalTypeSerializer
    queryset = AnimalType.objects.all()


class BreedView(viewsets.ModelViewSet):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        animal_type = get_object_or_404(AnimalType, id=self.request.data.get('animal_type'))
        return serializer.save(animal_type=animal_type)


class AnimalViews(viewsets.ModelViewSet):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()

    def perform_create(self, serializer):
        breed = get_object_or_404(Breed, id=self.request.data.get('breed'))
        return serializer.save(breed=breed)


class RewardViews(viewsets.ModelViewSet):
    serializer_class = RewardSerializer
    queryset = Reward.objects.all()


class ExhibitionViews(viewsets.ModelViewSet):
    serializer_class = ExhibitionSerializer
    queryset = Exhibition.objects.all()
