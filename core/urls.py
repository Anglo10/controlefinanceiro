from django.conf.urls import url
from core.views import controle

urlpatterns = [
    url(r'^$',controle.inicio, name="inicio"),
    url(r'^nova_conta/$', controle.novaConta, name="nova_conta"),
    url(r'^editar/(?P<pk>\d+)$', controle.editarConta, name="editar"),
    url(r'^dado_editado/(?P<pk>\d+)$', controle.atualizarConta, name="dado_editado"),
    url(r'^deletar/(?P<pk>\d+)$', controle.deletarConta, name="deletar")
]