from django.urls import path, include
import products.views as product_views


app_name = "products"
urlpatterns = [
    path('products/<str:category_type>/<int:page>',
         product_views.ProductListView.as_view(), name="products"),
    path('products-detail/<int:pk>', product_views.ProdctDetailView.as_view(),
         name='product-detail')
]