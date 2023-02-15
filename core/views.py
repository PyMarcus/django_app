from typing import Any, Dict, List
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request: Any) -> HttpResponse:
    products: Product = Product.objects.all()
    to_template: Dict[str] = {
        "welcome": f'welcome {request.user}!',
        "products": products
    }
    return render(request, 'index.html', to_template)


def another_route(request: Any) -> HttpResponse:
    items: Dict[str, List] = {"items": [1, 2, 3]}
    return render(request, 'another.html', items)


def product(request: Any, id: int) -> HttpResponse:
    print(f"ID {id}")
    prod = Product.objects.get(id=id)
    prodct: Dict[str, Any] = {"product": prod}
    return render(request, 'product.html', prodct)

