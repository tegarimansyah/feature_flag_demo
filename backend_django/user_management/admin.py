from django.contrib import admin
from django.contrib.auth.admin import User, UserAdmin

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'group', 'is_superuser')
    list_filter = ('is_superuser', 'groups')

    def group(self, obj):
        return obj.groups.first()


admin.site.unregister(User)
admin.site.register(User, UserAdmin)