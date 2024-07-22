from django.urls import path 
from . import views
urlpatterns = [
    path('',views.Home),
    path('notes',views.get_notes),
    path('notes/<int:id>',views.get_note_by_id),
    path('notes/create',views.post_note),
    path('notes/<int:id>/update',views.update_note),
    path('notes/<int:id>/delete',views.delete_note)
]
