from django.contrib import admin
from .models import Department,Course,Person,Purpose,Choices
# Register your models here.



class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Department,DepartmentAdmin)

admin.site.register(Course)
admin.site.register(Person)
admin.site.register(Purpose)
admin.site.register(Choices)