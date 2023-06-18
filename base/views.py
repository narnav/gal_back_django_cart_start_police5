from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product,Order
from rest_framework.views import APIView
from rest_framework import status

from rest_framework import serializers
from .models import Cart
from rest_framework import generics

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields =  ['__all__']#, 'user', 'product', 'quantity', 'created_at']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields =  ['amount', 'desc', 'price']
    def create(self, validated_data):
        # return Order.objects.create(**validated_data)
        user = self.context['user']
        return Order.objects.create(**validated_data,user=user)

class CartView(APIView):
    
    permission_classes = [IsAuthenticated]
    def post(self, request):
        cart_items = request.data
        print(cart_items)
        serializer = CartItemSerializer(data=request.data, many=True, context={'user': request.user})
        if serializer.is_valid():
            cart_items = serializer.save()
        #     # Process the cart items as needed
        #     # ...
            return Response("Cart items received and processed successfully.")
        else:
            return Response(serializer.errors, status=400)


class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


@api_view(['post'])
@permission_classes([IsAuthenticated])
def buy(req):
    cart_items = req.data
    print(cart_items)
    return Response("about")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def about(req):
    return Response("about")


@api_view(['GET'])
def contact(req):
    return Response("contact")


# register
@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
    user.is_active = True
    user.is_staff = False
    user.save()
    return Response("new user born")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductView(APIView):
    def get(self, request):
        my_model = Product.objects.all()
        serializer = ProductSerializer(my_model, many=True)
        return Response(serializer.data)


    def post(self, request):
        # usr =request.user
        # print(usr)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def put(self, request, pk):
        my_model = Product.objects.get(pk=pk)
        serializer = ProductSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request, pk):
        my_model = Product.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




