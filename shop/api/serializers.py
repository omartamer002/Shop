from .models import Product
from rest_framework.serializers import ModelSerializer

class ProductSerializer(ModelSerializer):
  class Meta:
    model = Product
    fields = '__all__'

class VendorSerializer(ModelSerializer):
  class Meta:
    model = Vendor
    fields = '__all__'

class ReviewSerializer(ModelSerializer):
  class Meta:
    model = Review
    fields = '__all__'