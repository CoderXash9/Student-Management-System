from rest_framework import (
    serializers,
)  # importing django REST framework's serializer tools
from .models import Student, Course, Enrollment  # imports my models


class StudentSerializer(
    serializers.ModelSerializer
):  # creating serializer for the Student model
    class Meta:  # the serializer belongs to this model
        model = Student  # connects to my Student table
        fields = "__all__"  # include every field of Student


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"
