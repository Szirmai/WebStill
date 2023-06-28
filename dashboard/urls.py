from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='dash-home'),
    path('offer-requests/<str:pk>', views.offerRequest, name='offer-reque'),
    path('contact-us/<str:pk>', views.Contact, name='contacts'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('offer-requests/', views.offerRequests, name='offer-requests'),
    path('contact-us/', views.Contacts, name='contact-us'),
]
