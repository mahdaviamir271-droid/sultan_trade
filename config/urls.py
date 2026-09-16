from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.http import FileResponse
from django.shortcuts import redirect
from pathlib import Path
from django.conf import settings


def home(request):
    return redirect("/hero/")


def hero_image(request):
    image_path = Path(settings.BASE_DIR) / "hero-image.jpg"
    return FileResponse(
        open(image_path, "rb"),
        content_type="image/jpeg"
    )


def sections_image(request):
    image_path = Path(settings.BASE_DIR) / "sections-image.jpg"
    return FileResponse(
        open(image_path, "rb"),
        content_type="image/jpeg"
    )


def courses_image(request):
    image_path = Path(settings.BASE_DIR) / "courses-image.jpg"
    return FileResponse(
        open(image_path, "rb"),
        content_type="image/jpeg"
    )


def app_image(request):
    image_path = Path(settings.BASE_DIR) / "app-image.jpg"
    return FileResponse(
        open(image_path, "rb"),
        content_type="image/jpeg"
    )


def bottom_banner(request):
    image_path = Path(settings.BASE_DIR) / "bottom-banner.png"
    return FileResponse(
        open(image_path, "rb"),
        content_type="image/png"
    )


urlpatterns = [
    path("", home, name="home"),

    path("admin/", admin.site.urls),

    path(
        "hero/",
        TemplateView.as_view(template_name="hero.html"),
        name="hero",
    ),

    path(
        "analysis/",
        TemplateView.as_view(template_name="analysis.html"),
        name="analysis",
    ),

    path(
        "signals/",
        TemplateView.as_view(template_name="signals.html"),
        name="signals",
    ),

    path(
        "students/",
        TemplateView.as_view(template_name="students.html"),
        name="students",
    ),

    path(
        "courses/",
        TemplateView.as_view(template_name="courses.html"),
        name="courses",
    ),

    path(
        "contact/",
        TemplateView.as_view(template_name="contact.html"),
        name="contact",
    ),

    path(
        "hero-image.jpg",
        hero_image,
        name="hero_image",
    ),

    path(
        "sections-image.jpg",
        sections_image,
        name="sections_image",
    ),

    path(
        "courses-image.jpg",
        courses_image,
        name="courses_image",
    ),

    path(
        "app-image.jpg",
        app_image,
        name="app_image",
    ),

    path(
        "bottom-banner.png",
        bottom_banner,
        name="bottom_banner",
    ),
]