from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
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