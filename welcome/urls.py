from django.conf.urls import url
from welcome import views
import sell_staff.views as vws
import Check_Stock.views as cvws
# SET THE NAMESPACE!
app_name = 'welcome'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^sell/$', vws.sell, name='sell'),
    url(r'^check_stock/$', cvws.check_stock, name='check_stock'),
]
