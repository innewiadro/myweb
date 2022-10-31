from django.db.transaction import atomic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import CharField, Textarea
from .models import Profile


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ["username", "first_name", "email"]

    biography = CharField(label="Your story", widget=Textarea, min_length=20)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visable in self.visible_fields():
            visable.field.widget.attrs["class"] = "form-control"



    @atomic
    def save(self, commit=True):
        self.instance.is_active = False
        user = super().save(commit)
        biography = self.cleaned_data["biography"]
        profile = Profile(biography=biography, user=user)
        if commit:
            profile.save()
        return super().save(commit)


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        fields = ["username", "first_name", "groups"]

    biography = CharField(label="Your story", widget=Textarea, min_length=20)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    @atomic
    def save(self, commit=True):
        user = super().save(commit)
        biography = self.cleaned_data["biography"]
        profile = Profile.objects.get(user__pk=user.pk)
        profile.biography = biography
        if commit:
            profile.save()
        return user