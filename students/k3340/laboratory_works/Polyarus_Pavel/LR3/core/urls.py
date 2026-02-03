from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('subjects', SubjectViewSet)
router.register('weekdays', WeekDayViewSet)
router.register('timeslots', TimeSlotViewSet)
router.register('classrooms', ClassroomViewSet)
router.register('teachers', TeacherViewSet)
router.register('classes', SchoolClassViewSet)
router.register('students', StudentViewSet)
router.register('grades', GradeViewSet)

router.register(
    r'schedule',
    ScheduleViewSet,
    basename='schedule'
)

urlpatterns = router.urls
