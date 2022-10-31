from django.db.models import CASCADE, CharField, Model, TextField, SlugField, ForeignKey, DateTimeField, IntegerField
from django.contrib.auth.models import User
from django.utils.text import slugify

STATUS = ((0, "Draft"),
          (1, "Published"))


class Post(Model):
    title = CharField(max_length=200, unique=True)
    slug = SlugField(max_length=200, unique=True)
    author = ForeignKey(User, on_delete=CASCADE, related_name="blog_posts", default=1)
    updated_on = DateTimeField(auto_now=True)
    content = TextField()
    created_on = DateTimeField(auto_now_add=True)

    status = IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
