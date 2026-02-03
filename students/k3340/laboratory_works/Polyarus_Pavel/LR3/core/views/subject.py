from rest_framework.viewsets import ModelViewSet
from core.models.subject import Subject
from core.serializers.subject import SubjectSerializer


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
