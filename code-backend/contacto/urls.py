# contacto/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Mapea la raíz de api/contacto/ a la función contact_form_submit en views.py
    path('', views.contact_form_submit, name='submit_contact_form'),
]