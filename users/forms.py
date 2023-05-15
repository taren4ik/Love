from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ClearableFileInput, ImageField

User = get_user_model()


class CreationForm(UserCreationForm):
    # image = ImageField(
    #     label=u'Фото профиля',
    #     widget=ClearableFileInput(attrs={'multiple': 'multiple'}),
    #     required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'first_name', 'username', 'phone', 'email', 'sex', 'city',
            'year', 'avatar',
        )


class ChangeForm(UserChangeForm):
    password = None
    image = ImageField(
        label=u'Фото профиля',
        widget=ClearableFileInput(attrs={'multiple': 'multiple'}),
        required=False, )

    class Meta(UserChangeForm.Meta):
        model = User
        fields = (
            'first_name', 'email', 'sex', 'city', 'year', 'image', 'avatar')
