
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View,TemplateView,ListView,DetailView,UpdateView,CreateView
from user.forms import*
from user.models import UserRegisterModel,BookModel
from hotel.models import HotelDetailModel
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.contrib.auth.models import User
from django.conf import settings
import requests

from django.shortcuts import render
from bookmyrooms.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


# Create your views here.
razorpay_client = razorpay.Client(
	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))



class PaymentView(View):
	template_name="payment.html"

	def get(self,request):
		data=BookModel.objects.last()
		amount=int(data.price)*100
		currency = 'INR'
		# amount = 20000  # Rs. 200
 
		# Create a Razorpay Order
		razorpay_order = razorpay_client.order.create(dict(amount=amount,
			currency=currency,payment_capture='0'))
 
		# order id of newly created order.
		razorpay_order_id = razorpay_order['id']
		callback_url = '/user/paymenthandler/'
 
		# we need to pass these details to frontend.
		context = {'amount_rupee':data.price}
		context['razorpay_order_id'] = razorpay_order_id
		context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
		context['razorpay_amount'] = amount
		context['currency'] = currency
		context['callback_url'] = callback_url
 
		return render(request,self.template_name, context=context)
 
 
# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):
 
	# only accept POST request.
	if request.method == "POST":
		try:
           
			# get the required parameters from post request.
			payment_id = request.POST.get('razorpay_payment_id', '')
			razorpay_order_id = request.POST.get('razorpay_order_id', '')
			signature = request.POST.get('razorpay_signature', '')
			params_dict = {
				'razorpay_order_id': razorpay_order_id,
				'razorpay_payment_id': payment_id,
				'razorpay_signature': signature
			}
 
			# verify the payment signature.
			result = razorpay_client.utility.verify_payment_signature(
				params_dict)
			if result is None:
				# amount = 20000  # Rs. 200
				data=BookModel.objects.last()
				amount=int(data.price)*100
				try:
 
					# capture the payemt
					razorpay_client.payment.capture(payment_id, amount)
					data=BookModel.objects.last()
					hotel_name=data.hotel_booked
					price=data.price
					room_type=data.room_type
					booking_date=data.booking_date
					days=data.days
					data.payment_status=True
					data.save()
 
					# render success page on successful caputre of payment
					return render(request, 'paymentsuccess.html')
				except:
 
					# if there is an error while capturing payment.
					return render(request, 'paymentfail.html')
			else:
 
				# if signature verification fails.
				return render(request, 'paymentfail.html')
		except:
 
			# if we don't find the required parameters in POST data
			return HttpResponseBadRequest()
	else:
		# if other than POST request is made.
		return HttpResponseBadRequest()



class UserLogout(TemplateView):
	template_name="log.html"

def adduser(request):
	if request.method=="POST":
		form=UserRegisterForm(request.POST)
		extend_form=ExtendedUserForm(request.POST,request.FILES)

		if form.is_valid() and extend_form.is_valid():
			user=form.save()
			extended_profile=extend_form.save(commit=False)
			extended_profile.user=user
			extended_profile.save()

			sub=forms.UserRegisterForm(request.POST)
			fname=str(sub["first_name"].value())
			lname=str(sub["last_name"].value())
			subject='wellcome to book my rooms'
			message='hi %s %s, successfully registered' %(fname,lname)
			recepient = str(sub['email'].value())
			send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently =False)



			username_var=form.cleaned_data.get('username')
			password_var=form.cleaned_data.get('password1')
			user=authenticate(username=username_var,password=password_var)

			login(request,user)
			return redirect ('userhome')
	else:
		form=UserRegisterForm(request.POST)
		extend_form=ExtendedUserForm(request.POST,request.FILES)

	context={"form":form,"extend_form":extend_form}
	return render(request,'userregister.html',context)



