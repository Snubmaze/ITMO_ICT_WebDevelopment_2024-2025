from rest_framework.viewsets import ModelViewSet
from core.models.timeslot import TimeSlot
from core.serializers.timeslot import TimeSlotSerializer


class TimeSlotViewSet(ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer
