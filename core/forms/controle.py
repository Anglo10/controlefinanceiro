from core.models.controle import Conta, Categoria
from django import forms
from django.forms import ModelForm


class CategoriaForm(ModelForm):
    model = Categoria


class ContaForm(ModelForm):
    model = Conta