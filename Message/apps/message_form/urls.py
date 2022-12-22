from django.urls import re_path
from message_form import views
urlpatterns = [
    re_path(r'^send/', views.message_form)
]