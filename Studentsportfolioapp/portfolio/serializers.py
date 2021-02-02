from rest_framework import serializers
from .models import Portfolio


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        property = '__all__'
        fields = '__all__'
