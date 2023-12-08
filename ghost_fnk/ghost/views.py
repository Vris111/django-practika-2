from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import View, generic
from django.views.generic import CreateView, DeleteView, TemplateView, UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import RegisterUserForm
from .models import Application, Category
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
    template_name = 'application_list.html'


@login_required()
def ApplicationListView(request):
    user = request.user
    template_name = 'application_list.html'
    if user:
        application_list = Application.objects.filter(user=request.user).order_by('time')
    else:
        application_list = Application.objects.all().order_by('time')

    context = {
        'application_list': application_list
    }
    return render(request, template_name, context)


class ApplicationDetailView(generic.DetailView):
    model = Application
    context_object_name = 'application'
    template_name = 'application_detail.html'


class ApplicationCreate(CreateView):
    model = Application
    fields = ['name', 'description', 'category', 'image']

    template_name = 'application_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ApplicationCreate, self).form_valid(form)

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
        except Exception:
            return HttpResponseRedirect(
                reverse("application-delete", kwargs={"pk": self.object.pk})
            )


class FilterApplications(TemplateView, LoginRequiredMixin):
    template_name = 'application_list.html'

    def get(self, request):
        application_status = request.GET.get('status')

        if application_status:
            application_list = Application.objects.filter(status=application_status, user=request.user).order_by('time')
        else:
            application_list = Application.objects.all().order_by('time')

        context = {
            'application_list': application_list
        }
        return render(request, self.template_name, context)


class CategorysAdmin(generic.ListView):
    template_name = 'categories_list_admin.html'
    model = Category


class CategoryCreate(CreateView):
    model = Category
    fields = ['name']
    template_name = 'category_form.html'
    success_url = '/ghost/categories'

class CategoryDelete(DeleteView):
    model = Category
    permission_required = 'delete_category'
    template_name = 'category_conf_delete.html'
    success_url = '/ghost/categories'
    def catg_del(self):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception:
            return HttpResponseRedirect(
                reverse("category-delete", kwargs={"pk": self.object.pk})
            )
class ATJChange(UpdateView):
    model = Application
    fields = ['comm']
    template_name = 'change_conf.html'
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.status ='ATJ'
        instance.save()
        return redirect('applications')

class DChange(UpdateView):
    model = Application
    fields = ['image_status']
    template_name = 'change_conf.html'
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.status ='D'
        instance.save()
        return redirect('applications')





