from decimal import Decimal
from django.conf import settings


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0

    grand_total = total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'class_count': class_count,
        'grand_total': grand_total,
    }

    return context