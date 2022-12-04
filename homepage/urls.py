from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsPostListView.as_view()),
    path('featured', NewsPostFeaturedView.as_view()),
    path('<slug>', NewsPostDetailView.as_view()),
]