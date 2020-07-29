from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated profile!')
        else:
            messages.error(request, 'Update failed! Ensure the form if valid and try again.')
    else:
        form = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This confirmation is for a past order with order number {order_number}.'
        'A confirmation was sent to the provided email address on the order date.'
    ))

    template = 'checkout/checkout-success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
