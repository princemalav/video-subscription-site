from django.urls import path
from .views import MemberSelectView

app_name = 'memberships'
urlpatterns=[
    path('',MemberSelectView.as_view(),name='select')
]
