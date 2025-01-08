from django.urls import path
from .views import registrations, UserHistoryCreateAPIView, UserHistoryReturnSerializer, UserHistoryReturnAPIView, UserLoginSerializer, UserLoginView, UserRegistrationView
from django.views.generic import TemplateView

urlpatterns = [
    #path('', authterisation, name = 'authterisation'),
    #path('registration/', registrations, name = 'registration'),
    path('api/post_login/', UserLoginView.as_view(), name='your_model_api'),
    path('api/post_input/', UserHistoryCreateAPIView.as_view(), name='your_model_api'),
    path('api/get_history/', UserHistoryReturnAPIView.as_view(), name='your_model_api'),
    path('api/post_register/', UserRegistrationView.as_view(), name='your_model_api'),
    path('api/get_result/', UserHistoryCreateAPIView.as_view(), name='your_model_api'),
    path('', TemplateView.as_view(template_name="vue/index.html")),
]
