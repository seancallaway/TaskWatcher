from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.forms import TWUserChangeForm, TWUserCreationForm
from users.models import TWUser


class TWUserAdmin(UserAdmin):
    add_form = TWUserCreationForm
    form = TWUserChangeForm
    model = TWUser
    list_display = ['email', 'username']


admin.site.register(TWUser, TWUserAdmin)
