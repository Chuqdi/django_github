
from django.contrib import admin
from django.urls import include, path
from book.views import index, register_user,Dashboard
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", index, name="index"),
    path("login", LoginView.as_view(template_name="auth/login.html"), name="login"),
    path("register", register_user, name="register"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("dashboard", Dashboard.as_view(), name="dashboard"),

    path("book/", include("book.urls"))
]


if settings.DEBUG:
    urlpatterns+=static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )


