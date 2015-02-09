from django.contrib import admin

# Register your models here.
from support_user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'phone', 'alt_phone',)
    list_filter = ('first_name', 'last_name', 'username', 'email', 'is_staff',)


admin.site.register(User, UserAdmin)


