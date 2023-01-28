from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'first_name', 'username', 'phone', 'email', 'sex', 'city', 'year',
            'image')


class ChangeForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'first_name', 'phone', 'email', 'sex', 'city', 'year',
            'image')

