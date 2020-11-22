from django.shortcuts import render
from sell_staff.models import Items

def check_stock(request):
    if(request.method=="POST"):
        item_type = request.POST.get("item_type")
        val = request.POST.get("val_1")
        q = Items.objects.none()
        print(val)
        if item_type == 'Item_name':
            try:
                q = Items.objects.get(Item_title=val)
                print(q.Item_ab)
            except Items.DoesNotExist:
                return render(request, 'Check_stock/check_html.html', {'message': 'The item does not exist!'})
        else:
            try:
                q = Items.objects.get(Item_ab=val)
                print(q.Item_ab)
            except Items.DoesNotExist:
                return render(request, 'Check_stock/check_html.html', {'message': 'The item does not exist!'})

        return render(request,'Check_stock/disp_stock.html',{'items': q})

    else:
        return render(request,'Check_stock/check_html.html')