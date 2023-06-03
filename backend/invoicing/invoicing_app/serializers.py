from rest_framework import serializers
from .models import *

class ItemSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Item
        fields = "__all__"
        
class InvoiceSerializer(serializers.ModelSerializer): 
    items =  ItemSerializer(many=True)
    class Meta:
        model = Invoice
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

