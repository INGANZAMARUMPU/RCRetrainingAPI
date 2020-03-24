from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class PersonelSerializer(serializers.ModelSerializer):

    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    class Meta:
        model = Personnel
        fields = ["id","telephone", "whatsapp_number", "facebook_account",\
                "tweeter_account", "instagram_account", "profile", "detail", \
                "avatar", "is_environmentalist", "first_name", "last_name", "email"]

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_email(self, obj):
        return obj.user.email

class DepotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Depot
        fields = "__all__"

class SourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Source
        fields = "__all__"

class TrajetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trajet
        fields = "__all__"

class ProduitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produit
        fields = "__all__"

class TokenPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        data['email'] = self.user.email
        try:
            data['photo'] = self.user.personnel.avatar.url
        except:
            data['photo'] = ""
        return data