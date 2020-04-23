from rest_framework import serializers
from .Models import Product
class ProductSerialzer(serializers.Serializer):
    class Meta:
        model=Product
        fields=('name','dob','email','phno')