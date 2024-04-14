from django.urls import path
from .views import DramaList, DramaDetails, ActorList, DirectorList, HomepageView, DramaEdit, DramaAdd, DramaDelete 
from .views import ActorAdd, ActorUpdate, ActorDelete, LoginView, AwardList, AwardAdd, AwardDelete, AwardUpdate 
from .views import DirectorList, DirectorAdd, DirectorDelete, DirectorUpdate, logout_view


urlpatterns = [
    path('drama/', DramaList.as_view(), name='drama-list'),
    path('dramas/<int:id>/', DramaDetails.as_view(), name='drama-details'),
    path('drama/<int:id>/edit', DramaEdit.as_view(), name='drama-edit'),
    path('directors/', DirectorList.as_view(), name='director-list'),
    path('directors/add/', DirectorAdd.as_view(), name='director-add'),
    path('directors/<int:id>/delete/', DirectorDelete.as_view(), name='director-delete'),
    path('directors/<int:id>/update/', DirectorUpdate.as_view(), name='director-update'),
    path('add/', DramaAdd.as_view(), name='drama-add'),
    path('drama/delete/<int:id>/', DramaDelete.as_view(), name='drama-delete'),
    path('actors/', ActorList.as_view(), name='actor-list'),
    path('actor/add/', ActorAdd.as_view(), name='actor-add'),
    path('actor/<int:id>/update/', ActorUpdate.as_view(), name='actor-update'),
    path('actor/<int:id>/delete/', ActorDelete.as_view(), name='actor-delete'),
    path('homepage/', HomepageView.as_view(), name = 'homepage'),
    path('login/', LoginView.as_view(), name='login'),
    path('awards/', AwardList.as_view(), name='award-list'),
    path('awards/add/', AwardAdd.as_view(), name='award-add'),
    path('award/<int:id>/delete', AwardDelete.as_view(), name='award-delete'),
    path('award/<int:id>/update', AwardUpdate.as_view(), name='award-update'),
    path('logout/', logout_view, name='logout'),

]