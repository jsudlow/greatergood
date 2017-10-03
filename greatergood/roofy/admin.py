from django.contrib import admin

# Register your models here.

from .models import Client,Project,Note



class ProjectAdmin(admin.ModelAdmin):
    
    list_display = ('status', 'client', 'sales_rep','site_address','city','state')


admin.site.register(Client)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Note)



