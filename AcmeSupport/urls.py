from django.urls import path
from . import views
from .views import TicketView


urlpatterns = [
    path('login/', views.login),
    path('signup/', views.signup),
    path('ticket/', views.TicketView.as_view())
]
