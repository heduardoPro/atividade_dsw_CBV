from django.contrib import admin
from .models import Cliente, Consumo, Hospedagem, Quarto

# Register your models here.

@admin.register(Hospedagem)
class HospedagemAdmin(admin.ModelAdmin):
    list_display=('data_entrada','data_saida', 'valor', 'cliente', 'quarto')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display=('nome', 'email', 'telefone', 'endereco')

@admin.register(Quarto)
class QuartoAdmin(admin.ModelAdmin):
    list_display=('apartamento','valor',)

@admin.register(Consumo)
class ConsumoAdmin(admin.ModelAdmin):
    list_display=('nome', 'data', 'valor', 'hospedagem')