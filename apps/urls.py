from django.contrib import admin
from django.urls import path

from apps.views import ProductListView, ProductDetailView, OrderFormView, OrderedDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='product'),
    path('category/<str:slug>', ProductListView.as_view(), name='category_list'),
    path('category', ProductListView.as_view(), name='category'),
    path('detail/<str:slug>', ProductDetailView.as_view(), name='detail'),
    path('order', OrderFormView.as_view(), name='order'),
    path('ordered/<int:pk>', OrderedDetailView.as_view(), name='ordered'),
]
