from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
app_name='searchapp'

urlpatterns = [
    path('',views.movie_search,name='search'),
]