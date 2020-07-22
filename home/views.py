from django.shortcuts import render

from content_management.models import Theme

def home(request):
    """ A view which return the index page """
    theme = Theme.objects.get(pk=1)
    theme_dict = {
        'colour_1': theme.colour_1,
        'colour_2': theme.colour_2,
        'colour_3': theme.colour_3,
        'colour_4': theme.colour_4,
        'colour_5': theme.colour_5,
    }
    print(theme_dict)
    context = {
        'theme': theme,
    }
    return render(request, 'home/index.html', context=context)
