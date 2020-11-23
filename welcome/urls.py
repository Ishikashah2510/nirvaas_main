from django.conf.urls import url
from django.conf.urls.static import static
from nirvaas_main import settings
from welcome import views
import sell_staff.views as vws
import Check_Stock.views as cvws
import admin_complete.views as avs
import buy_student.views as bsv
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
    url(r'^delete_item/$', cvws.delete_item, name='delete_item'),
    url(r'^delete_account_confirm/$', avs.delete_confirm, name='delete_account_confirm'),
    url(r'^delete_item_confirm/$', cvws.delete_confirm, name='delete_item_confirm'),
    url(r'^display_details/$', bsv.display_details, name='display_details'),
    url(r'^add_to_cart/$', bsv.add_to_cart, name='add_to_cart'),
    url(r'^display_all_item/$', bsv.display_all_details, name='display_all_item'),
    url(r'^view_cart/$', bsv.view_cart, name='view_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
