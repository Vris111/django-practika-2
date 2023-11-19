from django.urls import path, include
from . import views
from .views import RegisterUser, index, FilterApplications
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('register/', RegisterUser.as_view(), name='register'),
    path('applications/', views.ApplicationListView, name='applications'),
    path('applications/<int:pk>', views.ApplicationDetailView.as_view(), name='application-detail'),
    path('application/create/', views.ApplicationCreate.as_view(), name='application-create'),
    path('application/<int:pk>/delete/', views.ApplicationDelete.as_view(), name='application-delete'),
    path('applications/filter/', FilterApplications.as_view(), name='applications-filter')

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)