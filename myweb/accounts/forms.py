from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField, Textarea


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ["username", "first_name"]

    biography = CharField(label="Your story", widget=Textarea, min_length=20)