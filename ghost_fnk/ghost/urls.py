from django.urls import path, include
from . import views
from .views import RegisterUser, index


urlpatterns = [
    path('', index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('register/', RegisterUser.as_view(), name='register'),
    path('applications/', views.ApplicationListView.as_view(), name='applications'),
    path('applications/<int:pk>', views.ApplicationDetailView.as_view(), name='application-detail'),
]
