from rest_framework.routers import DefaultRouter
from support_main.v1.api import views


router = DefaultRouter()
router.register(r'tickets', views.TicketViewSet, base_name='tickets')
router.register(r'users', views.UserViewSet, base_name='users')

urlpatterns = router.urls