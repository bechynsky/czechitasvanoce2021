from django.shortcuts import render
from random import choice
from .models import Joke


def index(request):
    all_jokes = Joke.objects.all()
    # id existujícího vtipů - seznam
    all_jokes_id = [x.id for x in all_jokes]
    # náhodný výběr id ze seznamu
    joke_id = choice(all_jokes_id)
    joke = Joke.objects.get(id=joke_id)
    return render(request, "jokes/index.html", {"click_joke": joke.content})
