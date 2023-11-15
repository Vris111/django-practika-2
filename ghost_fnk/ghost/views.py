from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


def index(request):

    return render(
        request, 'index.html'
    )

class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

