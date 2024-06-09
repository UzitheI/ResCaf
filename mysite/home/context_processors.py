from menu.models import CartItem

def cart_context(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.dish.price * item.quantity for item in cart_items)
    else:
        cart_items = []
        total_price = 0
    return {
        'cart_items': cart_items,
        'total_price': total_price,
    }
