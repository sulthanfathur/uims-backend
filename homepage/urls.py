from django.urls import path
from .views import *

urlpatterns = [
    path('', HomepageView.as_view()),
    path('news/', NewsPostListView.as_view()),
    path('news/featured', NewsPostFeaturedView.as_view()),
    path('news/<slug>', NewsPostDetailView.as_view()),
]