from django.shortcuts import render
from shop. models import register_form

#insert the user in form

def register(request):

    # fatch the data from the signUp form

    #print(fname, lname, email, gender, course, uname, mobile, passw)
    
    if request.POST.get('btn2') == '2':
        date_1 = request.POST.get('date')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        course = request.POST.get('course')
        mobile = request.POST.get('mobile')
        uname = request.POST.get('uname')
        passw = request.POST.get('pass')

        #insert data in database
        ins = register_form(add_date=date_1 ,first_name=fname, last_name=lname,email=email, gender=gender, course=course, mobile=mobile, uname=uname, password=passw)
        ins.save()

        message = "Data Insert Successfully"
        print("the data save in database")
        return render(request, 'signUp.html', {'msg':message})

    elif request.POST.get('btn1') == '1':
        start_date = request.POST.get('sdate')
        end_date = request.POST.get('edate')
        if start_date <= end_date:
            #filter data date wise
            #info = register_form.objects.order_by('add_date')    
            info = register_form.objects.filter( add_date__gte=start_date,  add_date__lte=end_date)
            return render(request, 'signUp.html', {'info1':info})

        elif start_date > end_date:
            message = "please select date properly......!!!"
            return render(request, 'signUp.html', {'msg':message})
            
        else:
            message = "please select date properly......!!!"
            return render(request, 'signUp.html', {'msg':message})
                  
    else:
    
        return render(request, 'signUp.html')
        

    



    
