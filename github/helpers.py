import requests
from django.contrib.auth.decorators import login_required
import pygal
from pygal.style import DefaultStyle, DarkStyle, LightStyle, DarkSolarizedStyle, LightSolarizedStyle, NeonStyle

from github.models import Chart

# Retrieve github data from API
def retrieve_data(request):
  if request.user.is_authenticated:
    github = request.user.github
  
    repo_request = requests.get("https://api.github.com/users/" + github + "/repos")
    return repo_request.json()
  else:
    return ""

# Retrieve user info
@login_required
def retrieve_user_info(request):
  user = {}
  user['id'] = request.user.id
  user['username'] = request.user.username
  user['is_auth'] = request.user.is_authenticated
  user['profile_pic'] = request.user.profile_picture

  return user

# Render chart
def render_chart(request, repo, chart_style, chart_type):
  github = request.user.github
  repo_languages = requests.get("https://api.github.com/repos/" + github + "/" + repo + "/languages").json()
  
  # Create chart and get data for chart
  chart = ""

  if chart_style == "default":
    chart_style = DefaultStyle
  elif chart_style == "dark":
    chart_style = DarkStyle
  elif chart_style == "darksolar":
    chart_style = DarkSolarizedStyle
  elif chart_style == "light":
    chart_style = LightStyle
  elif chart_style == "lightsolar":
    chart_style = LightSolarizedStyle
  else:
    chart_style = NeonStyle

  if chart_type == "bar":
    chart = pygal.HorizontalBar(style=chart_style)
  else:
    chart = pygal.Pie(inner_radius=.4, style=chart_style)
  
  # Fill chart
  for name, value in repo_languages.items():
    chart.add(name, value)
  
  return chart.render_data_uri()

# Retrieve charts to display
def display_charts(user_id):
  charts = list(Chart.objects.filter(user=user_id))
  
  charts_to_display = []

  for chart in charts:
    charts_to_display.append({
      "name": chart.name,
      "chart": chart.chart
    })

  return charts_to_display