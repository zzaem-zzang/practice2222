from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm, CommentForm
from .models import Movie, Comment

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', pk=form.instance.pk)
    else:
        form = MovieForm()
    return render(request, 'movies/create.html', {'form': form})

def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    comments = movie.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.save()
            return redirect('movies:detail', pk=movie.pk)
    else:
        form = CommentForm()
    return render(request, 'movies/detail.html', {'movie': movie, 'comments': comments, 'form': form})

def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/update.html', {'form': form})

def delete(request, pk):
    if request.method =='POST':
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return redirect('movies:index')
    else:
        return render(request, 'movies/index.html')

def comments_delete(request, pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('movies:detail', pk=pk)