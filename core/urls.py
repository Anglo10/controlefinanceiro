from django.conf.urls import url
from core.views import controle

urlpatterns = [
    url(r'^$',controle.inicio, name="inicio"),
    url(r'^lista_categoria$',controle.listaCategoria, name="lista_categoria"),
    url(r'^nova_conta/$', controle.novaConta, name="nova_conta"),
    url(r'^nova_categoria/$', controle.novaCategoria, name="nova_categoria"),
    url(r'^editar/(?P<pk>\d+)$', controle.editarConta, name="editar"),
    url(r'^editar_categoria/(?P<pk>\d+)$', controle.editarCategoria, name="editar_categoria"),
    url(r'^categoria_editada/(?P<pk>\d+)$', controle.categoriaEditada, name="categoria_editada"),
    url(r'^dado_editado/(?P<pk>\d+)$', controle.atualizarConta, name="dado_editado"),
    url(r'^deletar/$', controle.deletarConta, name="deletar"),
    url(r'^deletar_categoria/$', controle.deletarCategoria, name="deletar_categoria")
]