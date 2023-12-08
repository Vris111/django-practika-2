from django.urls import path
from . import views
from .views import RegisterUser, index, FilterApplications
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('applications/', views.ApplicationListView, name='applications'),
    path('applications/<int:pk>', views.ApplicationDetailView.as_view(), name='application-detail'),
    path('application/create/', views.ApplicationCreate.as_view(), name='application-create'),
    path('application/<int:pk>/delete/', views.ApplicationDelete.as_view(), name='application-delete'),
    path('applications/filter/', FilterApplications.as_view(), name='applications-filter'),
    path('categories/', views.CategorysAdmin.as_view(), name='categories'),
    path('categories/create/', views.CategoryCreate.as_view(), name='category-create'),
    path('categories/delete/<int:pk>', views.CategoryDelete.as_view(), name='category-delete'),
    path('application/<int:pk>/status-change-ATJ/', views.ATJChange.as_view(), name='status-change-ATJ'),
    path('application/<int:pk>/status-change-D/', views.DChange.as_view(), name='status-change-D'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)