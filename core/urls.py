from django.conf.urls import url
from core.views import controle
urlpatterns = [
    url(r'^$',controle.inicio, name="inicio"),
]