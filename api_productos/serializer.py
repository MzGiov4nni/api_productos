from rest_framework import serializers
from .models import producto

class Productos_Serializer(serializers.ModelSerializer):
    class Meta:
        model=producto
        fields='__all__'