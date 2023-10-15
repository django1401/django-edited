from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomeUser, Profile

class CustomeUserAdmin(UserAdmin):

    model = CustomeUser
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser', 'is_verified')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('username', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',)}),
            ('Permissions', {
                'classes': ('collapse',),
                'fields': ('username', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )


class CustomeProfileAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'mobile', 'id_code')
    list_filter = ('user',)
    search_fields = ('id_code',)
    ordering = ('user',)

    fieldsets = (
        ('Basic data', {'fields': ('user','mobile', 'id_code')}),
        ('Others', {'fields': ('first_name', 'last_name', 'address', 'image')}),
    )

    add_fieldsets = (
        ('Basic data', {'fields': ('user','mobile', 'id_code')}),
        ('Others', {
            'classes': ('collapse',),
            'fields': ('first_name', 'last_name', 'address', 'image')}),
    )



admin.site.register(CustomeUser, CustomeUserAdmin)
admin.site.register(Profile, CustomeProfileAdmin)
