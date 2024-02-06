"""
URL configuration for garden_management project.

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

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView

# MEDIA関連
from .settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path("admin/", admin.site.urls),
    # PWA
    path(
        "sw.js", (
            TemplateView.as_view(
                template_name="sw.js", content_type="application/javascript"
            )
        ),
        name="sw.js"
    ),
    path("", RedirectView.as_view(url="/authentication/login")),
    path("authentication/", include("authentication.urls")),
    path("plant-management/", include("plant_management.urls")),
    path("help/", include("help.urls")),
]

# "settings.py"で"DEBUG=True"時のMEDIA（画像配信）の設定
if DEBUG:
    urlpatterns += static(
        MEDIA_URL, document_root=MEDIA_ROOT
    )
