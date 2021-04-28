from django.http import HttpResponse


def home(request):
    """Return response for an request route"""
    return HttpResponse("Homepage")


def products(request, product_id):
    """Return response for an request route"""
    return HttpResponse("This is a product {}".format(product_id))


def catalog(request):
    """Return response for an request route"""
    return HttpResponse("All catalog on site")
