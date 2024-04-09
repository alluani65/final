from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from .views import add_movie,edit_movie,delete_movie,post_review,profile,edit_profile,change_password
app_name='userloginapp'

urlpatterns = [
     path('register/',views.register_user,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('detail/<int:movie_id>/',views.movie_detail,name='detail'),
    path('edit/<int:movie_id>/',login_required(edit_movie),name='edit'),
    path('delete/<int:movie_id>/',login_required(delete_movie),name='delete'),
    path('add/',login_required(add_movie),name='add'),
    path('review/<int:movie_id>/',login_required(post_review),name='review'),
    path('profile/',login_required(profile),name='profile'),
    path('edit_profile/',login_required(edit_profile),name='edit_profile'),
    path('change_password/',login_required(change_password),name='change_password'),
]