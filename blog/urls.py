

from django.urls import path
from . import views
urlpatterns = [
    path('details/<int:post_id>', views.post_details, name='post-details')
]