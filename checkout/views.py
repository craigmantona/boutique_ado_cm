from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JiOjNAdnCyPqZTHJ6SlOSRonES2JT1SVyetrY7bLYODgl6FW9jUnvuDFqJZPc9HNN0LiHOSRp8Ho1QI5K7Z4OCm003CHmiDdP',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)