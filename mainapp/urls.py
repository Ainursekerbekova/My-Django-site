from django.urls import include, path

from .import views

urlpatterns = [
    #home page
    path('', views.index, name='index'),

    #register
    path('/register/', views.UserFormView.as_view(), name='register'),

    #profile
    path('profile/((?P<user_id>[0-9]+)/', views.profile, name='profile'),

    #post details
    path('post/(?P<pk>[0-9]+)/details', views.DetailView.as_view(), name='details'),

    #show all posts
    path('posts/', views.PostView.as_view(), name='posts'),

    #like the post
    path('like/(?P<post_id>[0-9]+)/(?P<after>[a-z]+)', views.LikePost, name='post_like'),

    #save the post
    path('save/(?P<post_id>[0-9]+)/(?P<after>[a-z]+)', views.SavePost, name='post_save'),

    #Post/add
    path('post/add/', views.PostCreate.as_view(), name='add_post'),

    #update Post by id Post/2/
    path('post/(?P<pk>[0-9]+)/update', views.PostUpdate.as_view(), name='update_post'),

    #Post/2/delete
    path('post/(?P<pk>[0-9]+)/delete/', views.PostDelete.as_view(), name='delete_post')
]
