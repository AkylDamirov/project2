from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

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
    path('logout', views.loguot_view, name='logout2'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_complete'),
    ]
# path('reset/<uidb64>/<token>/',
#      auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_form.html'),
#      name='password_reset_confirm'),