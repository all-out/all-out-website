from django.contrib import admin
from django.contrib.auth import get_user_model

from profile.models import Character
from profile.forms import UserModelForm

# admin.site.register(UserAdmin)
admin.site.register(Character)

# admin.site.register(get_user_model())


# admin.site.unregister(get_user_model())
@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):

    form = UserModelForm

    fieldsets = (
        ('Authentication', {'fields': ('username', 'password',)}),
        ('Eve Characters', {'fields': ('main_character', 'characters',)}),
    )
