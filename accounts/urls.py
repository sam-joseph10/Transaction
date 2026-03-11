from django.urls import path
from accounts.views import *

urlpatterns = [
    path('', landing, name='landing'),
    path('ca-dashboard/', ca_dashboard, name='ca_dashboard'),
    path('customer-dashboard/', customer_dashboard, name='customer_dashboard'),
    path("logout/", logout_view, name="logout"),
]