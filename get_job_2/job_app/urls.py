from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_vacancy', views.Vacancy.as_view(), name='add_vacancy'),
    path('register/', views.register, name='register'),
    path('about/<int:pk>/', views.about.as_view(), name='about'),
    path('about2', views.about2, name='about2'),
    # path('add/', views.cart_add, name='cart_add'),
    path('search/', views.searchBar, name='search'),
    # path('update_item/', views.updateItem, name='update_item'),
    path('cart', views.cart, name='cart'),
    path('basket-add/<int:product_id>', views.cart_add, name='basket_add'),
    path('delete/<int:id>', views.cart_delete, name='delete'),
    path('delete2/<int:id>', views.profile_delete, name='delete2'),
    path('profile', views.profile, name='profile'),
    path('change/<int:pk>/', views.UpdateVacancy.as_view(), name='change'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout', views.loguot_view, name='logout2')
    ]