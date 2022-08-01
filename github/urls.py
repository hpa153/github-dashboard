from django.urls import path
from github import views

urlpatterns = [
  path('', views.homepage, name="home"),
  path('repos', views.repos, name="repos"),
  path('users/<user_id>/', views.view_user, name='view_user'),
  path('users', views.users, name="users"),
  path('dashboard', views.dashboard, name="dashboard"),
  path('delete/<chart>', views.delete_chart, name="delete"),
]