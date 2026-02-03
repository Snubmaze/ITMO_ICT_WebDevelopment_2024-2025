from rest_framework.viewsets import ModelViewSet
from core.models.teacher import Teacher
from core.serializers.teacher import TeacherSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
