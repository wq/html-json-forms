from rest_framework import viewsets
from .serializers import ParentSerializer
from .models import Parent


class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
