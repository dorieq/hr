from django.contrib import admin
from .models import ApplicationStatus, Employee, ExpertCommission, Policy, Position, Department, Location

admin.site.register(ApplicationStatus)
admin.site.register(Employee)
admin.site.register(ExpertCommission)
admin.site.register(Policy)
admin.site.register(Position)
admin.site.register(Department)
admin.site.register(Location)