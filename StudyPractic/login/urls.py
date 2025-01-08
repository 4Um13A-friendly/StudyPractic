from django.urls import path
from .views import registrations, UserAPIView, UserHistoryCreateAPIView, UserHistoryReturnSerializer, \
    UserRegistreationAPIView, UserHistoryReturnAPIView
from django.views.generic import TemplateView

urlpatterns = [
    #path('', authterisation, name = 'authterisation'),
    #path('registration/', registrations, name = 'registration'),
    path('api/post_login/', UserAPIView.as_view(), name='your_model_api'),
    path('api/post_input/', UserHistoryCreateAPIView.as_view(), name='your_model_api'),
    path('api/get_history/', UserHistoryReturnAPIView.as_view(), name='your_model_api'),
    path('api/post_register/', UserRegistreationAPIView.as_view(), name='your_model_api'),
    path('api/get_result/', UserHistoryCreateAPIView.as_view(), name='your_model_api'),
    path('', TemplateView.as_view(template_name="vue/index.html")),
]
