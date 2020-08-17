from django.urls import path, include
import web_shop.views as shop_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', shop_views.HomeView.as_view(), name="home"),
    path('products/<str:prod_type>', shop_views.ProductListView.as_view(),
         name="product"),
    path('contact/', shop_views.ContactView.as_view(), name="contact"),
    path('products-detail/<int:pk>', shop_views.ProdctDetailView.as_view(),
         name='product-detail'),
    path('accounts/register', shop_views.RegisterView.as_view(),
         name="register"),
    path('accounts/profile/', shop_views.ProfileView.as_view(), name="profile")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)