from django.conf.urls import url
from welcome import views
import sell_staff.views as vws
import Check_Stock.views as cvws
import admin_complete.views as avs
# SET THE NAMESPACE!
app_name = 'welcome'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^sell/$', vws.sell, name='sell'),
    url(r'^check_stock/$', cvws.check_stock, name='check_stock'),
    url(r'^view_admin/$', avs.view_detail, name='view_admin'),
    url(r'^view_admin_all/$', avs.view_all, name='view_admin_all'),
    url(r'^view_items_all/$', cvws.view_all_items, name='view_items_all'),
    url(r'^delete_account/$', avs.delete_info, name='delete_account'),
    url(r'^delete_account_confirm/$', avs.delete_confirm, name='delete_account_confirm'),
]
