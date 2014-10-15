# encoding: utf-8
from django.contrib import admin
from caed.models import Student, StudentClass, Incident, IncidentType
from django.shortcuts import render_to_response


# Register your models here.
class IncidentAdmin(admin.ModelAdmin):
    actions = ['print_report']
    exclude = ('student_class',)
    list_display = ('student','student_class','title','type','archived')
    list_filter = ('student_class','type__title','date_time','archived')
    raw_id_fields = ('student',)
    
    def print_report(self,request,queryset):
        queryset.update(archived=True)
        return render_to_response('report.html',{'incidents': queryset})        
    
    print_report.short_description = "Imprimir relatório"

    
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','student_class','mother_name')
    list_filter = ('student_class',)
    
admin.site.register(Student,StudentAdmin)
admin.site.register(StudentClass)
admin.site.register(Incident,IncidentAdmin)
admin.site.register(IncidentType)
