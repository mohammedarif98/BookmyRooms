from django.urls import path,re_path
from hotel.views import*
from hotel import views

urlpatterns=[
		path('roomadding/',Hotel.as_view(),name='roomadding'),
		path('roomaddedlist/',HotelDetailList.as_view(),name="roomaddedlist"),
		re_path(r"^roomaddeddetail/(?P<pk>\d+)\$",HotelDetailView.as_view(),name='roomaddeddetail'),
		re_path(r"^roomaddedupdate/(?P<pk>\d+)\$",HotelDetailUpdate.as_view(),name='roomaddedupdate'),
		path('hotelregister/',views.addhotel, name='hotelregister'),
    	path("hotelregisterlist/",HotelRegisterList.as_view(),name="hotelregisterlist"),
    	re_path(r"^hotelregisterdetail/(?P<pk>\d+)\$",HotelRegisterDetail.as_view(),name='hotelregisterdetail'),
    	re_path(r"^HotelRegisterUpdate/(?P<pk>\d+)\$",HotelRegisterUpdate.as_view(),name="hotelregisterupdate"),
    	path('hotelhome/',HotelHome.as_view(),name="hotelhome"),
    	path("oderview/",OrdersView.as_view(),name="oderview"),
    	path('hprofile/',HotelProfile.as_view(),name='hprofile')

]




