from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView, TemplateView

from users.models import CustomUser


class ProfileLoginView(TemplateView, LoginRequiredMixin):
    template_name = 'auth/profile.html'


class UserUpdateFormView(UpdateView):
    model = CustomUser
    template_name = 'auth/profile.html'
    fields = ['first_name', 'last_name', 'username', 'phone_number', 'email', 'image']
    success_url = reverse_lazy('product')

    def get_object(self, queryset=None):
        return self.request.user

    def form_invalid(self, form):
        return super().form_invalid(form)


class PasswordChangingFormView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'auth/profile.html'
    success_url = reverse_lazy('product')


