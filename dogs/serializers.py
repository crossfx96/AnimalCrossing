from rest_framework import serializers
from .models import AnimalType, Breed, Animal, Exhibition, Reward


class AnimalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalType
        fields = '__all__'


class BreedSerializer(serializers.ModelSerializer):
    animal_type = AnimalTypeSerializer(read_only=True)

    class Meta:
        model = Breed
        fields = '__all__'


class AnimalSerializer(serializers.ModelSerializer):
    breed = BreedSerializer(read_only=True)

    class Meta:
        model = Animal
        fields = '__all__'


class ExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibition
        fields = '__all__'


class RewardSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(many=True, read_only=True)
    exhibition = ExhibitionSerializer(read_only=True)

    class Meta:
        model = Reward
        fields = '__all__'
