from rest_framework import serializers
from .models import *

class PersonelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Personnel
        fields = "__all__"
        depth = 1

class DepotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Depot
        fields = "__all__"

class SourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Source
        fields = "__all__"

class ProjetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projet
        fields = "__all__"

class TrajetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trajet
        fields = "__all__"

class ProduitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produit
        fields = "__all__"
