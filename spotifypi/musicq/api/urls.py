from django.urls import path, include
from rest_framework import routers
from .views import SongListView, SongViewSet#, SongDetailView


router = routers.DefaultRouter()
router.register('song', SongViewSet)

urlpatterns = router.urls
	# path('', SongListView.as_view()),
	#path('<pk>', SongDetailView.as_view())