from django.urls import path

from .views import ListsListView, DeleteEntryView, AddEntryView, AddListView

urlpatterns = [
    path('', ListsListView.as_view(), name='lists'),
    path('entries/<int:pk>/delete', DeleteEntryView.as_view(), name='delete-entry'),
    path('entries/add', AddEntryView.as_view(), name='add-entry'),
    path('add', AddListView.as_view(), name='add-list')
]