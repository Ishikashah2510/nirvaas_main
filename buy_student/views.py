from django.shortcuts import render
from sell_staff.models import Items
from  buy_student.models import Cart
import random
from welcome.models import Users
# Create your views here.


def display_details(request):
    item_id = request.GET.get('item_id')
    try:
        i = Items.objects.get(Item_id=item_id)
        return render(request, 'buy_student/item_display.html', {'item': i})
    except Items.DoesNotExist:
        return render(request, 'buy_student/item_display.html')


def add_to_cart(request):
    if request.method == 'POST':
        f = open('loggedin.txt', 'r')
        email = f.readline()
        id = request.POST.get('id')
        i = Items.objects.none()
        try:
            i = Items.objects.get(Item_id=id)
        except Items.DoesNotExist:
            pass
        order_id = random.randint(100, 999)
        c = Cart(Item_id=i.Item_id, Item_title=i.Item_title, Item_price=i.Item_price, Order_id=order_id, email_id=email)
        c.save()
        i = Items.objects.all()
        return render(request, 'buy_student/buy_display.html', {'message': 'The Item has been successfully added to cart!', 'items':i})
    else:
        return render(request, 'buy_student/item_display.html')


def display_all_details(request):
    i = Items.objects.all()
    return render(request, 'buy_student/buy_display.html', {'items': i})


def view_cart(request):
    f = open('loggedin.txt', 'r')
    email = f.readline()
    i = Cart.objects.filter(email_id=email)
    return render(request, 'buy_student/view_cart.html', {'items': i})
