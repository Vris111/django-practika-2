from django.urls import path
from . import views
#from .views import RegisterDoneView, RegisterUserView, user_activate

urlpatterns = [
    path('', views.index, name='index'),
    # path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    # path('accounts/register/', RegisterUserView.as_view(), name='register'),
    # path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
]
