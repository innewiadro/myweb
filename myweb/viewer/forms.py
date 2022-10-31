from django.forms import ModelForm
from django.db.models import CharField, TextField, DateTimeField, DateField, IntegerField, SlugField
from django.core.exceptions import ValidationError
from datetime import date
from .models import Post
import re

STATUS = ((0, "Draft"),
          (1, "Published"))


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

    title = CharField(max_length=200)
    content = TextField()
    status = IntegerField(choices=STATUS, default=0)
    slug = CharField(max_length=200, unique=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'