from django.contrib import admin
from. models import Movie,Genere,Review
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
class Genereadmin(admin.ModelAdmin):
    list_fields=['genere','slug']
    prepopulated_fields={'slug':('genere',)}

admin.site.register(Genere,Genereadmin)

class Movieadmin(admin.ModelAdmin):
    list_fields=['title','slug']
    prepopulated_fields={'slug':('title',)}
    list_display=('title', 'date', 'genere', 'added_by')
    search_fields = ('title', 'actors')
    list_filter = ('genere', 'added_by')

admin.site.register(Movie,Movieadmin)
class Reviewadmin(admin.ModelAdmin):
    list_display=['movie','user','rating']
admin.site.register(Review,Reviewadmin)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'date_joined')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

