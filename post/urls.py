from django.urls import path
from . import views
from .views import create_comment, home ,blog,postdetail,userdetail,save_comment


urlpatterns = [
# path('search', search, name="search"),
path('',home ,name = "home"),
path('blog/',blog,name ="blog"),
path('create_comment/<int:cid>/',create_comment, name ="create_comment"),
path('post/<int:cid>/',postdetail , name='postpage'),
path('user/<int:cid>/',userdetail , name='userpage'),
path('save_comment/<int:cid>/',save_comment , name = 'savecomment'),
]
