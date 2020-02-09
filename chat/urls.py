from django.urls import path

from .views.index import IndexView

app_name = 'chat'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]