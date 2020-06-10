from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms
# Create your views here.
class SignUp(CreateView):
    # no () since not creating a class but to add attribute
    form_class = forms.UserCreateForm
    # reverse_lazy waits for "submit", not just reverse
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
