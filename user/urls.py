from django.urls import path,re_path
from user.views import*
from user import views

urlpatterns = [
    path('userregister/',views.adduser, name='reg'),
    path("login/",UserLogin.as_view(),name="login"),
    path("logout/",views.logout_request,name="logout"),
    path("log/",UserLogout.as_view(),name="log"),
    path("userregisterlist/",UserRegisterList.as_view(),name="userregisterlist"),
    re_path(r"^detail/(?P<pk>\d+)\$",UserRegisterDetail.as_view(),name='userregisterdetail'),
    re_path(r"^update/(?P<pk>\d+)\$",UserRegisterUpdate.as_view(),name='userregisterupdate'),
    re_path(r"^booking/(?P<pk>\d+)\$",BookView.as_view(),name='booking'),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path("confirmpay/",ConfirmpayView.as_view(),name="confirmpay"),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('pay/', PaymentView.as_view(), name='pay'),
    path('profile/',UserProfile.as_view(),name="profile"),
    path('userhome/',UserHomeView.as_view(),name="userhome"),
    path('search/',views.search,name='search'),
    path("usersearch/",views.usersearch,name='usersearch'),
    path('bookeddetail/',BookedList.as_view(),name="bookeddetail"),
    path('feedback/',FeedbackView.as_view(),name='feedback'),
    path('feedlist/',FeedbackList.as_view(),name='feedlist'),

    ]