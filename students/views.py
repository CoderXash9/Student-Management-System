from rest_framework import viewsets
from .models import Student, Course, Enrollment
from .serializers import (
    StudentSerializer,
    CourseSerializer,
    EnrollmentSerializer,
)


class StudentViewset(
    viewsets.ModelViewSet
):  # automattically created all CRUD operations
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class EnrollmentViewset(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
