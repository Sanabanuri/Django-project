from django.contrib import admin
from .models import Student, Teacher, Course, Enrollment


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "date_of_birth", "phone", "created_at")
    search_fields = ("name", "email")
    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "specialization", "created_at")
    search_fields = ("name", "email", "specialization")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "teacher", "created_at")
    search_fields = ("name", "description")


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "enrolled_at")
    search_fields = ("student__name", "course__name")