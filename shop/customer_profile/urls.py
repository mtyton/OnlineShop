from django.urls import path, include
import customer_profile.views as customer_views


app_name = "customer_profile"
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', customer_views.RegisterView.as_view(), name="register"),
    path('contact/', customer_views.ContactView.as_view(), name="contact"),
    path('accounts/profile/',
         customer_views.profile_view, name="profile"),

]