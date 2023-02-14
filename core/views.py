from typing import Any, Dict, List
from django.http import HttpResponse
from django.shortcuts import render


def index(request: Any) -> HttpResponse:
    to_template: Dict[str] = {"welcome": 'welcome!'}
    return render(request, 'index.html', to_template)


def another_route(request: Any) -> HttpResponse:
    items: Dict[str, List] = {"items": [1, 2, 3]}
    return render(request, 'another.html', items)
