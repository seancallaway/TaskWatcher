from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from users.models import TWUser


class TWUserChangeForm(UserChangeForm):

    class Meta:
        model = TWUser
        fields = ('username', 'email')


class TWUserCreationForm(UserCreationForm):

    class Meta:
        model = TWUser
        fields = ('username', 'email')
