from django.shortcuts import render

def about(request):
    """Returns a rendered template of the about page"""

    return render(request, 'about/about.html')
