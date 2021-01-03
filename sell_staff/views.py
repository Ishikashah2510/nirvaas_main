from django.shortcuts import render
import random
from sell_staff.models import Items
from django.core.files.storage import FileSystemStorage
from welcome import notification_sender as ns
# Create your views here.


def sell(request):
    if request.method == "POST":
        item_name = request.POST.get("item_name")
        item_ab = request.POST.get("item_ab")
        item_price = request.POST.get("item_price")
        quantity = request.POST.get("qty")
        item_desc = request.POST.get("item_desc")
        Item_photo = request.FILES["Item_photo"]
        item_type = request.POST.get("item_type")
        item_id = 100000
        while True:
            item_id = random.randint(100000, 999999)
            try:
                i = Items.objects.get(Item_id=item_id)
            except Items.DoesNotExist:
                break
        fs = FileSystemStorage()
        filename = fs.save(Item_photo.name, Item_photo)
        i = Items(Item_id=item_id, Item_title=item_name, Item_ab=item_ab, Item_price=item_price, Item_quantity=quantity,
                  Item_description=item_desc, Item_photo=Item_photo, Item_type=item_type)
        i.save()
        f = open('loggedin.txt', 'r')
        email1 = f.readline()
        notification = "You put item " + item_name + " on sale"
        to = email1
        ns.send_notification(notification, to)
        return render(request, 'welcome/homepage_staff.html', {'message': 'The item has been successfully uploaded!'})
    else:
        return render(request, 'sell_staff/sell_form.html')
