from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect,HttpResponseBadRequest,HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import Reviewform,TicketForm
from .models import review,movie,show
from django.shortcuts import render
from django.views.generic import CreateView,DetailView
from show.forms import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
import stripe
from django.core.mail import EmailMessage
import time
from django.core.mail import send_mail
from django.conf import settings
import socket
from datetime import date
socket.getaddrinfo('localhost', 8080)

def sendmail(li,data):
    subject="Ticket Confirmation"
    message=f"Dear customer,\n\n{data.name} Booking is confirmed for the movie {data.show.movie} on {date}|{data.show.time}\nseat-coordinates \nseat_number:{data.seat_no}\nTheatre Address:{data.show.theatre}|{data.show.theatre.theatre_address} url:{data.show.location_url}\n Thank you for booking the ticket"
    from_email='ga21meb0b22@student.nitw.ac.in'
    recipient_list=li
    send_mail(subject,message,from_email,recipient_list)

class Signup(CreateView):
    form_class = UserCreateForm
    template_name = 'signup.html'
    success_url = reverse_lazy('index')


class Login(CreateView):
    form_class = UserCreateForm
    template_name = 'signup.html'
    success_url = reverse_lazy('index')
    
    
def profile(request):
    user=User.objects.get(username=request.user)
    book=booking.objects.filter(user=request.user)
    t=book.count()
    
    context={
        'form':user,
        'book':book,
        'tcount':t
    }
    return render(request,'profile.html',context)
   
   
    
@login_required    
def index(req):
    movies=movie.objects.all()
    context={
        'movies':movies
    }
    return render(req,'index.html',context)
@login_required
def mdetail(req,pk):
    movies=movie.objects.get(movie_id=pk)
    if(req.method=='POST'):
        c_form=Reviewform(req.POST)
        if c_form.is_valid():
            instance=c_form.save(commit=False)
            instance.user=req.user
            instance.movie=movies
            instance.save()
            return redirect('movie_detail',pk=movies.movie_id)
    else:
        c_form=Reviewform()
        
    context={
        'movies':movies,
        'c_form':c_form
    }
    return render(req,'movie_detail.html',context)

@login_required
def like(req,pk):
    user=req.user
    review=review.objects.get(rev_id=pk)
    current_likes=review.likes
    print(current_likes)
    liked=like.objects.filter(user=req.user,review=review).count()
    if not liked:
        liked=like.objects.create(user=user,review=review)
        current_likes=current_likes+1
    else:
        liked=like.objects.filter(user=user,review=review).delete()
        current_likes=current_likes-1
    review.likes=current_likes
    review.save()
    print(current_likes)
    return HttpResponseRedirect(reverse('movie_detail',args=[movie.movie_id]))  

@login_required
def theatre_list(req,pk):
    li=show.objects.filter(movie_id=pk)
    context={
        't_list':li
    }
    return render(req,'theatre_list.html',context)






class show_details(DetailView) :
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['form'] = TicketForm
        show_id = self.kwargs['pk']
        Show = show.objects.get(pk=show_id)
        context['tickets_booked'] = booking.objects.filter(show=Show)
        return context

    context_object_model = 'show'
    model = show
    template_name = 'book.html'
    


@login_required
def bookticket(request,pk):  
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.show=show.objects.get(show_id=pk)
            book.user = request.user
            seat_no = book.seat_no
            
                 
            if booking.objects.filter(seat_no=seat_no,show=book.show).exists():
                return HttpResponse("<h1>already ticket has been booked</h1>")
            book.save()
            return redirect('pay')
        else:
            return redirect('book-ticket',pk=pk)
                  
    else:
        form = TicketForm()
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
 

    

@login_required    
def pay(request):
    data=booking.objects.filter(user=request.user)
    l=len(data)
    context={
        'data':data[l-1]
    }
    return render(request,'payment.html',context)    
@login_required    
def confirm(request):
    data=booking.objects.filter(user=request.user)
    l=len(data)
    print(data[l-1].user.email)
    context={
        'data':data[l-1]
    }
    
    li=[request.user.email]
    # sendmail(li,data[l-1])
    return render(request,'conformation.html',context)    
    
    