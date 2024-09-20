from django.contrib import admin
from .models import data

class MemberAdmin(admin.ModelAdmin):
    list_display=("name","email","number","message",)

admin.site.register(data,MemberAdmin)