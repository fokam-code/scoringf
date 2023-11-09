from django.urls import path

from  . import views
from .views import  ArticleListView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView,Predicttest,Listescoring
urlpatterns=[
    path("",views.home,name="home"),
     path("import/",views.charger_csv,name="test"),
    path("crud/",views.crud,name="crud"),
    path("data/",views.data,name="data"),
    path("delete/",views.delete_data,name="delete"),
    path("indexc/",views.indexc,name="indexc"),
    path('login',views.login_blog,name='login'),
    path('upload/', views.upload, name = 'upload-data'),
    #
    path("scoring/", ArticleCreateView.as_view(),name="scoring"),
     path("mise/",views.mise,name="mise"),
    path("update/",views.update_data,name="update"),
    path("create/",views.create,name="create"),
    path("load/",views.charger_csv,name="load"),
    path("select/",views.selectfeature,name="selectfeature"),
    path("itemset/",views.itemset,name="itemset"),
    path("select/",views.selectfeature,name="selectfeature"),
    path("itemset/",views.itemset,name="itemset"),
    
   
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
    path('articles/update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('articles/delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
    path('test/',Predicttest.as_view() ,name='metrics'),
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-book'),
    path('update/<int:book_id>', views.update_book),
    path('delete/<int:book_id>', views.delete_book),
    path("mise/delete/",views.delete_book,name="adda"),
    path('mise/update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('mise/delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
    
]   

from django.urls import path
from . import views
from scoring.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

# urlpatterns = [
#     path('', views.index, name = 'index'),
#     path('upload/', views.upload, name = 'upload-book'),
#     path('update/<int:book_id>', views.update_book),
#     path('delete/<int:book_id>', views.delete_book)
# ]

#DataFlair
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)