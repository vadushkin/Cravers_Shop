from django.urls import path

from shop.views import ShopHome, ProductsByCategoryListView, ProductDetailView, \
    BlogDetailView, cart, checkout, updateItem, BlogsView

urlpatterns = [
    path('', ShopHome.as_view(), name='home'),

    # static urls
    path('blogs/', BlogsView.as_view(), name='blogs'),
    path('hot-offers/', ShopHome.as_view(), name='hot-offers'),

    # blogs
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog'),

    # categories
    path('category/<slug:slug>/', ProductsByCategoryListView.as_view(), name='posts-by-category'),
    path('categories/<slug:slug>/', ProductsByCategoryListView.as_view(), name='categories'),

    # products
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='products'),

    # cart
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('update_item/', updateItem, name="update_item"),
]
