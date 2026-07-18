from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Student, Course, Enrollment
from .serializers import (
    StudentSerializer,
    CourseSerializer,
    EnrollmentSerializer,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Students"])
class StudentViewset(
    viewsets.ModelViewSet
):  # automattically created all CRUD operations
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["first_name", "last_name", "email"]
    ordering_fields = ["first_name", "created_at"]

    filterset_fields = ["gender"]

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


@extend_schema(tags=["Courses"])
class CourseViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


@extend_schema(tags=["Enrollments"])
class EnrollmentViewset(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
