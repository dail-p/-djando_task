from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from posts.api import views as api_views
from posts.views import PostsListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", PostsListView.as_view()),
    path("api/posts/", api_views.PostListView.as_view(), name="api_post_list"),
    path("api/posts/<int:pk>", api_views.PostDetailView.as_view(), name="api_post_detail"),
    path("api/posts/<int:pk>/comments/", api_views.CommentPostView.as_view(), name="api_comments_post_"),
    path("api/posts/<int:pk>/add-file/", api_views.PostUploadView.as_view(), name="api_post_upload"),
    path("api/comments/", api_views.CommentListView.as_view(), name="api_comments_list"),
    path("api/comments/<int:pk>", api_views.CommentDetailView.as_view(), name="api_comments_detail"),
    path("api/comments/<int:pk>/add-file/", api_views.CommentUploadView.as_view(), name="api_post_upload"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