class UserLogin(View):
	def get(self,request):
		form=AuthenticationForm()
		context={'form':form}
		return render(request,'login.html',context)

	def post(self,request):
		username=request.POST.get('username')
		password=request.POST.get('password')
		recaptcha_response = request.POST.get('g-recaptcha-response')
		data = {
			'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
			'response': recaptcha_response
			}
		r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
		result = r.json()
        
		if result['success']:
			user=authenticate(username=username,password=password)
			login(request,user,backend='django.contrib.auth.backends.ModelBackend')

		# user=authenticate(username=username,password=password)
 		#login(request,user,backend='django.contrib.auth.backends.ModelBackend')

			if user is not None :
				login(request,user)
				if user.is_superuser == True and user.is_staff == True:
					return redirect('adminhome')
				if user.is_staff == True and user.is_superuser == False:
					return redirect('hotelhome')
				if user.is_staff == False and user.is_superuser == False:
					return redirect ('userhome')
			else:
				form=AuthenticationForm()
				context={'form':form}
				return render(request,'userhome.html',context)

def logout_request(request):
	logout(request)
	return redirect("bookmyrooms")


class UserRegisterList(ListView):
	template_name="userregisterlist.html"
	model=UserRegisterModel
	context_object_name="userreglist"

class UserRegisterDetail(DetailView):
	template_name="userregisterdetail.html"
	model=UserRegisterModel

class UserRegisterUpdate(UpdateView):
	template_name="userregisterUpdate.html"
	model=UserRegisterModel
	fields=["dob","mobile_no"]
	success_url="/user/userregisterlist/"




def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password_reset_email.txt"
                    c = {
                    "email":user.email,
                    'domain':'127.0.0.1:8000',
                    'site_name': 'Website',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password_reset.html", context={"password_reset_form":password_reset_form})




class BookView(View):
	template_name="booking.html"
	def get(self,request,pk):

		data=HotelDetailModel.objects.get(id=pk)
		current_user=str(request.user.username)
		hotel_booked=data.hotel_name
		price=data.price
		room_type=data.room_type
		date_form=BookForm()

		context={

			'user':current_user,'hotel_booked':hotel_booked,'price':price,'date_form':date_form
		}


		print(context)
		return render(request,self.template_name,context)
	
	def post(self,request,pk):

		data=HotelDetailModel.objects.get(id=pk)
		user=str(request.user.username)
		Days=request.POST.get('days')
		date=request.POST.get('booking_date')
		price=data.price
		room_type=data.room_type
		hotel_booked=data.hotel_name
		price=int(Days)*int(data.price)

		BookModel.objects.create(
			user=user,
			hotel_booked=hotel_booked,
			price=price,
			room_type=room_type,
			days=Days,
			booking_date=date)

		return redirect ('confirmpay')

class ConfirmpayView(View):
	template_name="confirmpay.html"
	def get(self,request):
		data=BookModel.objects.filter(user=request.user).last()
		user=str(request.user)
		hotel_booked= data.hotel_booked
		price=data.price
		Days=data.days
		booking_date=data.booking_date
		room_type=data.room_type

		context={

				'hotel_booked':hotel_booked,'price':price,'Days':Days,'booking_date':booking_date,'room_type':room_type,'user':user

		}

		return render(request,self.template_name,context)


class UserProfile(View):
	template_name="profile.html"

	def get(self,request):
		user=request.user
		data=UserRegisterModel.objects.get(user=user)
		dob=data.dob
		mobile_no=data.mobile_no
		context={'user':user,'dob':dob,'mobile_no':mobile_no}
		return render(request,self.template_name,context)


class UserHomeView(TemplateView):
	template_name="userhome.html"

# class UserSearch(ListView):
# 	template_name="usersearch.html"
# 	model=HotelDetailModel
# 	context_object_name="hotellist"


def search(request):
	if request.method=='POST':
		hotel_search=request.POST.get('search')
		status=HotelDetailModel.objects.filter(hotel_name=hotel_search)
		if status==None:
			pass
		else:
			return render(request,'search.html',{'status':status})
 


def usersearch(request):
	if request.method=='POST':
		hotel_search=request.POST.get('usersearch')
		status=HotelDetailModel.objects.filter(hotel_name=hotel_search)
		if status==None:
			pass
		else:
			return render(request,'usersearch.html',{'status':status})


class BookedList(ListView):
	template_name="bookeddetail.html"
	model=BookModel
	context_object_name="booklist"

class FeedbackView(CreateView):
	template_name='feedback.html'
	form_class=AddFeedbackForm
	success_url='/user/feedback/'

class FeedbackList(ListView):
	template_name='feedlist.html'
	model=AddFeedbackModel
	context_object_name='feedlist'
