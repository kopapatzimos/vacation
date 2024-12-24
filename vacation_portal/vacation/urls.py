from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("", views.dashboard_view, name="dashboard"),
    path('signup/', views.sign_up, name='signup'),
    path('submit-request/', views.submit_vacation_request, name='submit_request'),

]
