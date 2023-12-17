"""
URL configuration for animeList project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from animeApp.views import anime_list
from django.views.generic import RedirectView

# from django.urls.conf.static import static

urlpatterns = [
    path('', RedirectView.as_view(url='/api/animes/')),  # Redirect to your API endpoint
    path('api/animes/', include('animeApp.urls')),  # Include your API endpoints
    path('api/animes/', anime_list, name='anime_list'),
    path('admin/', admin.site.urls),
]


