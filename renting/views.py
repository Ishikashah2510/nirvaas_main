from django.shortcuts import render
from renting.models import *
import random
from django.core.files.storage import FileSystemStorage
from datetime import datetime, timedelta
from welcome import notification_sender as ns

# Create your views here.


def view_options(request):
    return render(request, 'renting/rent_options.html')


def view_options_staff(request):
    return render(request, 'renting/rent_options_staff.html')


def put_on_rent_staff(request):
    if request.method == "POST":
        item_name = request.POST.get("item_name")
        item_ab = request.POST.get("item_ab")
        item_desc = request.POST.get("item_desc")
        item_photo = request.FILES["Item_photo"]
        item_type = request.POST.get("item_type")
        rent_id = 100000
        while True:
            rent_id = random.randint(100000, 999999)
            try:
                i = RentItems.objects.get(rent_id=rent_id)
            except RentItems.DoesNotExist:
                break
        fs = FileSystemStorage()
        filename = fs.save(item_photo.name, item_photo)
        i = RentItems(rent_id=rent_id, item_name=item_name, item_type=item_type,
                      item_description=item_desc, item_photo=item_photo, item_ab=item_ab)
        i.save()
        f = open('loggedin.txt', 'r')
        email = f.readline()
        notification = "You put item" + item_name + " on rent"
        to = email
        ns.send_notification(notification, to)
        return render(request, 'renting/rent_options_staff.html', {'message': 'The item has been successfully uploaded!'})
    else:
        return render(request, 'renting/put_on_rent_form.html')


def view_items_staff(request):
    try:
        r = RentItems.objects.all()
        return render(request, 'renting/view_items_on_rent_staff.html', {'items': r})
    except RentItems.DoesNotExist:
        return render(request, 'renting/view_items_on_rent_staff.html', {'message': 'No items placed on rent'})


def view_items_student(request):
    try:
        r = RentItems.objects.filter(rent_var=False)
        return render(request, 'renting/view_items_on_rent_student.html', {'items': r})
    except RentItems.DoesNotExist:
        return render(request, 'renting/view_items_on_rent_student.html', {'message': 'No items placed on rent'})


def rent_form(request):
    if request.method == "POST":
        rent_id = request.POST.get('rent_id')
        date = request.POST.get('date')
        f = open('loggedin.txt', 'r')
        email = f.readline()
        try:
            r = RentItems.objects.get(rent_id=rent_id)
            if date > str(datetime.now().date()):
                r.rent_date = datetime.now()
                r.rented_until = date
                r.renter_email = email
                r.rent_var = True
                r.save()
                return render(request, 'renting/rent_options.html',
                              {'message': 'Item rented succefully, kindly collect the item from Library desk'})
            else:
                return render(request, 'renting/rent_form.html', {'message': 'Kindly enter a valid date'})
        except RentItems.DoesNotExist:
            return render(request, 'renting/rent_form.html', {'message': 'Kindly enter a valid rent ID'})
    else:
        f = open('loggedin.txt', 'r')
        email = f.readline()
        r = RentItems.objects.filter(rent_var=False)
        try:
            a = RentItems.objects.get(renter_email__exact=email)
            return render(request, 'renting/rent_options.html',
                          {'message': 'Sorry you cannot rent an item. Kindly return the item you have currently rented to rent another item'})
        except RentItems.DoesNotExist:
            pass
        if len(r):
            return render(request, 'renting/rent_form.html', {'items': r})
        else:
            return render(request, 'renting/rent_form.html', {'message': 'No items placed for rent'})


def take_return(request):
    if request.method == "POST":
        rentid = request.POST.get('rent_id')
        try:
            r = RentItems.objects.get(rent_id=rentid)
            rdate = r.rent_date
            r.rent_date = datetime.today() + timedelta(150)
            email = r.renter_email
            r.renter_email = ""
            r.rent_var = False
            r.save()
            rent_id = 100000
            while True:
                rent_id = random.randint(100000, 999999)
                try:
                    i = RentItems.objects.get(rent_id=rent_id)
                except RentItems.DoesNotExist:
                    break
            f = OldRentedItems(rent_id=rent_id, renter_email=email, item_name=r.item_name,
                               item_photo=r.item_photo, rent_date=rdate)
            f.save()
            f = open('loggedin.txt', 'r')
            email1 = f.readline()
            notification = "Return taken from " + email + "of item " + r.item_name
            to = email1
            ns.send_notification(notification, to)
            notification = "You returned item " + r.item_name + " to " + email1
            to = email
            ns.send_notification(notification, to)
            return render(request, 'renting/rent_options_staff.html', {'message': 'Item return taken successfully'})
        except RentItems.DoesNotExist:
            r = RentItems.objects.filter(rent_var=True)
            return render(request, 'renting/take_return.html', {'message': 'Kindly enter a valid id', 'items': r})
    else:
        r = RentItems.objects.filter(rent_var=True)
        if len(r):
            return render(request, 'renting/take_return.html', {'items': r})
        else:
            return render(request, 'renting/take_return.html', {'message': 'No one has rented an item yet'})


def item_current_rented_staff(request):
    r = RentItems.objects.filter(rent_var=True)
    if len(r):
        return render(request, 'renting/items_current_rented_staff.html', {'items': r})
    else:
        return render(request, 'renting/items_current_rented_staff.html', {'message': 'No one has rented an item yet'})


def item_current_rented_student(request):
    f = open('loggedin.txt', 'r')
    email = f.readline()
    try:
        r = RentItems.objects.get(renter_email__exact=email)
        return render(request, 'renting/items_current_rented_student.html', {'items': r})
    except RentItems.DoesNotExist:
        return render(request, 'renting/items_current_rented_student.html', {'message': "You haven't rented any item"})


def view_old_rented_items_student(request):
    f = open('loggedin.txt', 'r')
    email = f.readline()
    r = OldRentedItems.objects.filter(renter_email__exact=email)
    if len(r):
        return render(request, 'renting/olditemsrented_student.html', {'items': r})
    else:
        return render(request, 'renting/olditemsrented_student.html', {'message': "You haven't rented any item yet"})
