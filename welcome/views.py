from django.shortcuts import render
from Bidding.models import Bidding, BidItems, old_items_on_bid
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import re
from sell_staff.models import Items
from welcome.models import Users
from django.db.models import Q
import datetime as dt


def index(request):
    return render(request, 'welcome/index.html')


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.method == 'POST':
        name_ = request.POST.get('name')
        mno = request.POST.get('mno')
        tu = request.POST.get('choice_field')
        email = request.POST.get('email')
        password_ = request.POST.get('password')
        password1 = request.POST.get('password1')
        if password1 == password_:
            if tu == 'Student':
                valid = re.search(r"[1-9][0-9][a-zA-Z]{3}[0-9]{3}@nirmauni.ac.in", email)
                if not valid:
                    return render(request, 'welcome/registration.html',
                                  {'error_message': 'Kindly enter your nirmauni id since you are a student', })
        else:
            return render(request, 'welcome/registration.html', {'error_message': 'Kindly enter the same password', })
        q1 = Users.objects.filter(Q(email_id=email) | Q(mobile_no=mno))
        if q1:
            return render(request, 'welcome/registration.html', {'error_message': 'Account already exists', })
        else:
            u = Users(name=name_, mobile_no=mno, type_user=tu, email_id=email, password=password_)
            u.save()
        return render(request, 'welcome/login.html')
    else:
        return render(request, 'welcome/registration.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password_ = request.POST.get('password')
        choice = request.POST.get('choice_field')
        f = open('loggedin.txt', 'w')
        f.write(email)
        f.close()
        order_check = Items.objects.all()
        for a in order_check:
            if a.Item_quantity <= 0:
                a.delete()
        if choice == 'Student':
            try:
                check_details = Users.objects.get(email_id=str(email), password=str(password_), type_user=str(choice))
            except Users.DoesNotExist:
                return render(request, 'welcome/login.html',
                              {'error_message': 'Kindly check the details you entered', })
            today = dt.date.today()
            gone = today - dt.timedelta(days=7)
            i = BidItems.objects.filter(seller_email=email)
            for item in i:
                if str(item.item_place_date) < (gone.strftime("%Y-%m-%d")):
                    try:
                        b = Bidding.objects.get(seller_email=email)
                        r = old_items_on_bid(item_id=item.item_id, seller_email=email,
                                             buyer_email=b.buyer_email, threshold_value=item.threshold_value,
                                             last_bid_value=b.curr_bid_value)
                        r.save()
                        item.delete()
                        b.delete()
                    except Bidding.DoesNotExist:
                        pass
            return render(request, 'welcome/homepage_student.html')
        elif choice == 'Stationery_staff':
            try:
                check_details = Users.objects.get(email_id=str(email), password=str(password_), type_user=str(choice))
            except Users.DoesNotExist:
                return render(request, 'welcome/login.html', {'error_message': 'Kindly check the details you entered', })
            return render(request, 'welcome/homepage_staff.html')
        elif choice == 'Admin':
            try:
                check_details = Users.objects.get(email_id=str(email), password=str(password_), type_user=str(choice))
            except Users.DoesNotExist:
                return render(request, 'welcome/login.html', {'error_message': 'Kindly check the details you entered', })
            return render(request, 'welcome/homepage_admin.html')
    else:
        return render(request, 'welcome/login.html', {})
