from django.http import HttpResponse
from django.shortcuts import render, redirect
from core.models.controle import Conta,Categoria

def inicio(request):
    dados = {}
    dados['lista_conta'] = Conta.objects.all()
    return render(request, 'core/lista_conta.html', dados)