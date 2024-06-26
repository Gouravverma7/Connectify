from django.urls import path,include
from accounts.views import UserRegistration,UserSearchView,ParticulartUserProfile,LogoutAPIView,UserLoginView,UserProfileView,UserChangePasswordView,SendPasswordResetEmailView,UserPasswordResetView,UserDetailView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('register/',UserRegistration.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('profile/',UserProfileView.as_view(),name='profile'),
    path('user-profile/',ParticulartUserProfile.as_view(),name='user-profile'),
    path('detail/',UserDetailView.as_view(),name='userdetail'),
    path('changepassword/',UserChangePasswordView.as_view(),name='changepassword'),
    path('send-reset-password-email/',SendPasswordResetEmailView.as_view(),name='sendresetpassemail'),
    path('reset-password/<uid>/<token>/',UserPasswordResetView.as_view(),name='reset-password'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('search/', UserSearchView.as_view(), name='user_search'),
]
