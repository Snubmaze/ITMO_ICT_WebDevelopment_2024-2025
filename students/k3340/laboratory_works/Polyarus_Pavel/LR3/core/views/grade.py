from rest_framework.viewsets import ModelViewSet
from core.models.grade import Grade
from core.serializers.grade import GradeSerializer


class GradeViewSet(ModelViewSet):
    queryset = Grade.objects.select_related(
        'student',
        'subject'
    )
    serializer_class = GradeSerializer
