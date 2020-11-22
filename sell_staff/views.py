from django.shortcuts import render
import random
from sell_staff.models import Items

# Create your views here.


def sell(request):
    if request.method == "POST":
        item_name = request.POST.get("item_name")
        item_ab = request.POST.get("item_ab")
        item_price = request.POST.get("item_price")
        quantity = request.POST.get("qty")
        item_desc = request.POST.get("item_desc")
        item_image = request.POST.get("item_pic")
        item_type = request.POST.get("item_type")
        item_id = 100000
        while True:
            item_id = random.randint(100000, 999999)
            try:
                i = Items.objects.get(Item_id=item_id)
            except Items.DoesNotExist:
                break

        i = Items(Item_id=item_id, Item_title=item_name, Item_ab=item_ab, Item_price=item_price, Item_quantity=quantity,
                  Item_description=item_desc, Item_photo=item_image, Item_type= item_type)
        i.save()
        return render(request, 'welcome/homepage_staff.html', {'message': 'The item has been successfully uploaded!'})
    else:
        return render(request, 'sell_staff/sell_form.html')
