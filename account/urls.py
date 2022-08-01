from django.urls import path
from account import views

urlpatterns = [
  path('signin', views.sign_in, name="signin"),
  path('signup', views.sign_up, name="signup"),
  path('edit-profile', views.edit_profile, name="edit-profile"),
  path('logout', views.logout_view, name='logout'),
]

