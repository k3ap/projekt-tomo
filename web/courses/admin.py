from django.contrib import admin
from .models import Course, ProblemSet, StudentEnrollment, Group, AddAMember


class StudentEnrollmentInline(admin.StackedInline):
    model = StudentEnrollment

class AddAMemberInline(admin.StackedInline):
    model = AddAMember


class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = (
        'teachers',
        'students',
    )
    inlines = (
        StudentEnrollmentInline,
    )


class ProblemSetAdmin(admin.ModelAdmin):
    list_display = (
        'course',
        'title',
    )
    list_display_links = (
        'title',
    )
    list_filter = (
        'course',
    )
    ordering = (
        'course',
        '_order',
    )
    search_fields = (
        'title',
        'description',
    )

class GroupAdmin(admin.ModelAdmin):
    list_display = ['title']
    filter_horizontal = (
        'members',
    )
    inlines = (
        AddAMemberInline,
    )

admin.site.register(Course, CourseAdmin)
admin.site.register(ProblemSet, ProblemSetAdmin)
admin.site.register(Group, GroupAdmin)
