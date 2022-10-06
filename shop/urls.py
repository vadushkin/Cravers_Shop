from django.urls import path

from shop.views import ShopHome, CategoryListView, ProductDetailView, BlogDetailView

urlpatterns = [
    path('', ShopHome.as_view(), name='home'),
    path('category/<str:slug>/', CategoryListView.as_view(), name='posts-by-category'),
    path('products/<str:slug>/', ProductDetailView.as_view(), name='product'),
    path('blogs/<str:slug>/', BlogDetailView.as_view(), name='blog'),
]
