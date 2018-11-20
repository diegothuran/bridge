from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^relevancia/$', views.RelevanciaList.as_view()),
    url(r'^relevancia/(?P<site>.+)$', views.RelevanciaList.as_view()),
]