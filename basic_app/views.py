from django.shortcuts import render
from .forms import UserForm,UserProfileInfoForm,availform
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView,FormView
from basic_app import models
from django.http import HttpResponse
from django.core.mail import send_mail
from basic_app.booking_fnc import avail
class AthleteListView(ListView):
    context_object_name = 'athletes'
    model = models.UserProfileInfo
    paginate_by = 5
    ordering = ['id']
    template_name = 'basic_app/athlete_list.html'
class AthleteDetailView(DetailView):
    context_object_name = "athlete_detail"
    model = models.UserProfileInfo
    template_name = 'basic_app/athlete_detail.html'
class ResultMenListView(ListView):
    context_object_name = 'result_men'
    model = models.Result_Men
    ordering = ['id']
    paginate_by = 5
    template_name = 'basic_app/result_men.html'
class ResultMenDetailView(DetailView):
    context_object_name = "result_men_detail"
    model = models.Result_Men
    template_name = 'basic_app/result_men_detail.html'
class ResultWomenListView(ListView):
    context_object_name = 'result_women'
    model = models.Result_Women
    paginate_by = 5
    ordering = ['id']
    template_name = 'basic_app/result_women.html'
class ResultWomenDetailView(DetailView):
    context_object_name = "result_women_detail"
    model = models.Result_Women
    template_name = 'basic_app/result_women_detail.html'
class MedalsListView(ListView):
    context_object_name = 'medals'
    model = models.Medals
    paginate_by = 5
    template_name = 'basic_app/medals.html'
class MedalsDetailView(DetailView):
    context_object_name = 'medals_detail'
    model = models.Medals
    template_name = 'basic_app/medals_detail.html'
def RoomListView(request):
    room = models.Room.objects.all()[0]
    room_categories = dict(room.Categories)
    room_values = room_categories.values()
    room_list = []
    for room_category in room_categories:
        room = room_categories.get(room_category)
        room_url = reverse('basic_app:RoomDetailView',kwargs={'category':room_category})
        room_list.append((room,room_url))
    context = {'room_list':room_list,}
    return render(request,'basic_app/room_list.html',context)
class BookingListView(ListView):
    model = models.Booking
    context_object_name = "booking_list"
    template_name = 'basic_app/booking_list.html'
class BookingDetailView(DetailView):
    model = models.Booking
    context_object_name = "booking_detail"
    template_name = 'basic_app/booking_detail.html'
# class SchoolUpdateView(UpdateView):
#     fields = ('Room','check_in','check_out')
#     model = models.Booking
class BookingDeleteView(DeleteView):
    context_object_name = 'bookings'
    model = models.Booking
    template_name = 'basic_app/booking_delete.html'
    success_url = reverse_lazy('index')
def index(request):
    return render(request,'basic_app/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in. Nice!")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def schedule(request):
    return render(request,'basic_app/schedule.html')
def accomodate(request):
    return render(request,'basic_app/accomodate.html')
class RoomDetailView(View):
    def get(self,request,*args,**kwargs):
        category = self.kwargs.get('category',None)
        form = availform()
        room_list  = models.Room.objects.filter(Category = category)
        if len(room_list)>0:
            room = room_list[0]
            room_category = dict(room.Categories).get(room.Category,None)
            return render(request,"basic_app/room_detail_view.html",{"category":room_category,'form':form})
        else:
            return HttpResponse(' category rooms Does not exit')
    def post(self,request,*args,**kwars):
        category = self.kwargs.get('category',None)
        book_form=availform(request.POST)
        room_list  = models.Room.objects.filter(Category = category)
        if book_form.is_valid():
            book_form = book_form.cleaned_data
        avail_rooms = []
        print("hi")
        print("fi"+str(room_list))
        for room in room_list:
            print("i"+str(room_list))
            print(book_form)
            print(type(book_form['check_in']),book_form['check_out'])
            if avail.check_avail(room,book_form['check_in'],book_form['check_out']):
                avail_rooms.append(room)
        if len(avail_rooms) > 0:
            r = avail_rooms[0]
            b = models.Booking.objects.create(Athlete = request.user,Room = r,check_in = book_form['check_in'],check_out = book_form['check_out'])
            #b.save(request.user)
            print(request.user)
            booked = True
            return HttpResponse(b)
        else:
            return HttpResponse("All rooms are filled")

def BookingView(request):
      booked = False
      if request.method == 'POST':
          book_form = availform(data=request.POST)
          if book_form.is_valid:
              room_list  = models.Room.objects.filter(Category = book_form['room_category'].value())
              avail_rooms = []
              print("hi")
              print(book_form['room_category'].value())
              print("fi"+str(room_list))
              for room in room_list:
                  print("i"+str(room_list))
                  print(book_form)
                  print(type(book_form['check_in'].value()),book_form['check_out'].value())
                  if avail.check_avail(room,book_form['check_in'].value(),book_form['check_out'].value()):
                      avail_rooms.append(room)
              if len(avail_rooms) > 0:
                  r = avail_rooms[0]
                  b = models.Booking.objects.create(Athlete = request.user,Room = r,check_in = book_form['check_in'].value(),check_out = book_form['check_out'].value())
                  #b.save(request.user)
                  print(request.user)
                  booked = True
              else:
                  print(book_form.errors)
                  print("All rooms are booked")
      else:
            book_form = availform()
      return render(request,"basic_app/avail_form.html",{"book_form":book_form,"booked":booked})

def search(request):
    if request.method == 'POST':
        searched = request.POST['search']
        athlete = models.UserProfileInfo.objects.filter(user__username__icontains = searched)
        return render(request,"basic_app/search.html",{'searched':searched,'athlete':athlete})
    else:
        return render(request,"basic_app/search.html",{})
def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            send_mail('Registered','Successfully signed-up. Have a great tournament','chundurimanohar2509@gmail.com',[request.POST['email']])

            # Save User Form to Database
            user = user_form.save()
            print(request.POST['email'])
            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'basic_app/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'basic_app/login.html', {})
