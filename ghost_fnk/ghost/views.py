from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View, generic
from django.views.generic import CreateView


from .forms import RegisterUserForm
from .models import Application


def index(request):
    counter_for_indx = Application.objects.filter(status__exact='D').order_by('time')[:4]
    counter_for_indx_job = Application.objects.filter(status__exact='ATJ').count()
    return render(
        request, 'index.html',
        context={'counter_for_indx': counter_for_indx, 'counter_for_indx_job': counter_for_indx_job}
    )

class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class ApplicationListView(generic.ListView):
    model = Application
    context_object_name = 'application_list'
    template_name = 'application_list.html'

class ApplicationDetailView(generic.DetailView):
    model = Application
    context_object_name = 'application'
    template_name = 'application_detail.html'
