from django.shortcuts import render
from sell_staff.models import Items
from buy_student.models import Cart, Order
import random
from datetime import date
from datetime import datetime
from welcome import notification_sender as ns
from welcome.models import Users
from buy_student import invoice_generator as ig

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
    which = request.GET.get('which')
    if which != '2':
        which = 1
    else:
        which = 2
    f = open('loggedin.txt', 'r')
    email = f.readline()
    i = Cart.objects.filter(email_id=email)
    if which == 1 and i != Cart.objects.none():
        cart_total = 0
        for item in i:
            cart_total += item.Item_price
        return render(request, 'buy_student/view_cart.html', {'items': i, 'total': cart_total})
    elif which == 2 and i != Cart.objects.none():
        return render(request, 'buy_student/remove_item.html', {'items': i})
    else:
        return render(request, 'buy_student/view_cart.html', {'message': 'No items in the cart!'})


def remove_an_item(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        f = open('loggedin.txt', 'r')
        email = f.readline()
        try:
            c = Cart.objects.get(email_id=email, Order_id=order_id)
            c.delete()
            i = Cart.objects.filter(email_id=email)
            return render(request, 'buy_student/view_cart.html', {'items': i, 'message': 'The item has been removed successfully'})
        except Cart.DoesNotExist:
            i = Cart.objects.filter(email_id=email)
            return render(request, 'buy_student/remove_item.html', {'items': i, 'message': 'Kindly type the order id of an item in cart'})


def empty_cart(request):
    f = open('loggedin.txt', 'r')
    email = f.readline()
    c = Cart.objects.filter(email_id=email)
    c.delete()
    return render(request, 'buy_student/view_cart.html', {'message': 'No items in the cart!'})


def goto_empty_confirm(request):
    return render(request, 'buy_student/empty_confirm.html')


cart_total = 0


def goto_checkout(request):
    global cart_total
    f = open('loggedin.txt', 'r')
    email = f.readline()
    c = Cart.objects.filter(email_id=email)
    for item in c:
        cart_total += item.Item_price
    return render(request, 'buy_student/checkout.html', {'total': cart_total})


def generate_invoice(request):
    global cart_total
    f = open('loggedin.txt', 'r')
    email = f.readline()
    c = Cart.objects.filter(email_id=email)
    oid = random.randint(100, 999)
    o = []
    f = []
    for item in c:
        o.append(Order(Item_id=item.Item_id, Item_title=item.Item_title,
                       Item_price=item.Item_price, Item_quantity=item.Item_quantity,
                       email_id=email, Order_id=oid, Order_date=date.today().strftime("%Y-%m-%d"),
                       Order_time=datetime.now().strftime('%H:%M')))
        x = Items.objects.get(Item_id=item.Item_id)
        x.Item_quantity -= 1
        f.append(x)
        if x.Item_quantity < 0:
            msg = 'Sorry, item ' + x.Item_title + " doesn't have demanded quantity!"
            return render(request, 'buy_student/display_orders.html', {'message': msg})
    for item in o:
        item.save()
    for item in f:
        item.save()
    c.delete()
    c = Order.objects.filter(email_id=email)

    z = Items.objects.all()
    for item in z:
        if item.Item_quantity == 0:
            notification = "Item " + str(item.Item_id) + " has gone out of stock"
            for e in Users.objects.filter(type_user='Stationery_staff'):
                ns.send_notification(notification, e.email_id)
            item.delete()
    ig.generate(oid, cart_total, o)
    notification = "You placed an order worth Rs. " + str(cart_total) + ". Check in previous orders for more details"
    to = email
    ns.send_notification(notification, to)
    return render(request, 'buy_student/display_orders.html', {'items': c[::-1], 'message': 'Order has been successfully placed'})


def goto_display_order(request):
    f = open('loggedin.txt', 'r')
    email = f.readline()
    c = Order.objects.filter(email_id=email)[::-1]
    if len(c) == 0:
        return render(request, 'buy_student/display_orders.html', {'message': 'No orders placed yet'})
    return render(request, 'buy_student/display_orders.html', {'items': c})
