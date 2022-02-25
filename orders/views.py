from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.urls import reverse
from django.shortcuts import render, redirect


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            orders = OrderItem.objects.all()
            # total = orders.get(price='price', quantity='quantity')
            # all = int(total.price)*int(total.quantity)
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order, 'orders': orders})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
