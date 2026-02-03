from rest_framework import serializers
from core.models.weekday import WeekDay


class WeekDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekDay
        fields = '__all__'