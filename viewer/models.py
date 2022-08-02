from django.db.models import (
    CharField,
    Model,
    FloatField,
    ForeignKey,
    DO_NOTHING,
    TextField,
    DateTimeField,
    IntegerField,
    DateField
)


class Genre(Model):
    name = CharField(max_length=128)


class Actor(Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    phone = CharField(max_length=20)
    email = CharField(max_length=100)
    salary = FloatField(default=10000.0)


class Movie(Model):
    title = CharField(max_length=128)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)
