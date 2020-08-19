from django.urls import path, include
import products.views as product_views


app_name = "products"
urlpatterns = [
    path('products/<str:prod_type>', product_views.ProductListView.as_view(),
         name="product"),
    path('products-detail/<int:pk>', product_views.ProdctDetailView.as_view(),
         name='product-detail'),

]