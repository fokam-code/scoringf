from django.contrib import admin
from .models import Client,Testdata,pret,Donnee
# Register your models here.
admin.site.register(Client)
admin.site.register(Testdata)
admin.site.register(pret)
admin.site.register(Donnee)
