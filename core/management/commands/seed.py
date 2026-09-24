from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "Seed initial data"

    def handle(self, *args, **kwargs):
        teacher_group, _ = Group.objects.get_or_create(name="Teacher")
        student_group, _ = Group.objects.get_or_create(name="Student")

        course_permissions = Permission.objects.filter(
            content_type__app_label="core",
            content_type__model="course",
        )

        teacher_group.permissions.set(course_permissions)

        student_permissions = Permission.objects.filter(
            content_type__app_label="core",
            content_type__model__in=["student", "course", "enrollment"],
            codename__startswith="view_",
        )

        student_group.permissions.set(student_permissions)

        self.stdout.write(
            self.style.SUCCESS(
                "Teacher and Student groups created successfully!"
            )
        )