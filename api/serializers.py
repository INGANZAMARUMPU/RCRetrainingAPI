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

# class AccountSerializer(serializers.Serializer):
#     email = serializers.CharField(required=True, allow_blank=False)
#     first_name = serializers.CharField(required=True, allow_blank=False)
#     last_name = serializers.CharField(required=True, allow_blank=False)
#     telephone = serializers.IntegerField(required=True, allow_blank=False)
#     whatsapp_number = serializers.IntegerField(required=False, allow_blank=True)
#     facebook_account = serializers.IntegerField(required=False, allow_blank=True)
#     tweeter_account = serializers.IntegerField(required=False, allow_blank=True)
#     instagram_account = serializers.IntegerField(required=False, allow_blank=True)
#     profile = serializers.CharField(required=True, allow_blank=False)
#     detail = serializers.CharField(required=False, allow_blank=True)
#     avatar = serializers.ImageField(required=False, allow_blank=True)

#     def create(self, validated_data):
#         user = models.User(
#             username = validated_data["telephone"],
#             email = validated_data["email"],
#             first_name = validated_data["first_name"],
#             last_name = validated_data["last_name"]
#         )
#         user.set_password(validated_data["password"])
#         user.save()
#         tokens = RefreshToken.for_user(user)
#         Personnel(
#             user = user,
#             telephone = validated_data["telephone"],
#             whatsapp_number = validated_data["whatsapp_number"],
#             facebook_account = validated_data["facebook_account"],
#             tweeter_account = validated_data["tweeter_account"],
#             instagram_account = validated_data["instagram_account"],
#             profile = validated_data["profile"],
#             detail = validated_data["detail"],
#             avatar = validated_data["avatar"]
#         ).save()
#         response = {}
#         response['first_name'] = user.first_name
#         response['last_name'] = user.last_name
#         response['email'] = user.email
#         response['photo'] = ""
#         response['access'] = str(tokens.access_token)
#         response['refresh'] = str(tokens)
#         return Response(response, status=status.HTTP_200_OK)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance