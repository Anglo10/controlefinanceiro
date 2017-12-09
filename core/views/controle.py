from core.forms.controle import CategoriaForm, ContaForm
from django.shortcuts import render, redirect
from core.models.controle import Conta,Categoria

def inicio(request):
    dados = {}
    dados['lista_conta'] = Conta.objects.all()
    return render(request, 'core/lista_conta.html', dados)

def listaCategoria(request):
    dados = {}
    dados['lista_categoria'] = Categoria.objects.all()
    return render(request, 'core/lista_categoria.html', dados)

#recupera os dados
def novaConta(request):
    dados = {}
    dados['form'] = ContaForm
    conta = ContaForm(request.POST)
    if conta.is_valid():
        conta.save()
    return render(request, 'core/nova_conta.html',dados)

#atualiza
def contaCriada(request, pk):
    conta = Conta.objects.get(pk=pk)
    conta = ContaForm(request.POST or None, instance=conta)
    if conta.is_valid():
        conta.save()
    return redirect('inicio')
    
#recupera os dados
def atualizarConta(request,pk):
    dados = {}
    conta = Conta.objects.get(id=pk)
    dados['form'] = ContaForm(instance=conta)
    dados['pk'] = pk
    return render(request, 'core/atualizar_dados.html', dados)

#atualiza
def editarConta(request, pk):
    conta = Conta.objects.get(pk=pk)
    form = ContaForm(request.POST or None, instance=conta)
    if form.is_valid():
        form.save()
    return redirect('inicio')


def deletarConta(request, pk):
    conta = Conta.objects.get(id=pk)
    conta.delete()
    return redirect('inicio')

def novaCategoria(request):
    dados={}
    dados['form'] = CategoriaForm
    categoria = CategoriaForm(request.POST)
    if categoria.is_valid():
        categoria.save()
    return render(request, 'core/nova_categoria.html', dados)

def categoriaCriada(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    categoria = CategoriaForm(request.POST or None, instance=categoria)
    if categoria.is_valid():
        categoria.save()
    return redirect('lista_categoria')

def editarCategoria(request, pk):
    dados = {}
    categoria = Categoria.objects.get(id=pk)
    dados['form'] = CategoriaForm(instance=categoria)
    dados['pk'] = pk
    return render(request, 'core/editar_categoria.html', dados)



def categoriaEditada(request,pk):
    categoria = Categoria.objects.get(pk=pk)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if form.is_valid():
        form.save()
    return redirect('lista_categoria')

def deletarCategoria(request,pk):
    categoria = Categoria.objects.get(id=pk)
    categoria.delete()
    return redirect('lista_categoria')
