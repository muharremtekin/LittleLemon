from django.urls import path
from .views import CategoryListCreate, MenuItemListCreate, MenuItemDetail, CartListCreate, CartDetail, OrderListCreate, OrderDetail, OrderItemListCreate, OrderItemDetail

urlpatterns = [
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('menu-items/', MenuItemListCreate.as_view(), name='menuitem-list-create'),
    path('menu-items/<int:pk>/', MenuItemDetail.as_view(), name='menuitem-detail'),
    path('cart/', CartListCreate.as_view(), name='cart-list-create'),
    path('cart/<int:pk>/', CartDetail.as_view(), name='cart-detail'),
    path('orders/', OrderListCreate.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('order-items/', OrderItemListCreate.as_view(), name='orderitem-list-create'),
    path('order-items/<int:pk>/', OrderItemDetail.as_view(), name='orderitem-detail'),
]