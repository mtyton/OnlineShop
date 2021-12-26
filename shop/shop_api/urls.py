from django.urls import path
from rest_framework.routers import DefaultRouter

from shop_api.views import products as products_views


router = DefaultRouter()

router.register(
    "category", products_views.CategoryModelViewSet, basename="category"
)

urlpatterns = [

] + router.urls
