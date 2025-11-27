from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'validade') # Colunas da tabela
    search_fields = ('nome',) # Barra de pesquisa
    list_filter = ('validade',) # Filtro lateral por data