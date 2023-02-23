from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ClearableFileInput, ImageField


from profiles import forms
from profiles.models import Photo

User = get_user_model()


class CreationForm(UserCreationForm):
    image = ImageField(
        label=u'Фото профиля',
        widget=ClearableFileInput(
                           attrs={'multiple': 'multiple'}),
        required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'first_name', 'username', 'phone', 'email', 'sex', 'city', 'year',
            'image')
        # widgets = {
        #     'image': ClearableFileInput(attrs={'multiple': True}),
        # }


# class CreationForm(forms.Form):
#     first_name = forms.CharField(label=u'Локация')
#     username = forms.CharField(label=u'Никнейм')
#     phone = forms.PhoneNumberField(label=u'Телефон')
#     email = forms.EmailField(CharField)
#     description = forms.CharField
#
#     photos = forms.ImageField(label=u'Фотографии', widget=forms.FileInput(attrs={'multiple': 'multiple'}))


class ChangeForm(UserChangeForm):
    password = None
    image = ImageField(
        label=u'Фото профиля',
        widget=ClearableFileInput(attrs={'multiple': 'multiple'}),
        required=False)

    class Meta(UserChangeForm.Meta):
        model = User
        fields = (
            'first_name', 'email', 'sex', 'city', 'year', 'image')
        # widgets = {
        #     'image': ClearableFileInput(attrs={'multiple': True}),
        # }

