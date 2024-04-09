from django.urls import path
from django.contrib.auth.decorators import login_required
from. views import list_favourite,add_favourite,remove_favourite
app_name='userapp'

urlpatterns = [
    path('favourite/',login_required(list_favourite),name='favourite'),
    path('add_favourite/<int:movie_id>/',login_required(add_favourite),name='add_favourite'),
    path('remove_favourite/<int:movie_id>/',login_required(remove_favourite),name='remove_favourite'),
]