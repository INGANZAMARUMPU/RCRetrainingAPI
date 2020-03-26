from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import SessionAuthentication

from .serializers import * 
from .models import *


class PersonelViewset(viewsets.ModelViewSet):
	queryset = Personnel.objects.all()
	serializer_class = PersonelSerializer
	authentication_classes = [SessionAuthentication, JWTAuthentication]
	permission_classes = (IsAuthenticatedOrReadOnly,)

	def list(self, request, *args, **kwargs):
		queryset = Personnel.objects.filter(is_environmentalist=True)
		serializer = PersonelSerializer(queryset, many=True)
		return Response(serializer.data)

class DepotViewset(viewsets.ModelViewSet):
	queryset = Depot.objects.all()
	serializer_class = DepotSerializer
	authentication_classes = [SessionAuthentication, JWTAuthentication]
	permission_classes = (IsAuthenticatedOrReadOnly,)

class SourceViewset(viewsets.ModelViewSet):
	queryset = Source.objects.all()
	serializer_class = SourceSerializer
	authentication_classes = [SessionAuthentication, JWTAuthentication]
	permission_classes = (IsAuthenticatedOrReadOnly,)

class TrajetViewset(viewsets.ModelViewSet):
	queryset = Trajet.objects.all()
	serializer_class = TrajetSerializer
	authentication_classes = [SessionAuthentication, JWTAuthentication]
	permission_classes = (IsAuthenticatedOrReadOnly,)

class ProduitViewset(viewsets.ModelViewSet):
	queryset = Produit.objects.all()
	serializer_class = ProduitSerializer
	authentication_classes = [SessionAuthentication, JWTAuthentication]
	permission_classes = (IsAuthenticatedOrReadOnly,)

class TokenPairView(TokenObtainPairView):
	serializer_class = TokenPairSerializer

@csrf_exempt
@api_view(["POST",])   
def register(request):
	try:
		data = request.data
		user = User(
			username = data["telephone"],
			first_name = data.pop("first_name"),
			last_name = data.pop("last_name")
		)
		user.email = data.pop("email")
		user.set_password(data.pop("password"))
		user.save()
		tokens = RefreshToken.for_user(user)
		Personnel(
			user = user,**data
		).save()
		response = {}
		response['first_name'] = user.first_name
		response['last_name'] = user.last_name
		response['email'] = user.email
		response['photo'] = ""
		response['access'] = str(tokens.access_token)
		response['refresh'] = str(tokens)
		return Response(response, status=status.HTTP_200_OK)
	except Exception as e:
		return Response({"detail":str(e)}, status=status.HTTP_400_BAD_REQUEST)
