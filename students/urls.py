from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewset, CourseViewset, EnrollmentViewset

router = DefaultRouter()

router.register(r"students", StudentViewset)
router.register(r"courses", CourseViewset)
router.register(r"enrollments", EnrollmentViewset)

urlpatterns = [
    path("", include(router.urls)),
]
