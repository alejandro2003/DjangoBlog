from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Article


def home(request):
    articles = Article.objects.all()  # todos los articulos
    # con poner un id en el metodo get recibimos un articulo concreto

    context = {
        'articles': articles
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article.html', {'article':article})