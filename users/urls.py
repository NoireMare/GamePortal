from django.urls import path, include
from .views import UserRegistrationView, SignInView, UserProfileView, \
    UserLogOutView, EmailVerificationView, PostsByUserView, comments_for_user_posts, approve_comment, \
    delete_comment, UserActivityView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('sign_in', SignInView.as_view(), name='log_in'),
    path('register/', UserRegistrationView.as_view(), name="user_registration"),
    path('profile/<int:pk>', UserProfileView.as_view(), name='user_profile'),
    path('', UserLogOutView.as_view(), name='user_logout'),
    path('verify/<str:email>/<str:code>', EmailVerificationView.as_view(), name='email_verify'),
    path('profile/<int:pk>/posts/', PostsByUserView.as_view(), name='user_posts'),
    path('profile/comments', login_required(comments_for_user_posts), name='comments_for_user'),
    path('profile/comment/<int:pk>/approve/', login_required(approve_comment), name='approve_comment'),
    path('profile/comment/<int:pk>/delete/', login_required(delete_comment), name='delete_comment'),
    path('profile/<int:pk>/activity', UserActivityView.as_view(), name='user_activity')
]
