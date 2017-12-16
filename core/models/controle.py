from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class Categoria(models.Model):
    nome = models.CharField("Nome", max_length=100, blank=False)
    ativa = models.BooleanField("Ativa", default=True)

    def __str__(self):
        return self.nome


class Conta(models.Model):
    descricao = models.CharField("Descrição", max_length=100, blank=False)
    categoria = models.ForeignKey(Categoria, verbose_name="Categoria", blank=False)
    valor = models.DecimalField("Valor", max_digits=9, decimal_places=2, blank=False)
    vencimento = models.DateField("Vencimento", blank=False)

    def __str__(self):
        return self.descricao

