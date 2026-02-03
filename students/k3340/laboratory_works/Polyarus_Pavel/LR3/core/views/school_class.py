from rest_framework.viewsets import ModelViewSet
from core.models.school_class import SchoolClass
from core.serializers.school_class import SchoolClassSerializer


class SchoolClassViewSet(ModelViewSet):
    queryset = SchoolClass.objects.select_related('class_teacher')
    serializer_class = SchoolClassSerializer
