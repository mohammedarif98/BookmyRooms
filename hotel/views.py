from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,TemplateView,DetailView,UpdateView,View
from django.contrib.auth import authenticate,login,logout
from hotel.forms import HotelDetailForm,HotelRegisterForm,ExtendedHotelForm
from hotel.models import HotelDetailModel,HotelRegisterModel
from user.models import BookModel
from django.contrib.auth.forms import AuthenticationForm 



# Create your views here.
class Hotel(CreateView):
	template_name="roomadding.html"
	form_class=HotelDetailForm
	success_url="/hotel/roomaddedlist/"


class HotelDetailList(ListView):
	template_name="roomaddedlist.html"
	model=HotelDetailModel
	context_object_name="hotellist"

class HotelDetailView(DetailView):
	template_name="roomaddeddetail.html"
	model=HotelDetailModel

class HotelDetailUpdate(UpdateView):
	template_name="roomaddedupdate.html"
	model=HotelDetailModel
	fields=["hotel_name","room_type","room_facility","price","room_images","hotel_location","contact_no","email"]
	success_url="/hotel/roomdetaillist"

def addhotel(request):
	if request.method=="POST":
		form=HotelRegisterForm(request.POST)
		extend_form=ExtendedHotelForm(request.POST,request.FILES)

		if form.is_valid() and extend_form.is_valid():
			user=form.save()
			extended_profile=extend_form.save(commit=False)
			extended_profile.user=user
			extended_profile.save()

			username_var=form.cleaned_data.get('username')
			password_var=form.cleaned_data.get('password1')
			user=authenticate(username=username_var,password=password_var)

			login(request,user)
			return redirect ('login')
	else:
		form=HotelRegisterForm(request.POST)
		extend_form=ExtendedHotelForm(request.POST,request.FILES)

	context={"form":form,"extend_form":extend_form}
	return render(request,'hotelregister.html',context)


class HotelRegisterList(ListView):
	template_name="hotelregisterlist.html"
	model=HotelRegisterModel
	context_object_name="hotelreglist"

class HotelRegisterDetail(DetailView):
	template_name="hotelregisterdetail.html"
	model=HotelRegisterModel

class HotelRegisterUpdate(UpdateView):
	template_name="hotelregisterupdate.html"
	model=HotelRegisterModel
	fields=["contact_no","hotel_image"]
	success_url="/hotel/hotelregisterlist/"



class HotelHome(TemplateView):
	template_name="hotelhome.html"

class OrdersView(View):
	template_name="orderview.html"

	def get(self,request):

		user_data=HotelRegisterModel.objects.get(user=request.user)
		hotel_assigned=user_data.user.username
		hotel_data=BookModel.objects.filter(hotel_booked=hotel_assigned)

		context={

				'data':BookModel.objects.filter(hotel_booked=hotel_assigned)
		}

		return render(request,self.template_name,context)


class HotelProfile(View):
	template_name="hprofile.html"

	def get(self,request):
		user=request.user
		data=HotelRegisterModel.objects.get(user=user)
		contact_no=data.contact_no
		hotel_name=data.hotel_name
		hotel_image=data.hotel_image
		context={'user':user,'contact_no':contact_no,'hotel_name':hotel_name,'hotel_image':hotel_image}
		return render(request,self.template_name,context)
