from .models import Portfolio
from rest_framework import viewsets, permissions
from .serializers import PropertySerializer


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = PropertySerializer
