from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ClearableFileInput

User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'first_name', 'username', 'phone', 'email', 'sex', 'city', 'year',
            'image',)
        widgets = {'image': ClearableFileInput(attrs={'multiple': True}),}


class ChangeForm(UserChangeForm):
    password = None

    class Meta(UserChangeForm.Meta):
        model = User
        fields = (
            'first_name', 'email', 'sex', 'city', 'year', 'image')
        widgets = {'image': ClearableFileInput(attrs={'multiple': True}), }

