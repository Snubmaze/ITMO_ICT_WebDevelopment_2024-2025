from django.db.models import Avg
from rest_framework.views import APIView, status
from rest_framework.response import Response

from core.models import SchoolClass, Grade
from .serializers import ClassReportSerializer


class ClassPerformanceReportAPIView(APIView):
    def get(self, request):
        class_id = request.query_params.get('class_id')
        quarter = request.query_params.get('quarter')

        if not class_id or not quarter:
            return Response(
                {'detail': 'class_id и quarter обязательны'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            school_class = SchoolClass.objects.select_related('class_teacher').get(id=class_id)

        except SchoolClass.DoesNotExist:
            return Response(
                {'detail': 'Класс не найден'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        grades = Grade.objects.filter(student__school_class=school_class, quarter=quarter)

        subject_stats = (
            grades.values('subject__name').annotate(average=Avg('value'))
        )
        
        class_average = grades.aggregate(avg=Avg('value'))['avg']

        data = {
            'class': f'{school_class.grade}{school_class.letter}',
            'class_teacher': str(school_class.class_teacher),
            'students_count': school_class.students.count(),
            'class_average': round(class_average, 2) if class_average else None,
            'subjects': [
                {
                    'subject': s['subject__name'],
                    'average': round(s['average'], 2)
                }

                for s in subject_stats
            ]

        }
        serializer = ClassReportSerializer(data)
        return Response(serializer.data)



