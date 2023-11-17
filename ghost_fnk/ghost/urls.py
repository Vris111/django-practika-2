from django.urls import path, include
from . import views
from .views import RegisterUser, index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('register/', RegisterUser.as_view(), name='register'),
    path('applications/', views.ApplicationListView.as_view(), name='applications'),
    path('applications/<int:pk>', views.ApplicationDetailView.as_view(), name='application-detail'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
