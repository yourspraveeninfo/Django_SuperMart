from django.urls import path
from .views import *

urlpatterns = [
    path('all/customers/', CustomersList),
    path('add/customers/', CustomersAdd),
    path('update/customer/<int:id>', CustomerUpdate, name='customer_update'),
    path('delete/customer/<int:id>', CustomersDelete, name='customer_delete'),

    path('add/orders/',OrdersAdd),
    path('orders/',OrdersList),
    path('delete/order/<int:id>',OrdersDelete, name='order_delete'),
    path('update/order/<int:id>',OrdersUpdate, name='order_update'),
]