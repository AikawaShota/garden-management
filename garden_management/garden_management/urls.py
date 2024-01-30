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
