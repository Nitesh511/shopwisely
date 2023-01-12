from django.urls import path
from .import views
urlpatterns = [
    path('dashboard', views.dashboard),
    path('updatestatus/<int:order_id>', views.update_status),



]