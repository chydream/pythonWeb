from django.conf.urls import url
from taobaoke import views
app_name = 'tbk'

urlpatterns = [
    url(r'^item/info$', views.Tbk_item_info.as_view(), name='Tbk_item_info'),
    url(r'^product/list$', views.Tbk_material_search.as_view(), name='Tbk_material_search'),
    url(r'^material/list$', views.Tbk_material_optimus.as_view(), name='Tbk_material_optimus'),
    url(r'^coupon$', views.Tbk_itemid_coupon.as_view(), name='Tbk_itemid_coupon'),
    url(r'^coupon/convert$', views.Tbk_coupon_convert.as_view(), name='Tbk_coupon_convert'),
    url(r'^item/word$', views.Tbk_item_word.as_view(), name='Tbk_item_word'),
    url(r'^shop/search$', views.Tbk_shop_search.as_view(), name='Tbk_shop_search'),
    url(r'^shop/recommend$', views.Tbk_shop_recommend.as_view(), name='Tbk_shop_recommend'),
    url(r'^shop/convert$', views.Tbk_shop_convert.as_view(), name='Tbk_shop_convert'),
    url(r'^product/convert$', views.Tbk_item_convert.as_view(), name='Tbk_item_convert'),
    url(r'^activity/info$', views.Tbk_activity_info.as_view(), name='Tbk_activity_info'),
    url(r'^tpwd/create$', views.Tbk_tpwd_create.as_view(), name='Tbk_tpwd_create'),
    url(r'^spread$', views.Tbk_spread.as_view(), name='Tbk_spread')
]