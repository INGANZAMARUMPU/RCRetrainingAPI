from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import timezone

class Personnel(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	tel = models.IntegerField()
	telW = models.IntegerField()
	fb = models.CharField(blank=True, max_length=60)
	tw = models.CharField(max_length=60, blank=True)
	insta = models.CharField(max_length=60, blank=True)
	profil = models.TextField()
	avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")


class Depot(models.Model):
	quartier = models.CharField(max_length=60)
	longitude = models.FloatField()
	latitude = models.FloatField()

	def __str__(self):
		return self.quartier

class Source(models.Model):
	quartier = models.CharField(max_length=60)
	longitude = models.FloatField()
	latitude = models.FloatField()
	is_valid = models.BooleanField(default=False)
	
	def __str__(self):
		return self.quartier


class Projet(models.Model):
	nom = models.CharField(max_length=60)
	description = models.TextField()
	date = models.DateField(default=True)

	def __str__(self):
		return self.quartier

class Trajet(models.Model):
	"""docstring for Trajet"""
	source = models.ForeignKey(Source, null=False, on_delete=models.CASCADE)
	destination = models.ForeignKey(Depot, null=False, on_delete=models.CASCADE)
	time = models.DateTimeField()

	def __str__(self):
		return self.quartier

class Produit(models.Model):
	"""docstring for Produit"""
	type_produit = models.CharField(max_length=60)
	quantite = models.FloatField()
	etat = models.CharField(max_length=60)
	source = models.ForeignKey(Source, null=False, on_delete=models.CASCADE)
		
		