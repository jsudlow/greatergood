from django.contrib import admin

# Register your models here.

from .models import Client,SiteInformation
admin.site.register(Client)
admin.site.register(SiteInformation)
