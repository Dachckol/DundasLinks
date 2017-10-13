from django.contrib import admin
from contact.models import Type, ContactEntry

class ContactEntryAdmin(admin.ModelAdmin):
	list_display= ("name", "contentType", "answered")
	list_filter = ("answered", "contentType")

admin.site.register(Type)
admin.site.register(ContactEntry, ContactEntryAdmin)
