from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.urls import reverse_lazy
from django.views import View
#from django.views.generic import CreateView, TemplateView
#from .forms import RegisterUserForm
#from django.core.signing import BadSignature
#from .models import User
#from .utilities import signer

def index(request):
    return render(
        request, 'index.html'
    )

class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

# class RegisterUserView(CreateView):
#     model = User
#     template_name = 'ghost/register_user.html'
#     form_class = RegisterUserForm
#     success_url = reverse_lazy('ghost:register_done')

# def user_activate(request, sign):
#    try:
#        username = signer.unsign(sign)
#    except BadSignature:
#        return render(request, 'ghost/bad_signature.html')
#    user = get_object_or_404(User, username=username)
#    if user.is_activated:
#        template = 'ghost/user_is_activated.html'
#    else:
#        template = 'ghost/activation_done.html'
#        user.is_activated = True
#        user.is_active = True
#        user.save()
#    return render(request, template)
#
# class RegisterDoneView(TemplateView):
#    template_name = 'ghost/register_done.html'

