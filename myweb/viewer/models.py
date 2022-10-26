from django.db.models import CharField, DateField, Model, TextField


class Post(Model):
    title = CharField(max_length=128)
    content = TextField()
    publish_date = DateField(auto_now=True)

    class Meta:
        ordering =["-publish_date"]

    def __str__(self):
        return self.title
