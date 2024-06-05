# admin.py
from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)  # Enable search by 'name'

admin.site.register(Contact, ContactAdmin)
