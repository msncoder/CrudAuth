from django.urls import path
from . import views
urlpatterns = [
   path("",views.dashboard,name="dashboard"),
   path("product/",views.create_product,name="product"),
   path("update_product/<int:id>/",views.update_product,name="update_product"),
   path("delete_product/<int:id>/",views.delete_product,name="delete_product"),

   path("create_customer/",views.create_customer,name="create_customer"),
   path("customer/<int:id>/",views.customer_view,name="customer_url"),
   path("update_customer/<int:id>/",views.update_customer,name="update_customer"),
   path("customer_delete/<int:id>/",views.delete_customer,name="customer_delete"),

   path("createorder/",views.create_order,name="createorder"),
   path("updateorder/<int:id>/",views.update_order,name="updateorder"),
   path("order_delete/<int:id>/",views.delete_order,name="order_delete"),

   path("createtag/",views.create_tags,name="createtag"),
   path("update_tag/<int:id>/",views.update_tag,name="update_tag"),
   path("delete_tag/<int:id>/",views.delete_tag,name="delete_tag"),
]
