
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from. import views
# from .views import add_movie,edit_movie,delete_movie,post_review,profile,edit_profile,change_password
app_name='finalapp'

urlpatterns = [
    path('',views.all_movie_genere,name='index'),
    path('<slug:gslug>/',views.all_movie_genere,name='genere'),
    path('<slug:gslug>/<slug:mslug>/',views.genere_detail,name='genere_detail'),

]