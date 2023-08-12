from django.urls import path
from contato import views

app_name = 'contato'

urlpatterns = [

        path('', views.index, name= 'index'),
        path('consulta/', views.consulta, name='consulta'),

        #Contatos CRUD

        path('contact/<int:contato_id>/', views.contato_detalhe,name='contact'),
<<<<<<< HEAD
        path('contact/<int:contato_id>/update/', views.update ,name='update'),
        path('contact/<int:contato_id>/delete/', views.delete,name='delete'),
        path('contact/create/', views.create,name='create'),
=======
        path('contact/create/', views.create,name='create'),
        #path('contact/<int:contato_id>/update/', views.contato_detalhe,name='contact'),
        #path('contact/<int:contato_id>/delete/', views.contato_detalhe,name='contact'),
>>>>>>> cc44d4472d1f6704bbd8b5bcfbd4b1d3140c35fa

        ]
