from django.shortcuts import render
from welcome.models import Users

# Create your views here.


def view_detail(request):
    if request.method == 'POST':
        det_type = request.POST.get('det_type')
        det_view = request.POST.get('det_view')
        if det_type == 'emailid':
            q = Users.objects.filter(email_id__contains=det_view)
            if not q:
                return render(request, 'admin_complete/admin_view.html', {'message': 'The user does not exist!'})
        else:
            q = Users.objects.filter(name__contains=det_view)
            if not q:
                return render(request, 'admin_complete/admin_view.html', {'message': 'The user does not exist!'})

        return render(request, 'admin_complete/disp_details.html', {'users': q})

    else:
        return render(request, 'admin_complete/admin_view.html')


def view_all(request):
    if request.method == 'POST':
        try:
            q = Users.objects.all()
            return render(request, 'admin_complete/disp_details.html', {'users': q})
        except Users.DoesNotExist:
            return render(request, 'admin_complete/admin_view.html', {'message': 'No users!'})
    else:
        return render(request, 'admin_complete/admin_view.html')


q = Users.objects.none()


def delete_info(request):
    global q
    if request.method == 'POST':
        det = request.POST.get('det_view')
        try:
            q = Users.objects.get(email_id=det)
            return render(request, 'admin_complete/confirm_delete.html', {'users': q})
        except Users.DoesNotExist:
            return render(request, 'admin_complete/admin_delete.html', {'message': 'No such user exists!'})
    else:
        return render(request, 'admin_complete/admin_delete.html')


def delete_confirm(request):
    if request.method == 'POST':
        q.delete()
        return render(request, 'admin_complete/admin_delete.html', {'message': 'Account deletion successful'})
    else:
        return render(request, 'admin_complete/admin_delete.html')
