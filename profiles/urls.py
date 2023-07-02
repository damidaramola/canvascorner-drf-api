from django.urls import path
from profiles import views

"""
add url paths to access class based views 
"""
urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
]