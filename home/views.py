from django.shortcuts import render

def home(request):
    """ A view which return the index page """
    return render(request, 'home/index.html')
