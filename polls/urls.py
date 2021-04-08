from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]

'''
# GENERIC URLS

    path('generic', views.IndexView.as_view(), name='index'),
    path('generic/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('generic/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('generic/<int:question_id>/vote/', views.vote, name='vote'),
'''
