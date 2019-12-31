from django.contrib import admin

from .models import Event, Catagory, Organizer, Update


# Register your models here.

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'event_slug': ('name',)}


class CatagoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Event, EventAdmin)
admin.site.register(Catagory, CatagoryAdmin)
admin.site.register(Organizer)
admin.site.register(Update)
