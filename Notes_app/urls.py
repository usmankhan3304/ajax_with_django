from django.urls import path
from Notes_app import views

urlpatterns = [
    path('',views.index,name="home"),
    path("signup/",views.signup,name="signup"),
    path("login/",views.user_login,name="login"),
    path("logout/", views.logout_page, name="logout"),
    path("success/",views.success_page,name="success_page"),
    
]
