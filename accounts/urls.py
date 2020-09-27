from django.conf.urls import url
from accounts import views
app_name = 'accounts'
urlpatterns = [
    url(r'^login$', views.Accounts.as_view(), name='Accounts'),
]
