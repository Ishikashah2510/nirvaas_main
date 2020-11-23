from django.shortcuts import render
from sell_staff.models import Items


def check_stock(request):
    if request.method == "POST":
        item_type = request.POST.get("item_type")
        val = request.POST.get("val_1")
        q = Items.objects.none()
        if item_type == 'Item_name':
            q = Items.objects.filter(Item_title__contains=val)
            if not q:
                return render(request, 'Check_stock/check_html.html', {'message': 'The item does not exist!'})
        else:
            q = Items.objects.filter(Item_ab__contains=val)
            if not q:
                return render(request, 'Check_stock/check_html.html', {'message': 'The item does not exist!'})

        return render(request,'Check_stock/disp_stock.html', {'items': q})

    else:
        return render(request,'Check_stock/check_html.html')


def view_all_items(request):
    which = '0'
    if request.method == 'POST':
        which = request.POST.get('which')
        if which == '2':
            try:
                q = Items.objects.all()
                return render(request, 'Check_stock/disp_stock.html', {'items': q})
            except Items.DoesNotExist:
                return render(request, 'Check_stock/check_html.html', {'message': 'The item does not exist!'})
        elif which == '1':
            try:
                q = Items.objects.all()
                return render(request, 'Check_stock/item_delete.html', {'items': q})
            except Items.DoesNotExist:
                return render(request, 'Check_stock/item_delete.html', {'message': 'The item does not exist!'})
    else:
        if which == '2':
            return render(request, 'Check_stock/check_html.html')
        elif which == '1':
            return render(request, 'Check_stock/item_delete.html')


q = Items.objects.none()


def delete_item(request):
    global q
    if request.method == 'POST':
        det = request.POST.get('det_view')
        try:
            q = Items.objects.get(Item_id=det)
            return render(request, 'Check_stock/confirm_delete_item.html', {'items': q})
        except Items.DoesNotExist:
            return render(request, 'Check_stock/item_delete.html', {'message': 'No such item exists!'})
    else:
        return render(request, 'Check_stock/item_delete.html')


def delete_confirm(request):
    if request.method == 'POST':
        q.delete()
        return render(request, 'Check_stock/item_delete.html', {'message': 'Item deletion successful'})
    else:
        return render(request, 'Check_stock/item_delete.html')