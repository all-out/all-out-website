# basic rendering tools
from django.shortcuts import render, redirect
from django.http import HttpResponse

# user authentication
from django.contrib.auth.decorators import (
    login_required,
    user_passes_test,
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout,
)


def login(request):

    # if a user is already logged in, redirect to the front page
    if request.user.is_authenticated():
        return redirect('home')

    # if the hit to this URL was a POST (not GET or DELETE or whatever)
    if request.method == 'POST':

        # create a blank context dictionary for some reason
        context = {}

        # attempt to authenticate the user
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])

        # if the user is found in the database
        if user is not None:

            # and the user's account is active
            if user.is_active:

                # then go ahead and log the user in and redirect to front page
                auth_login(request, user)
                return redirect('home')

            # if the user's account is not active
            else:

                # reload the login page and display error message
                context['error'] = 'Account deactivated.'
                return render(request, 'profile/login.html', context)

        # if this user doesn't exist in the database
        else:

            # reload the login page and display error message
            context['error'] = 'Username or password not found.'
            return render(request, 'profile/login.html', context)

    # if the request method was not POST
    else:
        return render(request, 'profile/login.html', {})


def logout(request):
    auth_logout(request)
    return redirect('home')
