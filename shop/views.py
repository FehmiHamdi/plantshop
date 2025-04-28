from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, Panier, PanierItem
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'shop/home.html')

def about(request):
    return render(request, 'shop/about.html')

def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    # Filtering
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)

    # Sorting
    sort_by = request.GET.get('sort')
    if sort_by == 'low':
        products = products.order_by('price')
    elif sort_by == 'high':
        products = products.order_by('-price')

    return render(request, 'shop/shop.html', {'products': products, 'categories': categories})

def portfolio(request):
    products = Product.objects.all()
    return render(request, 'shop/portfolio.html', {'products': products})

def contact(request):
    return render(request, 'shop/contact.html')

@login_required
def view_panier(request):
    panier, _ = Panier.objects.get_or_create(user=request.user)
    items = panier.items.all()
    return render(request, 'shop/panier.html', {'panier': panier, 'items': items})

@login_required
def add_to_panier(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    panier, _ = Panier.objects.get_or_create(user=request.user)

    panier_item, created = PanierItem.objects.get_or_create(
        panier=panier,
        product=product,
    )
    if not created:
        panier_item.quantity += 1
    else:
        panier_item.quantity = 1
    panier_item.save()

    return redirect('view_panier')

@login_required
def remove_from_panier(request, item_id):
    item = get_object_or_404(PanierItem, id=item_id)
    item.delete()
    return redirect('view_panier')

@login_required
def update_quantity(request, item_id):
    item = get_object_or_404(PanierItem, id=item_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        if quantity > 0:
            item.quantity = quantity
            item.save()
        else:
            item.delete()
    return redirect('view_panier')

