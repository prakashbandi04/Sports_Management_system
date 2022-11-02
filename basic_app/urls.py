from django.urls import path
from . import views
app_name = 'basic_app'
urlpatterns = [
 path('register',views.register,name = 'register'),
 path('room_list',views.RoomListView,name = 'room'),
 path('booking_list/',views.BookingListView.as_view(),name = 'booking'),
 path('room/<category>/',views.RoomDetailView.as_view(),name = 'RoomDetailView'),
 path('search/',views.search,name='search'),
 #path('book/',views.BookingView,name = 'avail'),
 path('schedule',views.schedule,name = 'schedule'),
 path('booking_list/<int:pk>/',views.BookingDetailView.as_view(),name = "book_detail"),
  path('booking_delete/<int:pk>/',views.BookingDeleteView.as_view(),name = "book_delete"),
 path('accomodate',views.accomodate,name = 'accomodate'),
 path('user_login/',views.user_login,name = 'user_login'),
 path('athlete_list/',views.AthleteListView.as_view(),name = "list"),
 path('athlete_list/<int:pk>/',views.AthleteDetailView.as_view(),name = "detail"),
 path('result_men/',views.ResultMenListView.as_view(),name = "result_men"),
 path('result_men/<int:pk>/',views.ResultMenDetailView.as_view(),name = "result_men_detail"),
 path('result_women/',views.ResultWomenListView.as_view(),name = "result_women"),
 path('result_women/<int:pk>/',views.ResultWomenDetailView.as_view(),name = "result_women_detail"),
 path('medals/',views.MedalsListView.as_view(),name = "medals"),
 path('medals/<int:pk>/',views.MedalsDetailView.as_view(),name = "medals_detail"),
]
