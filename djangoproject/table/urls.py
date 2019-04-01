from django.urls import path
from . import views

urlpatterns = [
   path('api/table/', views.tableListCreate.as_view()),
]