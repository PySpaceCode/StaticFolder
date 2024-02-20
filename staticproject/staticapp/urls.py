from django.urls import path
from . import views
urlpatterns=[
    path("hello/",views.hello),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("service/",views.service,name="service"),
    path("/",views.dummy,name="dummy"),
    #path("hello/",views.hello),
    #book manager
    path('books/', views.book_list, name='book_list'),
    path('add_book/', views.add_book, name='add_book'),
    path("register/",views.register,name="register"),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book')
    
]
