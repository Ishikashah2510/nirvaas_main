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
    if request.method == 'POST':
        try:
            q = Items.objects.all()
            return render(request, 'Check_stock/disp_stock.html', {'items': q})
        except Items.DoesNotExist:
            return render(request, 'Check_stock/check_html.html', {'message': 'The item does not exist!'})
    else:
        return render(request, 'Check_stock/check_html.html')