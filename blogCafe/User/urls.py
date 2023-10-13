from django.urls import path
from User import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', LogoutView.as_view(template_name='User/logout.html'), name="Logout"),
    path('edit/', views.edit, name="Edit")
]