from django.conf.urls import url
from django.conf.urls.static import static
from nirvaas_main import settings
from welcome import views
import sell_staff.views as vws
import Check_Stock.views as cvws
import admin_complete.views as avs
import buy_student.views as bsv
import Bidding.views as bvws
import renting.views as rvs
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
    url(r'^remove_an_item/$', bsv.remove_an_item, name='remove_an_item'),
    url(r'^empty_cart/$', bsv.empty_cart, name='empty_cart'),
    url(r'^goto_empty_confirm/$', bsv.goto_empty_confirm, name='goto_empty_confirm'),
    url(r'^goto_checkout/$', bsv.goto_checkout, name='goto_checkout'),
    url(r'^generate_invoice/$', bsv.generate_invoice, name='generate_invoice'),
    url(r'^goto_display_order/$', bsv.goto_display_order, name='goto_display_order'),
    url(r'^goto_bid_options/$', bvws.goto_bid_options, name='goto_bid_options'),
    url(r'^place_an_item_on_bid/$', bvws.place_item_on_bid, name='place_an_item_on_bid'),
    url(r'^view_items_on_bid/$', bvws.view_items_placed_on_bid, name='view_items_on_bid'),
    url(r'^remove_item_from_bid/$', bvws.remove_item_from_bid, name='remove_item_from_bid'),
    url(r'^old_bids/$', bvws.old_bids, name='old_bids'),
    url(r'^make_a_bid/$', bvws.make_a_bid, name='make_a_bid'),
    url(r'^view_items_bid_on/$', bvws.view_items_bid_on, name='view_items_bid_on'),
    url(r'^searchresults/$', views.search_item, name='searchresults'),
    url(r'^notifications/$', views.view_notification, name='notifications'),
    url(r'^rent_options/$', rvs.view_options, name='rent_options'),
    url(r'^rent_options_staff/$', rvs.view_options_staff, name='rent_options_staff'),
    url(r'^put_on_rent_staff/$', rvs.put_on_rent_staff, name='put_on_rent_staff'),
    url(r'^view_on_rent_staff/$', rvs.view_items_staff, name='view_on_rent_staff'),
    url(r'^view_on_rent_student/$', rvs.view_items_student, name='view_on_rent_student'),
    url(r'^rent_item/$', rvs.rent_form, name='rent_item'),
    url(r'^take_return/$', rvs.take_return, name='take_return'),
    url(r'^current_rented_items/$', rvs.item_current_rented_staff, name='current_rented_items'),
    url(r'^current_rented_items_student/$', rvs.item_current_rented_student, name='current_rented_items_student'),
    url(r'^old_rented_items_student/$', rvs.view_old_rented_items_student, name='old_rented_items_student'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
