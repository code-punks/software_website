from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_location')
    list_select_related = ('profile', )

    def get_location(self, instance):
        return instance.profile.location
        
    get_location.short_description = 'Location'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

class EntryAdmin(admin.ModelAdmin):
    model = Entry
    list_display = ('user','entry_time','time','amount',)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Bill)
admin.site.register(Balance)
admin.site.register(Payment)
admin.site.register(Entry, EntryAdmin)