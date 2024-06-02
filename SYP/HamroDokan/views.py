from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import productmodel
from .models import profilemodel
from .models import userprofilemodel
from .models import ordermodel
from .forms import UserUpdateForm,ProfileUpdateForm,productupdateform,orderform




def signuppage(request):
    if request.method == 'POST':
        username=request.POST.get('uname')
        email=request.POST.get('email')
        password=request.POST.get('passwd')
        user_type = request.POST.get('user_type')  # Get the usertype vendor or customer
        location=request.POST.get('location') #this
        
        if not (username and email and password and user_type and location):
            return render(request,'signup.html', {'allexists': True})
        
        try:
            my_user=User.objects.create_user(username,email,password)
            
            profile = userprofilemodel(user=my_user, is_vendor=user_type == 'vendor')
            profile.save()
            return redirect('login')
            # Save additional user details based on user type
            
        except IntegrityError:
            return render(request, 'signup.html', {'username_exists': True})
    else:    
        
        return render(request,'signup.html', {})




def loginpage(request):
    if request.method == 'POST':
        username1 = request.POST.get('uname')
        password1 = request.POST.get('passwd')
        
        if not (username1 and password1):
            messages.error(request, 'Please fill in all the required fields.')
            return redirect('login')

        user = authenticate(request, username=username1, password=password1)
        if user is not None:
            login(request, user)
            # Redirect to a success page
            try:
                user_profile = userprofilemodel.objects.get(user=user)
                if user_profile.is_vendor:
                    return redirect('originalvendor')
                else:
                    return redirect('home') #home link
            except userprofilemodel.DoesNotExist:
                # Handle the case when UserProfileModel doesn't exist
                # This could be the admin user or any other user without a profile
                return redirect('userorder')  # Redirect to a generic dashboard
        else:
            # Handle invalid login
            # return an error message to the user
            return render(request, 'login.html', {'error_message':True})
    else:
        # Handle GET request for login page
        return render(request, 'login.html',{})


# This is for normal user to see the shop listed by vendorpage
@login_required(login_url='login')
def homepage(request):
    # Fetch all products added by vendors
    products = productmodel.objects.all()
    
    context = {
        'products': products,
    }
    return render(request, 'home.html', context)



def termspage(request):
    return render(request, 'terms.html', {})


def aboutmepage(request):
    return render(request, 'aboutme.html', {})


def logoutpage(request):
    logout(request)
    return redirect('login')
    


# This is for the Vendor section(next part)
@login_required(login_url='login')
def indexpage(request):
    countwk = User.objects.all().count()
    orders = ordermodel.objects.all()
    products = productmodel.objects.all()
    ordercount = ordermodel.objects.all().count()
    if request.method == 'POST':
        form = orderform(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staffmodel = request.user
            instance.save()
            return redirect('userorder')
    else:
        form = orderform()
    context={
        'orders': orders,
        'products': products,
        'form':form,
        'countwk': countwk,
        'ordercount':ordercount

    }
    
    return render(request,'VendorSection/index.html',context)



@login_required(login_url='login')
def staffpage(request):
    workers = User.objects.all()
    countwk = workers.count()
    context={
        'workers': workers,
        'countwk': countwk
        
    }
    return render(request,'VendorSection/staff.html',context)


@login_required(login_url='login')
def staff_detail(request,pk):
    workers = User.objects.filter(id=pk)
    countwk = User.objects.all().count()
    context={
        'workers': workers,
        'countwk': countwk
    }
    return render(request,'VendorSection/staff_detail.html',context)



@login_required(login_url='login')
def vendorpage(request):
    items = productmodel.objects.all()
    countwk = User.objects.all().count()
    ordercount = ordermodel.objects.all().count()
    storecount = items.count()
    if request.method == 'POST':
        form = productupdateform(request.POST,request.FILES)
        if form.is_valid():
             # Assign the current vendor to the product being added
            product = form.save(commit=False)
            product.vendor = request.user
            product.save()
            # form.save()
            return redirect('originalvendor')
    else:
        form = productupdateform

    context={
        'items': items,
        'form': form,
        'countwk': countwk,
        'ordercount':ordercount,
        'storecount':storecount
    }
    return render(request,'VendorSection/vendor.html',context)


@login_required(login_url='login')
def productdeletepage(request,pk):
    item = productmodel.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('originalvendor')
    return render(request,'VendorSection/productdelete.html')


@login_required(login_url='login')
def productupdatepage(request,pk):
    item = productmodel.objects.get(id=pk)
    if request.method == 'POST':
        form = productupdateform(request.POST,request.FILES, instance = item)
        if form.is_valid():
            form.save()
            return redirect('originalvendor')
    else:
        form = productupdateform( instance = item)
    
    context={
        'form':form,
        
    }
    
    return render(request,'VendorSection/productupdate.html',context)



@login_required(login_url='login')
def profilepage(request):
    return render(request,'VendorSection/profile.html')


@login_required(login_url='login')
def profilepage_update(request):
    
    # Get the profile instance associated with the logged-in user
    profile, created = profilemodel.objects.get_or_create(staff=request.user)

    if request.method == 'POST':
        # Update profile fields based on the form data
        user = request.user
        user.username = request.POST.get('name')
        user.email = request.POST.get('email')
        user.save()
        profile.address = request.POST.get('address')
        profile.phone = request.POST.get('phone')
        profile.image = request.FILES.get('image')  # Assuming image is uploaded

        profile.save()

        return redirect('userprofile')  # Redirect to the same page after updating

    return render(request, 'VendorSection/profilepage_update.html', {'profile': profile})



@login_required(login_url='login')
def orderpage(request):
    orders = ordermodel.objects.all()
    ordercount = ordermodel.objects.all().count()
    storecount = productmodel.objects.all().count()
    countwk = User.objects.all().count()
    context={
        'orders': orders,
        'countwk': countwk,
        'ordercount':ordercount,
        'storecount' : storecount
    }
    
    return render(request,'VendorSection/order.html',context)

