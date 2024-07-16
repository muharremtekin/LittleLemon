from rest_framework import generics, permissions
from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import CategorySerializer, MenuItemSerializer, CartSerializer, OrderSerializer, OrderItemSerializer
from .permissions import IsAdminUser, IsManager, IsDeliveryCrew, IsCustomer

# Category Views
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [permissions.AllowAny]
        return super(CategoryListCreate, self).get_permissions()

# MenuItem Views
class MenuItemListCreate(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [permissions.AllowAny]
        return super(MenuItemListCreate, self).get_permissions()

class MenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH']:
            self.permission_classes = [IsManager]
        else:
            self.permission_classes = [permissions.AllowAny]
        return super(MenuItemDetail, self).get_permissions()

# Cart Views
class CartListCreate(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsCustomer]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsCustomer]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

# Order Views
class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsCustomer]
        else:
            self.permission_classes = [permissions.AllowAny]
        return super(OrderListCreate, self).get_permissions()

    def get_queryset(self):
        if self.request.user.groups.filter(name='Delivery Crew').exists():
            return self.queryset.filter(assigned_to=self.request.user)
        return self.queryset.filter(user=self.request.user)

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH']:
            self.permission_classes = [IsManager]
        else:
            self.permission_classes = [permissions.AllowAny]
        return super(OrderDetail, self).get_permissions()

    def get_queryset(self):
        if self.request.user.groups.filter(name='Delivery Crew').exists():
            return self.queryset.filter(assigned_to=self.request.user)
        return self.queryset.filter(user=self.request.user)

# OrderItem Views
class OrderItemListCreate(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsManager]
        else:
            self.permission_classes = [permissions.AllowAny]
        return super(OrderItemListCreate, self).get_permissions()

class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH']:
            self.permission_classes = [IsManager]
        else:
            self.permission_classes = [permissions.AllowAny]
        return super(OrderItemDetail, self).get_permissions()

