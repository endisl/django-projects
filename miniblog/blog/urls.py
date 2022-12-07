from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(),
         name='blogger-detail'),

]

urlpatterns += [
    path('<int:pk>/create/', views.CommentCreate.as_view(), name='comment-create'),
]
