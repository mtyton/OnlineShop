from django.urls import path
import web_shop.views as web_shop_views


urlpatterns = [
    path(
        'home/', web_shop_views.HomeView.as_view(), name="home"
    )
]
