from django.urls import path
from crm.views import (add_product_view, update_availability_view,\
    image_upload_view)


app_name = "crm"
urlpatterns = [
    path('add_product/', add_product_view, name="add_product"),
    path('edit_availability/<int:product_id>',
         update_availability_view, name="edit_availability"),
    path('upload_image/<int:product_id>', image_upload_view,
         name='upload_image')
]
