from django.shortcuts import render
from django.http import JsonResponse

from .models import Theme

def get_theme(request):
    """
    Gets the default theme from the Theme model and 
    returns it as a JSON response
    """
    theme = Theme.objects.get(pk=1)
    theme_dict = {
        'colour_1': theme.colour_1,
        'colour_2': theme.colour_2,
        'colour_3': theme.colour_3,
        'colour_4': theme.colour_4,
        'colour_5': theme.colour_5,
        'dark_mode_colour': theme.dark_mode_background_colour,
    }

    response = JsonResponse(theme_dict)

    return response
