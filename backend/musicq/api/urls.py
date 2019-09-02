from django.urls import path
from .views import SongListView#, SongDetailView

urlpatterns = [
	path('', SongListView.as_view()),
	#path('<pk>', SongDetailView.as_view())
]