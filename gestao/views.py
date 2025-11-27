from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProdutoForm
from .models import Produto

def produto_list(request):
    
    produtos = Produto.objects.all().order_by('nome')
    
    search_query = request.GET.get('q')
    if search_query:
        produtos = produtos.filter(nome__icontains=search_query)

    return render(request, 'gestao/produto_list.html', {'produtos': produtos})

def produto_novo(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'gestao/sucesso.html')
        
    else:
            form = ProdutoForm()

    return render(request, 'gestao/produto_novo.html', {'form': form})

def produto_edit(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    
    if request.method == "POST":
     form = ProdutoForm(request.POST, instance=produto)
     if form.is_valid():
         form.save()
         return redirect('produto_list')
     
    else:
         form = ProdutoForm(instance=produto)

    return render(request, 'gestao/produto_novo.html', {'form': form})

def produto_delete(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    produto.delete()
    return redirect('produto_list')






