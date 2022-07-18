from django.shortcuts import render
import requests
import pygal
from pygal.style import DarkSolarizedStyle

# Create your views here.
# Retrieve data from API
def retrieve_data():
  repo_request = requests.get("https://api.github.com/users/hpa153/repos")
  return repo_request.json()

# Homepage
def homepage(request):

  context = {
  }

  return render(request, 'pages/home.html', context)

# Languages page
def languages(request):
  repos = retrieve_data()

  # Get options for select field
  repo_list = []

  for repo in repos:
    repo_list.append(repo["name"])

  # Create chart and get data for chart
  pie_chart = pygal.Pie(inner_radius=.4, style=DarkSolarizedStyle)
  
  # Get selected repo
  repo_name = ""

  if 'repo' in request.GET:
    repo_name = request.GET["repo"]
  else:
    repo_name = repo_list[0]
  
  repo_languages = requests.get("https://api.github.com/repos/hpa153/" + repo_name + "/languages").json()
  
  # Fill chart
  for name, value in repo_languages.items():
    pie_chart.add(name, value)
  
  pie_chart.render_to_file("./static/charts/pie_chart.svg")

  context = {
    "repo_list": repo_list,
    "current_repo": repo_name,
  }
    
  return render(request, 'pages/languages.html', context)

# Repos page
def repos(request):
  repos = retrieve_data()

  context = {
    "repos": repos
  }
    
  return render(request, 'pages/repos.html', context)

# Sizes page
def sizes(request):
  repos = retrieve_data()

  bar_chart = pygal.HorizontalBar(style=DarkSolarizedStyle)

  for repo in repos:
    label = repo["name"]
    size = repo["size"]
    bar_chart.add(label, size)
  
  bar_chart.render_to_file("./static/charts/bar_chart.svg")

  context = {
  }
  
  return render(request, 'pages/sizes.html', context)
