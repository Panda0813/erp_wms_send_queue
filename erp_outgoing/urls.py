from django.conf.urls import url, include
from erp_outgoing import views

urlpatterns = [
    url(r'^erp_to_wms$', views.send_data_to_wms),
]
