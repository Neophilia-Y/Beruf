from django.views import View
from django.views.generic import FormView
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from . import forms


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm
        return render(request, template_name="users/login.html", context={"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                # 알아서 쿠키도 만들어주고 세션도 만들어주고
                return redirect(reverse("core:home"))
        return render(request, template_name="users/login.html", context={"form": form})


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


class SignupView(FormView):
    """Signup View class"""

    template_name = "users/signup.html"
    form_class = forms.SignupForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
