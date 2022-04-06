from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home),
    path('Admin_Login',views.Admin_Login),
    path('Add_Book', views.Add_Book),
    path('Open', views.Open),
    path('Update_Book',views.Update_Book),
    path('Admin_Logout', views.Admin_Logout),
    path('Admin_Register', views.Admin_Register),
    path('View_Book', views.View_Book),
    path('Delete_Book', views.Delete_Book),
    path('Delete<int:pk>', views.Delete,name='Delete'),
    path('Update_book<int:pk>', views.Update_book, name='Update_book'),
    path('Student_Login', views.Student_Login, name='Student_Login'),
    path('Student_Registers', views.Student_Registers, name='Student_Registers'),
    path('Student_Home', views.Student_Home, name='Student_Home'),
    path('Student_Logout', views.Student_Logout, name='Student_Logout'),
    path('Student_Book', views.Student_Book, name='Student_Book')
    ]