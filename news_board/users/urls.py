from django.urls import path, include
from .api import *
from .views import *
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

router_user = routers.SimpleRouter()
router_user.register(r'register', RegistrationView)

router_superuser = routers.SimpleRouter()
router_superuser.register(r'super_register', CreateSuperuserView)

urlpatterns = [
    # path('register/', RegistrationView.as_view(), name='registration'),
    path('api/', include(router_user.urls)),
    path('api/', include(router_superuser.urls)),
    path('api-token-auth/', ObtainAuthToken.as_view(), name='api-token-auth'),
    path('login/', login_view, name='api-token-auth'),

]
