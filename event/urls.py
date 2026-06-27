from rest_framework.routers import DefaultRouter
from .api.viewsets import EventListViewset,EventDetailViewset

router = DefaultRouter()
router.register(r"event-list",EventListViewset,basename='event-list')
router.register(r"event-detail",EventDetailViewset,basename='event-detail')

urlpatterns = router.urls