from django.contrib.auth.models import User
from  django.db.models import CASCAD, Model, OneToOneField, TextField


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCAD)
    biography = TextField()
