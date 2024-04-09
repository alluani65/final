from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.urls import reverse
from finalapp.models import Movie, Review,Genere
from finalapp.forms import MovieForm, ReviewForm
from django.contrib.auth.forms import PasswordChangeForm
from finalapp.forms import ProfileForm


# Create your views here.
def register_user(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('userloginapp:register')  
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return redirect('userloginapp:register')  
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.first_name = firstname  
                user.last_name = lastname 
                user.save()
                messages.info(request, 'You have been successfully registered')
                return redirect('userloginapp:login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('userloginapp:register') 

    return render(request,'register.html')

def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('finalapp:index')
        else:
            messages.info(request,'Invalid User')
            return redirect('userloginapp:register')

    return render(request,'login.html')



def logout_user(request):
    auth.logout(request)
    return redirect('finalapp:index')

def movie_detail(request,movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request,'movie_detail.html',{'movie':movie})

# @login_required()
# def add_movie(request):
#     if request.method == 'POST':
#         form = MovieForm(request.POST or None, request.FILES)
#         if form.is_valid():
#             movie = form.save(commit=False)
#             movie.added_by = request.user
#             movie.save()
#             return redirect('finalapp:index')
#     else:
#         form = MovieForm()
#     return render(request, 'add_movie.html', {'form': form})

@login_required()
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST or None, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.added_by = request.user
            movie.save()
            genre_slug = movie.genere.slug
            movie_slug = movie.slug
            return redirect(reverse('finalapp:genere_detail', args=[genre_slug, movie_slug]))
    else:
        form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})

@login_required()
def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if movie.added_by != request.user:
        return redirect('finalapp:index', movie_id=movie.id)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('finalapp:index', movie_id=movie.id)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'edit_movie.html', {'form': form, 'movie': movie})

@login_required()
def delete_movie(request, movie_id):
    if request.method=='POST':
        movie = get_object_or_404(Movie, id=movie_id)
        if movie.added_by == request.user:
            movie.delete()
            return redirect('finalapp:index')
    return render(request,'delete.html')

@login_required
def post_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            return redirect('finalapp:index')
    else:
        form = ReviewForm()
    return render(request, 'review.html', {'form': form, 'movie': movie})

#user


@login_required
def profile(request):
    profile = request.user
    return render(request, 'profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('userloginapp:profile')
    else:
        form = ProfileForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form})


@login_required
def change_password(request):
    user=request.user
    if request.method == 'POST':
        form = PasswordChangeForm(user,request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password changed successfully.')
            return redirect('userloginapp:login')
    else:
        form = PasswordChangeForm(user)
    return render(request, 'change_password.html', {'form': form})