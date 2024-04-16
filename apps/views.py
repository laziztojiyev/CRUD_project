from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, FormView

from apps.forms import ProductOrderModelForm, ProductModelForm
from apps.models import Product, Category, ProductImages, Order


class ProductListView(ListView):
    model = Product
    template_name = 'apps/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_slug = self.request.path.split('/')[-1]
        if category_slug:
            return Product.objects.filter(category__slug=category_slug)
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductImageView(TemplateView):
    model = ProductImages
    template_name = 'apps/product_detail.html'
    context_object_name = 'product_image'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'apps/product_detail.html'
    context_object_name = 'details'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class OrderFormView(FormView):
    form_class = ProductOrderModelForm
    template_name = 'apps/product_detail.html'

    def form_valid(self, form):
        obj = form.save()
        return redirect('ordered', obj.pk)


class OrderedDetailView(DetailView):
    template_name = 'apps/ordered_page.html'
    queryset = Order.objects.all()
    context_object_name = 'order'
