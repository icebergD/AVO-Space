from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('tutorials', views.tutorials, name='tutorials'),
    path('donate', views.donate, name='donate'),
    path('merch', views.merch, name='merch'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)