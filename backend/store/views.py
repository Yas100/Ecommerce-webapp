from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from .models.customer import Customer
from .models.category import Category
from .models.orders import Order
from .models.product import  Product
from .serislizers import CustomerSerializers, ProductSerializers, CategorySerializers, OrderSerializers

from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CustomerViewSet(ModelViewSet):
        queryset = Customer.objects.all()
        serializer_class = CustomerSerializers

class ProductViewSet(ModelViewSet):
        queryset = Product.objects.all()
        serializer_class = ProductSerializers
        permission_classes = []

class OrderViewSet(ModelViewSet):
        queryset = Order.objects.all()
        serializer_class = OrderSerializers
        permission_classes = [IsAuthenticated]

class CategoryViewSet(ModelViewSet):
        queryset = Category.objects.all()
        serializer_class = CategorySerializers
        permission_classes = [IsAdminUser]


