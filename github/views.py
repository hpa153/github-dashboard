from django.shortcuts import render, redirect
from pathlib import Path
import random

from account.models import Account
from github.models import Chart
from github.helpers import retrieve_data, retrieve_user_info, render_chart, display_charts

# Create your views here.
# Homepage
def homepage(request):
  user = retrieve_user_info(request)

  context = {
    "user": user
  }

  return render(request, 'pages/home.html', context)

# Dashboard page
def dashboard(request):
  user = retrieve_user_info(request)
  repos = retrieve_data(request)

  # Retrieve data from form
  if request.method == 'POST':
    repo = request.POST['repo']
    name = user['username'] + "_" + repo
    chart_style = request.POST['style']
    chart_type = request.POST['chart']

    # Check if any chart has same name
    existing_charts = Chart.objects.all()

    for chart in existing_charts:
      if chart.name == name:
        name += "_" + str(random.randint(0, 100))

    # Render the chart to display
    render_chart(request, name, repo, chart_style, chart_type)

    # and save to database
    Chart.objects.create(
      user_id = Account.objects.get(username=user['username']),
      name = name,
      repo = repo,
      path = str(Path(__file__).parent.parent) + "/uploads/charts/" + name + ".svg",
      chart_style = chart_style,
      chart_type = chart_type
    )

  # Get options for select field
  repo_list = []

  for repo in repos:
    repo_list.append(repo["name"])

  # Get charts to display 
  charts_to_display =  []

  if request.user.is_authenticated:
    charts_to_display = display_charts(user['id'])

  context = {
    "repo_list": repo_list,
    "user": user,
    "charts": charts_to_display,
  }
    
  return render(request, 'pages/dashboard.html', context)

# Repos page
def repos(request):
  user = retrieve_user_info(request)
  
  repos = retrieve_data(request)

  context = {
    "user": user,
    "repos": repos
  }
    
  return render(request, 'pages/repos.html', context)

# Users page
def users(request):
  user = retrieve_user_info(request)
  users = Account.objects.all()

  context = {
    "user": user,
    "users": users
  }
  
  return render(request, 'pages/users.html', context)

def view_user(request, user_id):
  user = retrieve_user_info(request)

  # Get user name
  name = Account.objects.get(id=user_id).username
    
  # Get charts to display  
  charts_to_display = display_charts(user_id)

  context = {
      'user': user,
      'charts': charts_to_display,
      'is_viewing_user': True,
      'username': name,
  }
  return render(request, 'pages/user_dashboard.html', context)

def delete_chart(request, chart):
  chart_to_delete = Chart.objects.get(name=chart)
  chart_to_delete.delete()

  return redirect(request.META.get('HTTP_REFERER', '/dashboard'))