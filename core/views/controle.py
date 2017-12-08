from core.forms.controle import CategoriaForm, ContaForm
from django.shortcuts import render, redirect
from core.models.controle import Conta,Categoria

def inicio(request):
    dados = {}
    dados['lista_conta'] = Conta.objects.all()
    return render(request, 'core/lista_conta.html', dados)

#recupera os dados
def novaConta(request):
    dados = {}
    dados['form'] = ContaForm
    conta = ContaForm(request.POST)
    if conta.is_valid():
        conta.save()
    return render(request, 'core/nova_conta.html',dados)

    
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
    if form.is_valid:
        form.save()
        return redirect('inicio')


def deletarConta(request, pk):
    conta = Conta.objects.get(id=pk)
    conta.delete()
    return redirect('inicio')
