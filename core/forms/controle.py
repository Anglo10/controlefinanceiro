from core.models.controle import Conta, Categoria
from django import forms
from django.forms import ModelForm


class CategoriaForm(ModelForm):
    nome = forms.CharField(label="Nome", widget=forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model = Categoria
        exclude = ['']


class ContaForm(ModelForm):
    descricao = forms.CharField(label="Descrição", widget=forms.TextInput(attrs={"class":"form-control"}))
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label="Categoria", widget=forms.Select(attrs={"class":"form-control"}))
    valor = forms.DecimalField(label="Valor", widget=forms.NumberInput(attrs={"class":"form-control"}))
    vencimento = forms.DateField(label="Vencimento", widget=forms.TextInput(attrs={"class":"form-control", "type":"date"}))
    class Meta:
        model = Conta
        exclude = ['']