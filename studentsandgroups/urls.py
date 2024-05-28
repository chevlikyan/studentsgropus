from django.urls import path
from .views import StudentListView, GroupDetailView

urlpatterns = [
    path('', StudentListView.as_view(), name='home'),
    path('group/<slug:slug>/', GroupDetailView.as_view(), name='group_detail'),
]
