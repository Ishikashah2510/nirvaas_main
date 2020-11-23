from django.shortcuts import render
from sell_staff.models import Items
from  buy_student.models import Cart
import random
from welcome.views import email
# Create your views here.
def display_details(request,item_id):
    try:
        i = Items.objects.get(Item_id=item_id)
        return render(request, 'buy_student/item_display.html', {'item': i})
    except Items.DoesNotExist:
        pass

def add_to_cart(request):
    if request.method=='POST':
        id = request.POST.get('id')
        i = Items.objects.none()
        try:
            i = Items.objects.get(Item_id=id)
        except Items.DoesNotExist:
            pass
        order_id = random.randint(100,999)
        c = Cart(Item_id=i.Item_id, Item_title=i.Item_title, Item_price=i.Item_price, Order_id = order_id, buyer_email= email)
        c.save()
        return render(request, 'buy_student/buy_display.html', {'message':'The Item has been successfully added to cart!'} )
    else:
        return render(request, 'buy_student/item_display.html')

def display_all_details(request):
    i = Items.objects.all()
    return render(request, 'buy_student/buy_display.html', {'items': i})
