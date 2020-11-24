from django.shortcuts import render
import random
from Bidding.models import Bidding, Bid_Items
from datetime import date
from datetime import datetime
# Create your views here.


def goto_bid_options(request):
    return render(request, 'Bidding/bid_options.html')


def place_item_on_bid(request):
    if request.method == "POST":
        item_name = request.POST.get("item_name")
        item_price = request.POST.get("item_price")
        item_desc = request.POST.get("item_desc")
        item_image = request.POST.get("item_pic")
        item_id = 100000
        f = open('loggedin.txt', 'r')
        email = f.readline()
        while True:
            item_id = random.randint(100000, 999999)
            try:
                i = Bid_Items.objects.get(item_id=item_id)
            except Bid_Items.DoesNotExist:
                break

        i = Bid_Items(item_id=item_id, threshold_value=item_price,
                      item_description=item_desc, item_photo=item_image,
                      seller_email=email, item_name=item_name,
                      item_place_date=date.today().strftime("%Y-%m-%d"))
        i.save()
        return render(request, 'Bidding/bid_options.html', {'message': 'The item has been successfully uploaded!'})
    else:
        return render(request, 'Bidding/place_on_bid.html')


def view_items_placed_on_bid(request):
    f = open('loggedin.txt', 'r')
    email = f.readline()
    b = Bid_Items.objects.filter(seller_email=email)
    bi = Bidding.objects.filter(seller_email=email)
    if bi == Bidding.objects.none():
        return render(request, 'Bidding/view_items_on_bid.html', {'items': bi})
    return render(request, 'Bidding/view_items_on_bid.html', {'items': b})


def remove_item_from_bid(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        f = open('loggedin.txt', 'r')
        email = f.readline()
        i = Bid_Items.objects.filter(seller_email=email)
        try:
            b = Bid_Items.objects.get(item_id=item_id)
            b.delete()
            try:
                bi = Bidding.objects.get(item_id=item_id)
                bi.delete()
            except Bidding.DoesNotExist:
                pass
            i = Bid_Items.objects.filter(seller_email=email)
            return render(request, 'Bidding/remove_item_from_bid.html', {'message': 'Item removed', 'items': i})
        except Bid_Items.DoesNotExist:
            return render(request, 'Bidding/remove_item_from_bid.html',
                          {'message': 'Kindly enter a valid item ID', 'items': i})
    else:
        f = open('loggedin.txt', 'r')
        email = f.readline()
        i = Bid_Items.objects.filter(seller_email=email)
        return render(request, 'Bidding/remove_item_from_bid.html', {'items': i})
