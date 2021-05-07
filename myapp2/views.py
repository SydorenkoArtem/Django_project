from django.shortcuts import render


def homepage(request):
    """Return response for an request route"""
    return render(request, "home.html")


def contacts(request):
    """Return response for an request route"""

    context = {
        "title": "Contacts",
        "contacts": [
            {"title": "Contact #1", "url": "contact-1"},
            {"title": "Contact #2", "url": "contact-2"},
            {"title": "Contact #3", "url": "contact-3"},
            {"title": "Contact #4", "url": "contact-4"},
            {"title": "Contact #5", "url": "contact-5"},
            {"title": "Contact #6", "url": "contact-6"},
            {"title": "Contact #7", "url": "contact-7"},
        ]
    }
    return render(request, "contacts.html", context)


def contact_detail(request, contact_slug):
    """Return response for an request route"""
    return render(request, "contact_detail.html", {"contact_slug": contact_slug})
