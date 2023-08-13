from django.urls import path
from contato import views

app_name = "contato"

urlpatterns = [
    path("", views.index, name="index"),
    path("consulta/", views.consulta, name="consulta"),
    path("contact/<int:contato_id>/", views.contato_detalhe, name="contact"),
    path("contact/<int:contato_id>/update/", views.update, name="update"),
    path("contact/<int:contato_id>/delete/", views.delete, name="delete"),
    path("contact/create/", views.create, name="create"),
    # user
    path("user/create/", views.register, name="register"),
    path("user/login/", views.login_view, name="login"),
    path("user/logout/", views.logout_view, name="logout"),

]
