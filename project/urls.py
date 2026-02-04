"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse


def home(request):
    return HttpResponse('''
        <h1 style="text-align:center;" >Home</h1>
        <hr>
        <header>
            <ul style="display: flex; justify-content: center; list-style: none; padding: 0; margin: 0; gap: 20px;">
                <li><a style="text-decoration:none; color:black;" href="admin/">admin</a></li>
                <li><a style="text-decoration:none; color:black;" href="admin/contact/contact/">contacts</a></li>
                <li><a style="text-decoration:none; color:black;" href="admin/contact/category/">categories</a></li>
            </ul>
        </header>
    ''')


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
