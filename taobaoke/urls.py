from django.conf.urls import url
from taobaoke import views
app_name = 'tbk'

urlpatterns = [
    url(r'^list$', views.Tbk_list.as_view(), name='Tbk_list'),
    url(r'^product/list$', views.Tbk_material_search.as_view(), name='Tbk_material_search')
]