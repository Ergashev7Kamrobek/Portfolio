              
from django.urls import path 
from apps.views import home, Portfolio_detailsView, BlogSinglesView, commentfunc

urlpatterns = [
    path("", home, name="home"),
    path("portfolio_details/<int:id>", Portfolio_detailsView, name="portfolio_details"),
    path("blog_single/", BlogSinglesView, name="blog_single"),
    path('post/<int:pk>/', commentfunc, name='post'),
]
    
    
    
    # path('<str:username>/', userfunc, name='user'),
    