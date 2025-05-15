from django.shortcuts import render
from django.http import HttpResponse

from .models import Article

import requests
import json

def homepage(request):
    articles = Article.objects.all()

    return render(request, 'content/homepage.html', {'articles': articles})

def article(request, id):
    article = Article.objects.get(pk=id)

    return render(request, 'content/article.html', {'article': article})