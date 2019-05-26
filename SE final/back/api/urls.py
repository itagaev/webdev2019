from django.urls import path
from api import views

urlpatterns=[
    path('competitions/',views.CompetitionList.as_view()),
    path('competitions/<int:pk>/',views.CompetitionDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
    path('competitions/<int:pk>/members',views.CompetitionMember.as_view()),
    #path('competitions/<int:pk2>/memebers/<int:pk>',views.CompetitionMemberView.as_view())
]