from django.contrib.auth.models import User

from django.db.models import CASCADE, Model, OneToOneField, TextField


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    biography = TextField(default="add some text")

    def delete(self, using=None, keep_parents=False):
        self.user.delete()
        return super().delete(using, keep_parents)

    def __str__(self):
        return self.user.username
