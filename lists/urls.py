from django.urls import path

from .views import ListsListView

urlpatterns = [
    path('', ListsListView.as_view(), name='lists')
]