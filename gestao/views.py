from django.db.models import Sum
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import ProdutoForm, UsuarioForm
from .models import Produto, Categoria

def checar_admin(user):
    return user.is_staff

def produto_list(request):
    
    produtos = Produto.objects.all().order_by('nome')
    
    search_query = request.GET.get('q')
    if search_query:
        produtos = produtos.filter(nome__icontains=search_query)

    return render(request, 'gestao/produto_list.html', {'produtos': produtos})

@login_required
def produto_novo(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'gestao/sucesso.html')
        
    else:
            form = ProdutoForm()

    return render(request, 'gestao/produto_novo.html', {'form': form})

@login_required
def produto_edit(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    
    if request.method == "POST":
     form = ProdutoForm(request.POST, request.FILES, instance=produto)
     if form.is_valid():
         form.save()
         return redirect('produto_list')
     
    else:
         form = ProdutoForm(instance=produto)

    return render(request, 'gestao/produto_novo.html', {'form': form})

@login_required
def produto_delete(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    produto.delete()
    return redirect('produto_list')

def register(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()

            grupo_vendedores = Group.objects.get(name='Vendedores')
            usuario.groups.add(grupo_vendedores)
            
            return redirect('login')
    
    else:
        form = UsuarioForm()

    return render(request, 'registration/register.html', {'form': form})

def dashboard(request):
    total_produtos = Produto.objects.count()
    total_categorias = Categoria.objects.count()
    
    #Filtrando produtos com menos de 5 unidades em estoque
    produtos_baixo_estoque_queryset = Produto.objects.filter(quantidade__lt=5)
    
    #Contagem para o carg estoque
    baixo_estoque_count = produtos_baixo_estoque_queryset.count()

    #Somando o valor total do estoque
    valor_estoque = Produto.objects.aggregate(Sum('preco'))['preco__sum'] or 0

    contexto = {
        'total_produtos': total_produtos,
        'total_categorias': total_categorias,
        'baixo_estoque': baixo_estoque_count,
        'lista_alerta': produtos_baixo_estoque_queryset,
        'valor_estoque': valor_estoque,
        }

    return render(request, 'gestao/dashboard.html', contexto)



