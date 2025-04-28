from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('panier/', views.view_panier, name='view_panier'),
    path('add-to-panier/<int:product_id>/', views.add_to_panier, name='add_to_panier'),
    path('remove-from-panier/<int:item_id>/', views.remove_from_panier, name='remove_from_panier'),
    path('update-quantity/<int:item_id>/', views.update_quantity, name='update_quantity'),
]
