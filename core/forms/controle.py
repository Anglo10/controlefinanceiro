from core.models.controle import Conta, Categoria
from django import forms
from django.forms import ModelForm


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        exclude = ['']


class ContaForm(ModelForm):
    class Meta:
        model = Conta
        exclude = ['']