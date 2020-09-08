from django.conf.urls import url
from shares import views
app_name = 'shares'

urlpatterns = [
    url(r'^category$', views.Shares_category.as_view(), name='Shares_category'),
    url(r'^category/export$', views.Shares_category_export.as_view(), name='Shares_category_export'),
    url(r'^list/export$', views.Shares_export.as_view(), name='Shares_export'),
    url(r'^list$', views.Shares_list.as_view(), name='Shares_list'),
    url(r'^detail/export$', views.Shares_detail_export.as_view(), name='Shares_detail_export'),
    url(r'^detail/export/day$', views.Shares_detail_export_by_day.as_view(), name='Shares_detail_export_by_day'),
    url(r'^news$', views.Shares_news.as_view(), name='Shares_news'),
    url(r'^detail$', views.Shares_detail.as_view(), name='Shares_detail'),
]