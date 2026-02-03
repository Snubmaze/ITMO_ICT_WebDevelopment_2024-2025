from django.urls import path
from .views import ClassPerformanceReportAPIView


urlpatterns = [
    path(
        'reports/',
        ClassPerformanceReportAPIView.as_view(),
        name='class-performance-report'
    )
]
