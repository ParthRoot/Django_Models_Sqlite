from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

#insert the user in form
  


def register(request):

    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    gender = request.POST.get('gender')
    course = request.POST.get('course')
    mobile = request.POST.get('mobile')
    uname = request.POST.get('uname')
    passw = request.POST.get('pass')

    print(fname, lname, email, gender, course, uname, mobile, passw)
    

    return render(request, 'signUp.html')

    