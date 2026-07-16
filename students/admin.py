from django.contrib import admin
from .models import Student , Course , Enrollment

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "phone",
        "gender",
    )

    search_fields = (
        "first_name",
        "last_name",
        "email",
    )

    list_filter = (
        "gender",
    )

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "course_name",
        "course_code",
        "credits",
    )

    search_fields = (
        "course_name",
        "course_code",
    )

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "student",
        "course",
        "status",
        "enrollment_date",
    )

    list_filter = (
        "status",
    )


