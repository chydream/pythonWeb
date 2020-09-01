from django.conf.urls import url
from shares import views

urlpatterns = [
    url(r'^category$', views.Shares_category.as_view(), name='Shares_category'),
    url(r'^category/export$', views.Shares_category_export.as_view(), name='Shares_category_export')
]