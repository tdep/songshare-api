from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseUserAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "is_staff",
        "email",
        "phone_number",
    ]
    readonly_fields = ["username"]


admin.site.register(User, UserAdmin)


# TODO: Build admin
# TODO: Set user permissions

# TODO: Create mock database

# TODO: Write tests
# TODO: Test in postman
