from django.urls import path
from authorization.views import SongShareObtainTokenPairView, RegisterView, ChangePasswordView, UpdateProfileView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', SongShareObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='authorization_register'),
    path('change_password/<int:pk>', ChangePasswordView.as_view(), name='authorization_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='authorization_update_profile'),
]
