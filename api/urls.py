import imp
from django.urls import path, include
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
            path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
            path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
            path("register", views.CreateUserAPIView.as_view(), name="sign_up"),
            path("provider", views.ProviderAPIView.as_view(), name="provider"),
            path("provider-CRUD/<int:pk>", views.ProviderDetailAPIView.as_view(), name="provider_crud"),
            path("bank", views.BankAPIView.as_view(), name="bank"),
            path("bank-CRUD/<int:pk>", views.BankDetailAPIView.as_view(), name="bank_crud"),
            path("bankaccount", views.BankAccountAPIView.as_view(), name="bankaccount"),
            path("bankaccount/create", views.BankAccountCreateAPIView.as_view(), name="bankaccount"),
            path("bankaccount-CRUD/<int:pk>", views.BankAccountDetailAPIView.as_view(), name="bankaccount_crud"),
]