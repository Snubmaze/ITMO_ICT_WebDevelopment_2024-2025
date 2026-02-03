from rest_framework.viewsets import ModelViewSet
from core.models.classroom import Classroom
from core.serializers.classroom import ClassroomSerializer


class ClassroomViewSet(ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
