from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
    LoginView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Aplicacion.Sistema.urls')),  # Asegúrate de que la ruta de 'Sistema' esté correcta
    path('accounts/', include('django.contrib.auth.urls')),  # Incluye las vistas predeterminadas de autenticación de Django

     path('reset/password_reset/', auth_views.PasswordResetView.as_view(
        template_name='contraseñas/password_reset_form.html',
        email_template_name='contraseñas/password_reset_email.html',
        subject_template_name='contraseñas/password_reset_subject.txt',
    ), name='password_reset'),

    # Ruta que confirma que el correo fue enviado
    path('reset/password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='contraseñas/password_reset_done.html',
    ), name='password_reset_done'),

    # Ruta para la página donde el usuario cambia su contraseña (con uid y token)
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='contraseñas/password_reset_confirm.html',
    ), name='password_reset_confirm'),

    # Ruta que confirma que el restablecimiento de la contraseña fue exitoso
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='contraseñas/password_reset_complete.html',
    ), name='password_reset_complete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
