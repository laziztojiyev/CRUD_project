
from django.contrib import admin
from django.urls import path

from users.views import ProfileLoginView, UserUpdateFormView, PasswordChangingFormView

urlpatterns = [
    path('profile', ProfileLoginView.as_view(), name='profile'),
    path('profile/update', UserUpdateFormView.as_view(), name='profile_update'),
    path('profile/update_password', PasswordChangingFormView.as_view(), name='password_update'),
]
