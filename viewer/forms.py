from django.forms import (
    CharField,
    DateField,
    ModelForm,
    IntegerField,
    ModelChoiceField,
    Textarea,
    FloatField
)

from viewer.models import Genre, Movie, Actor


class MovieForm(ModelForm):
    title = CharField(max_length=128)
    genre = ModelChoiceField(queryset=Genre.objects)
    rating = IntegerField(min_value=1, max_value=10)
    released = DateField()
    description = CharField(widget=Textarea, required=False)

    class Meta:
        model = Movie
        fields = '__all__'


class ActorForm(ModelForm):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    phone = CharField(max_length=20)
    email = CharField(max_length=100)
    salary = FloatField(min_value=0)

    class Meta:
        model = Actor
        fields = '__all__'
