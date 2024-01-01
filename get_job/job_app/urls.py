from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_vacancy', views.Vacancy.as_view(), name='add_vacancy'),
    path('register/', views.register, name='register'),
    path('about/<str:pk>/', views.about.as_view(), name='about'),
    path('about2', views.about2, name='about2'),
    # path('add/', views.cart_add, name='cart_add'),
    path('search/', views.searchBar, name='search'),
    # path('update_item/', views.updateItem, name='update_item'),
    path('cart', views.cart, name='cart'),
    path('basket-add/<int:product_id>', views.cart_add, name='basket_add'),
    path('delete/<int:id>', views.cart_delete, name='delete')
    ]