from django.urls import path

from .views import AccountView, DashboardView, LoginView, LogoutView, RegisterView, ProfileView


app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('account/', AccountView.as_view(), name='account'),
    path('<str:username>/', ProfileView.as_view(), name='profile'),
]
