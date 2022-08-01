from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from account.forms import SignupForm, UserEditForm
from github.views import retrieve_user_info

# Create your views here.
def sign_in(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      login(request, form.get_user())
      return redirect('home')
  else:
    form = AuthenticationForm()

  context = {
    'form': form,
  }

  return render(request, 'login.html', context)

def sign_up(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      user = form.save()

      # Log-in the user right away, then redirect home
      login(request, user)
      return redirect('home')
  else:
    form = SignupForm()

  context = {
    'form': form,
  }
  
  return render(request, 'signup.html', context)


def edit_profile(request):
  cur_user = request.user
  user = retrieve_user_info(request)

  if request.method == 'POST':
    form = UserEditForm(request.POST, request.FILES, instance=cur_user)
    
    if form.is_valid():
      form.save()

      return redirect('home')
  else:
    form = UserEditForm(instance=cur_user)

  context = {
    'form': form,
    'user': user,
    'is_media': True,
    'is_editing': True,
  }
  
  return render(request, 'edit_form.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')