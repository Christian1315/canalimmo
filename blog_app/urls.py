from django.urls import path
from blog_app import views

urlpatterns = [
    # ======= CHRISTIAN =========#
    path('show-blog-page/',views.showBlogPage,name="blog_dtail"),
    path('blog-detail/',views.showBlogDetail,name="showBlogDetail"),
]