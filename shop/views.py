from django.views.generic import ListView, DetailView

from shop.models.category import Category
from shop.models.product import Product
from shop.models.social_network import Network


class ShopHome(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'shop/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cravers'
        context['networks'] = Network.objects.all()
        return context


class CategoryListView(ListView):
    model = Category
    template_name = 'shop/category.html'


class ProductDetailView(DetailView):
    context_object_name = 'product'
    template_name = 'shop/post.html'

    def get_queryset(self):
        queryset = Product.objects.filter(slug=self.kwargs['slug'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs["slug"].title()
        return context
