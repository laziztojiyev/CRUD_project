from django.forms import ModelForm

from users.models import CustomUser


class ProfileModelForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'phone_number', 'email', 'image')


