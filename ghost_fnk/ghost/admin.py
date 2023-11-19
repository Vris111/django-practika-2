from django.contrib import admin

from .forms import ApplicationChekerForAdmin
from .models import User, Application, Category

admin.site.register(User)
admin.site.register(Category)

@admin.register(Application)
class AdminApplication(admin.ModelAdmin):
    form = ApplicationChekerForAdmin
    list_display = ['name', 'status']

