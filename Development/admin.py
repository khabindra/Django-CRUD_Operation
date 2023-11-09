from django.contrib import admin
from .models import Contact, Courses, Student

admin.site.site_header = 'हावा सफ्टवेयर कम्पनी'
admin.site.site_title = 'Development'

from .models import Student,Courses,Contact
# Register your models here.
admin.site.register([Courses])
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','gmail']
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','phone_number','email','course','image','message']