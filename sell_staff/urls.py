from django.conf.urls import url
import Check_Stock.views as cvws
import sell_staff.views as vws
# SET THE NAMESPACE!
app_name = 'check_stock'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    url(r'^check_stock/$', cvws.check_stock, name='check_stock'),
    url(r'^$', vws.sell, name='sell'),
]
