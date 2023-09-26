from django.urls import re_path, include
from invoices import views


urlpatterns = [
    # url(r'^invoices/$', views.invoice_list),
    re_path(r'^invoices/$', views.invoice_list, name='invoices'),
    re_path(r'^invoices/(?P<pk>[0-9]+)/$', views.invoice_detail, name='invoices'),
]
