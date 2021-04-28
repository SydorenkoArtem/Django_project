from django.urls import path
from myapp.views import home, about, user_id, user

urlpatterns = [
    path("home/", home),
    path("about/", about),
    path("user/", user),
    path("user/<int:user_id>/<slug:name>", user_id, name='User name'),
]
