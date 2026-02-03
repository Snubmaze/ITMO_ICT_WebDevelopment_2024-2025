from rest_framework import serializers


class SubjectPerfomanceSerializer(serializers.Serializer):
    subject = serializers.CharField()
    average = serializers.FloatField()


class ClassReportSerializer(serializers.Serializer):
    school_class = serializers.CharField
    students_count = serializers.IntegerField()
    class_teacher = serializers.CharField()
    class_average = serializers.FloatField()
    subjects = SubjectPerfomanceSerializer(many=True)