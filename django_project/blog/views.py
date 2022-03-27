from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'posts': [
            {
                'title': 'Blog 1',
                'author': 'rokamura',
                'date_created': 'March 26, 2022',
                'content': 'This is the first post',
            },
            {
                'title': 'Blog 2',
                'author': 'jliao',
                'date_created': 'March 27, 2022',
                'content': 'This is another post',
            },
        ]
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')