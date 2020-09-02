from django.conf.urls import url
from shares import views
app_name = 'shares'

urlpatterns = [
    url(r'^category$', views.Shares_category.as_view(), name='Shares_category'),
    url(r'^category/export$', views.Shares_category_export.as_view(), name='Shares_category_export'),
    url(r'^list/export$', views.Shares_export.as_view(), name='Shares_export'),
    url(r'^list$', views.Shares_list.as_view(), name='Shares_list')
]