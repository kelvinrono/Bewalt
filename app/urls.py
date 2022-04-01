from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('',views.home,name = 'home'),
    path('projects',views.projects,name = 'projects'),

   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)