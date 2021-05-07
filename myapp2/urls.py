from django.urls import path
from myapp2.views import homepage, contacts, contact_detail

urlpatterns = [
    path("", homepage, name="home"),
    path("contact/", contacts, name="contacts"),
    path("contact/<contact_slug>/", contact_detail, name="contact_detail"),
]
