from django.urls import path
from . import views
urlpatterns = [
    path('api/table/', views.TableListCreate.as_view() ),
]