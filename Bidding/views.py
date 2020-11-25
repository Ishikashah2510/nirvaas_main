from django.shortcuts import render
import random
from Bidding.models import Bidding, BidItems, old_items_on_bid
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
                i = BidItems.objects.get(item_id=item_id)
            except BidItems.DoesNotExist:
                break

        i = BidItems(item_id=item_id, threshold_value=item_price,
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
    b = BidItems.objects.filter(seller_email=email)
    bi = Bidding.objects.filter(seller_email=email)
    if len(bi) != 0:
        return render(request, 'Bidding/view_items_on_bid.html', {'items': bi})
    return render(request, 'Bidding/view_items_on_bid.html', {'items': b})


def remove_item_from_bid(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        f = open('loggedin.txt', 'r')
        email = f.readline()
        i = BidItems.objects.filter(seller_email=email)
        try:
            b = BidItems.objects.get(item_id=item_id)
            b.delete()
            try:
                bi = Bidding.objects.get(item_id=item_id)
                bi.delete()
            except Bidding.DoesNotExist:
                pass
            i = BidItems.objects.filter(seller_email=email)
            return render(request, 'Bidding/remove_item_from_bid.html', {'message': 'Item removed', 'items': i})
        except BidItems.DoesNotExist:
            return render(request, 'Bidding/remove_item_from_bid.html',
                          {'message': 'Kindly enter a valid item ID', 'items': i})
    else:
        f = open('loggedin.txt', 'r')
        email = f.readline()
        i = BidItems.objects.filter(seller_email=email)
        return render(request, 'Bidding/remove_item_from_bid.html', {'items': i})


def old_bids(request):
    f = open('loggedin.txt', 'r')
    email = f.readline()
    i = old_items_on_bid.objects.filter(seller_email=email)
    return render(request, 'Bidding/old_bids.html', {'items': i})


def make_a_bid(request):
    if request.method == 'POST':
        f = open('loggedin.txt', 'r')
        email = f.readline()
        item_id = request.POST.get('item_id')
        bid_val = request.POST.get('bid_val')
        try:
            i = BidItems.objects.get(item_id=item_id)
        except BidItems.DoesNotExist:
            return render(request, 'Bidding/make_a_bid.html', {'message': 'Kindly enter a valid item id'})
        try:
            i = Bidding.objects.get(item_id=item_id)
            if float(bid_val) <= i.curr_bid_value:
                bi = BidItems.objects.exclude(seller_email=email)
                bid = Bidding.objects.exclude(seller_email=email)
                if len(bid) == 1:
                    return render(request, 'Bidding/make_a_bid.html',
                                  {'message': 'Kindly enter a bid value greater than ' + str(i.curr_bid_value),
                                   'items': bid})
                return render(request, 'Bidding/make_a_bid.html',
                              {'message': 'Kindly enter a bid value greater than ' + str(i.curr_bid_value), 'items': bi})
            bid = BidItems.objects.get(item_id=item_id)
            b = Bidding(buyer_email=email, curr_bid_value=bid_val,
                        prev_bid_value=i.curr_bid_value, item_id=item_id,
                        threshold_value=bid.threshold_value, seller_email=bid.seller_email,
                        item_name=bid.item_name, prev_buyer_email=i.buyer_email,
                        old_bid_date=i.new_bid_date, new_bid_date=date.today().strftime("%Y-%m-%d"))
            b.save()
            return render(request, 'Bidding/bid_options.html', {'message': 'Your bid has been placed!'})
        except Bidding.DoesNotExist:
            i = BidItems.objects.get(item_id=item_id)
            if float(bid_val) <= i.threshold_value:
                bi = BidItems.objects.exclude(seller_email=email)
                return render(request, 'Bidding/make_a_bid.html',
                              {'message': 'Kindly enter a bid value greater than ' + str(i.threshold_value), 'items': bi})
            b = Bidding(item_id=item_id, seller_email=i.seller_email,
                        buyer_email=email, curr_bid_value=bid_val,
                        prev_bid_value=i.threshold_value, threshold_value=i.threshold_value,
                        prev_buyer_email=email, item_name=i.item_name)
            b.save()
            return render(request, 'Bidding/bid_options.html', {'message': 'Your bid has been placed!'})
    else:
        f = open('loggedin.txt', 'r')
        email = f.readline()
        i = BidItems.objects.exclude(seller_email=email)
        bi = Bidding.objects.exclude(seller_email=email)
        if len(bi) != 0:
            return render(request, 'Bidding/make_a_bid.html', {'items': bi})
        return render(request, 'Bidding/make_a_bid.html', {'items': i})


def view_items_bid_on(request):
    f = open('loggedin.txt', 'r')
    email = f.readline()
    items = Bidding.objects.filter(buyer_email=email)
    items_exceed = Bidding.objects.filter(prev_buyer_email=email)
    return render(request, 'Bidding/where_bid_placed.html', {'items': items, 'items_exceed': items_exceed})