from django.urls import path
from .import views

urlpatterns = [
    path('index',views.index,name="index"),
    path('bookstore',views.bookform,name="bookform"),
    path('addbook',views.addbook,name="addbook"),
    path('dashboard',views.getbook,name="addbook"),
    path('edit/<rid>',views.edit,name="edit"),
    path('delete/<rid>',views.delete,name="delete"),
    path('',views.home,name="home"),
    path('books',views.books,name="books"),
    path('register',views.register,name="register"),
    path('login',views.login_user,name="login"),
    path('contact',views.contact,name="contact")

]
