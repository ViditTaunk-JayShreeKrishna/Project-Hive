from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('signup/', views.signupPage, name='signup'),
#     path('login/', views.loginPage, name='login'),
#     path('logout/', views.logoutPage, name='logout'),
#     path('skills/', views.skillsPage, name='skills'),
#     path('suggestions/', views.suggestionsPage, name='suggestions'),

#     # Forgot Password URLs
#     path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
#     path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
# ]
from django.urls import path
from .views import SignupAPIView
from .views import SuggestionAPIView
from .views import SignupAPIView, CustomTokenView
from django.urls import path
from .views import ResetPasswordView
from django.urls import path, re_path
from .views import SignupAPIView, CustomTokenView, SuggestionAPIView, FrontendAppView
from django.urls import path
from .views import ProjectDetailView
from django.urls import path
from .views import generate_project_details
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.urls import path
from .views import csrf_token_view 
from core.views import FrontendAppView

urlpatterns = [
    path('signup/', SignupAPIView.as_view()),
    path('login/', CustomTokenView.as_view()),  # ✅ Custom login view
    path('suggest/', SuggestionAPIView.as_view()),
    path('reset_password/', ResetPasswordView.as_view(), name='reset-password'),
    path('get-csrf-token/', csrf_token_view),
    path("generate-project-details/", generate_project_details, name="generate_project_details"),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    re_path(r'^(?!api/).*$', FrontendAppView.as_view()),
]


