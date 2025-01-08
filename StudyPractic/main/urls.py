from django.urls import path
from .views import solve, history

urlpatterns = [
    path('', solve, name = 'solve'),
    path('history/', history, name = 'history')
]
