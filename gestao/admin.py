from django.contrib import admin
from .models import Produto, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)  # Colunas da tabela.
    search_fields = ('nome',)  # Barra de pesquisa.

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade', 'validade') # Colunas da tabela.
    search_fields = ('nome',) # Barra de pesquisa.
    list_filter = ('validade', 'categoria') # Filtro lateral por data e categoria.
    