from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Home, About, Contact_Form, Contact_info, Edit_Data, Delete_data

urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact_Form, name='contact'),  
    path('contact_info/', Contact_info, name='contact_info'),
    path('delete/<int:pk>', Delete_data, name='delete'),
    path('edit/<int:pk>', Edit_Data, name='edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
