from django.urls import path, include
from .views import PostsListView, SinglePostView, create_post, EditPostView, delete_post
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', PostsListView.as_view(), name='posts_list'),
    path('category/<int:category>', PostsListView.as_view(), name='posts_by_category'),
    path('post/<int:pk>', SinglePostView.as_view(), name='post_details'),
    path('posts/page/<int:page>', PostsListView.as_view(), name='posts_per_page'),
    path('post/create', login_required(create_post), name='create_post'),
    path('post/<int:pk>/edit', login_required(EditPostView.as_view()), name='change_post'),
    path('post/<int:pk>/delete', login_required(delete_post), name='delete_post'),

]
