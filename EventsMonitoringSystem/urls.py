from django.contrib import admin
from django.urls import path
from events_monitoring_system import views as evs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', evs.listings, name = "listings"),
    path('edit/<list_id>', evs.edit, name = "edit"),
    path('delete/<list_id>', evs.delete, name='delete'), 
]
