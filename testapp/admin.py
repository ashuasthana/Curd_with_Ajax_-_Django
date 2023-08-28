from django.contrib import admin
from .models import StudentRagistration
# Register your models here.
@admin.register(StudentRagistration)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','email','password']

