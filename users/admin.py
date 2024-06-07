from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.utils.translation import gettext_lazy as _
from users.models import SongShareUser, SongShareUserGroup


class SongShareUserAdmin(UserAdmin):
    # How the SongShareUserAdmin model is displayed in the admin interface
    list_display = ('username', 'email', 'phone_number', 'first_name',
                    'is_staff', 'created_at')
    list_filter = ('user_type', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'user_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Activity Dates', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'user_type'),
        }),
    )


admin.site.site_title = "SongShareAPI Admin"
admin.site.site_header = "User Admin"
admin.site.index_title = "Site administration"

admin.site.register(SongShareUser, SongShareUserAdmin)
admin.site.unregister(Group)


@admin.register(SongShareUserGroup)
class SongShareGroupAdmin(GroupAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'permissions')}),
        (_('Description'), {'fields': ('description',)}),
    )
