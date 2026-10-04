from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Student, Teacher, Course, Enrollment


class SMSAdminSite(AdminSite):
    site_header = "Student Management System"
    site_title = "SMS Admin"
    index_title = "Dashboard"

    def index(self, request, extra_context=None):
        extra_context = extra_context or {}

        extra_context.update({
            "total_students": Student.objects.count(),
            "total_teachers": Teacher.objects.count(),
            "total_courses": Course.objects.count(),
            "total_enrollments": Enrollment.objects.count(),
        })

        return super().index(request, extra_context=extra_context)


admin_site = SMSAdminSite(name="sms_admin")


@admin.register(Student, site=admin_site)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "date_of_birth", "phone", "created_at")
    search_fields = ("name", "email")


@admin.register(Teacher, site=admin_site)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "specialization", "created_at")
    search_fields = ("name", "email", "specialization")


@admin.register(Course, site=admin_site)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "teacher", "created_at")
    search_fields = ("name", "description")


@admin.register(Enrollment, site=admin_site)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "enrolled_at")
    search_fields = ("student__name", "course__name")
    list_filter = ("student", "course")