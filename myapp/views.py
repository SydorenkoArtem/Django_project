from django.http import HttpResponse


def home(request):
    """Return response for an request route"""
    return HttpResponse("Homepage")


def about(request):
    """Return response for an request route"""
    return HttpResponse("About site")


def user(request):
    """Return response for an request route"""
    return HttpResponse("All users")


def user_id(request, user_id, name=''):
    """Return response for an request route"""
    return HttpResponse("This is a user #{}. {}".format(user_id, "Name of this user is {}".format(
            name) if name else "This is unnamed user"))
