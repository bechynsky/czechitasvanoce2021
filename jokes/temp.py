from .models import Category, Joke
import csv
import os


def init_categories():
    categories = ['Rodinné vánoční vtipy', 'Vánoční vtipy o mužích a ženách', 'Vánoční vtipy o Santovi']

    for category in categories:
        Category.objects.create(name=category)


def init_jokes():
    filepath = os.path.join(os.getcwd(), "jokes", "vtipy_1.csv")

    jokes_list = []
    with open(filepath, "r", encoding="utf8") as data:
        jokes = csv.DictReader(data)
        for joke in jokes:
            jokes_list.append(joke)

    category = Category.objects.get(id=1)
    for joke in jokes_list:
        Joke.objects.get_or_create(content=joke["content"], category=category)
