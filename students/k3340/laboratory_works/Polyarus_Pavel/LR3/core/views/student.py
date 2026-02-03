from rest_framework.viewsets import ModelViewSet
from core.models.student import Student
from core.serializers.student import StudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.select_related('school_class')
    serializer_class = StudentSerializer

    
