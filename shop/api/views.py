from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer, VendorSerializer
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class ProductList(APIView):
  def get(self, request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
  
class ProductDetail(APIView):
  def get(self, request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
  
  def put(self, request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=400)
  
  def delete(self, request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response(status=204)

class VendorList(generics.ListCreateAPIView):
  queryset = Vendor.objects.all()
  serializer_class = VendorSerializer

class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Vendor.objects.all()
  serializer_class = VendorSerializer

class ReviewViewSet(ModelViewSet):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer