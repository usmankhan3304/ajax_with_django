from django.urls import path
from Notes_app import views

urlpatterns = [
    path('',views.index,name="home"),
    path("signup/",views.signup,name="signup")
    
]
