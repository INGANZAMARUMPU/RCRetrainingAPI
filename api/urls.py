from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register('personnels', PersonelViewset)
router.register('depots', DepotViewset)
router.register('sources', SourceViewset)
router.register('trajets', TrajetViewset)
router.register('produits', ProduitViewset)

urlpatterns = [
    path('', include(router.urls)),
]