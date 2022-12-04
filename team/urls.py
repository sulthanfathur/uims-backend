from django.urls import path
from .views import *

urlpatterns = [
    path('', TeamListView.as_view()),
    path('gokart', GokartListView.as_view()),
    path('ev', EVListView.as_view()),
    path('marketing', MarketingListView.as_view()),
]