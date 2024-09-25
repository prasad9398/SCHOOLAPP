from django.contrib import admin
from admission.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','fathername','classname','contact']

# Register your models here.
admin.site.register(Student,StudentAdmin)
