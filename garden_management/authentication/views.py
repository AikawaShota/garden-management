from . import forms
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views


class SignUpView(generic.CreateView):
    form_class = forms.SignUpForm
    template_name = 'authentication/signup.html'
    success_url = reverse_lazy('lend:equipment-list')

    def form_valid(self, form):
        user = form.save()
        self.object = user
        return redirect(self.get_success_url())


class LoginView(auth_views.LoginView):
    template_name = 'authentication/login.html'
    authentication_form = forms.LoginForm


class LogoutView(auth_views.LogoutView):
    template_name = 'authentication/logout.html'
    next_page = 'authentication:logout'
