from django.contrib import admin
from .models import Category, Product, Panier, PanierItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Panier)
admin.site.register(PanierItem)

