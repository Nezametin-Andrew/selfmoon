from django.urls import path
from .views import BalanceView


urlpatterns = [
    path('', BalanceView.as_view(), name='account_balance'),
]