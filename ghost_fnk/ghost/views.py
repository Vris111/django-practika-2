from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import View, generic
from django.views.generic import CreateView, DeleteView, TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import RegisterUserForm
from .models import Application
from django.core.exceptions import ValidationError

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

class ApplicationCreate(PermissionRequiredMixin, CreateView):
    model = Application
    fields = ['name', 'description', 'category', 'image']
    permission_required = 'add_application'
    template_name = 'application_form.html'

    def clean_image(self):
        image = self.cleaned_data.get("image")
        image_size = image.size
        str_file = str(image)
        if str_file.endswith('.jpg') and image_size <= 2097152:
            return image
        elif str_file.endswith('.jpeg') and image_size <= 2097152:
            return image
        elif str_file.endswith('.png') and image_size <= 2097152:
            return image
        elif str_file.endswith('.bpm') and image_size <= 2097152:
            return image
        else:
            raise ValidationError(
                "Error: "
                "The file must have the following formats: jpg, jpeg, png, bmp and no more than 2MB in size."
            )


class ApplicationDelete(PermissionRequiredMixin, DeleteView):
    model = Application
    success_url = '/ghost/applications'
    permission_required = 'delete_application'
    template_name = 'application_form.html'
    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("application-delete", kwargs={"pk": self.object.pk})
            )

class FilterApplications(TemplateView, LoginRequiredMixin):
    template_name = 'application_list.html'
    def get(self, request):
        application_status = request.GET.get('status')

        if application_status:
            application_list = Application.objects.filter(status=application_status).order_by('time')
        else:
            application_list = Application.objects.all().order_by('time')

        context = {
            'application_list': application_list
        }
        return render(request, self.template_name, context)
