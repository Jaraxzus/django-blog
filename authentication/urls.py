from dj_rest_auth.registration.views import (
    RegisterView,
    ResendEmailVerificationView,
    VerifyEmailView,
)
from dj_rest_auth.views import (
    LoginView,
    LogoutView,
    PasswordResetConfirmView,
    PasswordResetView,
    UserDetailsView,
)
from django.urls import path

from . import views
from .views import email_confirm_redirect, password_reset_confirm_redirect

urlpatterns = [
    path("register/", RegisterView.as_view(), name="rest_register"),
    path(
        "register/verify-email/",
        VerifyEmailView.as_view(),
        name="account_email_verification_sent",
    ),
    path(
        "register/resend-email/",
        ResendEmailVerificationView.as_view(),
        name="rest_resend_email",
    ),
    path(
        "register/confirm_email/<str:key>/",
        views.email_confirm_redirect,
        name="account_confirm_email",
    ),
    path(
        "password/reset/",
        PasswordResetView.as_view(),
        name="rest_password_reset",
    ),
    path(
        "password/reset/confirm/<str:uidb64>/<str:token>/",
        views.password_reset_confirm_redirect,
        name="password_reset_confirm",
    ),
    path(
        "password/reset/confirm/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),
]
