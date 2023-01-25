from django.urls import path
from .views import *

urlpatterns = [
    path('', SponsorsListView.as_view()),
    path('gokart', GokartSponsorsListView.as_view()),
    path('ev', EVSponsorsListView.as_view()),
]