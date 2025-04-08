

from django.contrib import admin

# Register your models here.
from .models import College, Program, Organization, Student, OrgMember

admin.site.register(College)
admin.site.register(Program)
admin.site.register(Organization)
admin.register(Student)
admin.register(OrgMember)
