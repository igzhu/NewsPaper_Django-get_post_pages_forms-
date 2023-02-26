from django.urls import path
from .views import PostsList, PostDetails, PostSearch

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetails.as_view()),
    path('search/', PostSearch.as_view()),
]