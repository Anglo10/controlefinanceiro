from django.contrib import admin
from core.models.controle import Categoria, Conta

class CategoriaAdmin(admin.ModelAdmin):
    model = Categoria

class ContaAdmin(admin.ModelAdmin):
    model = Conta

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Conta, ContaAdmin)

