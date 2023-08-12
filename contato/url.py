from django.urls import path
from contato import views

app_name = 'contato'

urlpatterns = [

        path('', views.index, name= 'index'),
        path('consulta/', views.consulta, name='consulta'),

        #Contatos CRUD

        path('contact/<int:contato_id>/', views.contato_detalhe,name='contact'),
        path('contact/<int:contato_id>/update/', views.update ,name='update'),
        path('contact/<int:contato_id>/delete/', views.delete,name='delete'),
        path('contact/create/', views.create,name='create'),

        ]
