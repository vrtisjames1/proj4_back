from django.urls import path
from . import views

urlpatterns = [
    path('api/connect4', views.Connect4List.as_view(), name='connect4_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/connect4/<int:pk>', views.Connect4Detail.as_view(), name='connect4_detail'), # api/contacts will be routed to the ContactDetail view for handling
]