from django.shortcuts import render


def homepage(request):
    """Return response for an request route"""
    return render(request, "home.html")


def product_list(request):
    """Return response for an request route"""

    context = {
        "title": "Products List",
        "products": [
            {"title": "Product #1", "url": "product-1"},
            {"title": "Product #2", "url": "product-2"},
            {"title": "Product #3", "url": "product-3"},
            {"title": "Product #4", "url": "product-4"},
            {"title": "Product #5", "url": "product-5"},
            {"title": "Product #6", "url": "product-6"},
            {"title": "Product #7", "url": "product-7"},
        ]
    }
    return render(request, "product.html", context)


def product_detail(request, product_slug):
    """Return response for an request route"""
    return render(request, "product_detail.html", {"product_slug": product_slug})
