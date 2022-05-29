from django.urls import path
from app import views
# from engage.app.views import facedect
urlpatterns = [
    path('',views.Index, name='Index'),
    path('login.html',views.login, name ='login'),
    path('profile.html',views.profile, name ='profile'),
    path('documents.html',views.documents, name ='documents')
    # path('',views.facedect)
]