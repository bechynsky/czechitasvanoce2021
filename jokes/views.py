from django.http import HttpResponse
from django.shortcuts import render
from .models import Joke


def index(request):
    joke = Joke.objects.get(id=1)
    # return render(request, "jokes/randomJoke.html", {"joke": joke})
    return HttpResponse(joke.content)
