# from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

from produto import models


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 10


class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'


class AdicionarAoCarrinho(View):
    pass


class RemoverDoCarrinho(View):
    pass


class Carrinho(View):
    pass


class Finalizar(View):
    pass
