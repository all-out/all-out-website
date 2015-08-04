# basic rendering tools
from django.shortcuts import render
from django.http import HttpResponse

from moviepicker.models import Movie


def home(request):
    return render(request, 'moviepicker/home.html')


def get_results(request):
    context = {}
    choices = Movie.objects.filter(shown=False).order_by('-vote_count', 'title')
    context['choices'] = choices
    if choices.count() > 0:
        return render(request, 'moviepicker/choices.html', context)
    else:
        return HttpResponse('')


def vote_toggle(request):
    # get the watcher and the movie from the POST request
    watcher = request.user.watcher
    movie = Movie.objects.get(id=int(request.POST['movie_id']))

    # VOTE: (the user hasn't voted for this movie yet)
    if movie not in watcher.votes.all():
        movie.votes.add(watcher)

    # UNVOTE: (the user has already voted for this movie)
    else:
        movie.votes.remove(watcher)

    # save the movie to update its vote_count and return a success
    movie.save()
    return HttpResponse(status=200)


def watcher_details(request):
    pass


def watcher_votes(request):
    pass
