from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, ProductCategory, Basket
from users.models import User

def index(request):
	context = {'title': 'Store',}
	return render(request, 'products/index.html', context)


def products(request, category_id=None):
	products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
	context = {
		'title': 'Store - Каталог',
		'products': products,
		'categories': ProductCategory.objects.all()
	}
	return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
	product = Product.objects.get(id=product_id)
	baskets = Basket.objects.filter(user=request.user, product=product)

	if not baskets.exists():
		Basket.objects.create(user=request.user, product=product, quantity=1)
	else:
		baskets = baskets.first()
		baskets.quantity += 1
		baskets.save()

	return redirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
	basket = Basket.objects.get(id=basket_id)
	basket.delete()
	return redirect(request.META['HTTP_REFERER'])