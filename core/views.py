from typing import Any, Dict, List
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
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
    # prod = Product.objects.get(id=id)
    prod = get_object_or_404(Product, id=id)
    prodct: Dict[str, Any] = {"product": prod}
    return render(request, 'product.html', prodct)


def error404(request: Any, exception) -> HttpResponse:
    template = loader.get_template('error404.html')
    return HttpResponse(content=template.render(),
                        content_type="text/html",
                        charset="utf-8",
                        status=404)
