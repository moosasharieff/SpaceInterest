

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):

    class Meta:
        # Below fields are what we are seeking from the user
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adding custom labels to the forms
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
