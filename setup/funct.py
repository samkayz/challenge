from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import get_user_model, authenticate, login as dj_login, logout as s_logout
from django.contrib.auth import user_logged_in
from django.shortcuts import render, redirect, get_object_or_404
from user.models import *
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist



## Main Class of the Projects ##
class Main:
    
    ## Function to do the Login ##
    def do_login(self, request, email, password):
        
        # Check if the email is follow email format
        if '@' not in email:
            messages.error(request, "Not a valid email")
            return redirect('/')
        
        elif User.objects.filter(email=email).exists():
            user = authenticate(email=email, password=password)
            
            if user is not None:
                
                ## get Login User Info #
                # u = get_object_or_404(User, email=email)
                ## Login ##
                dj_login(request, user)
                
                ## Set Session Expiring Date and login User ###
                # request.session.set_expiry(600)
                messages.success(request, f'Welcome to challenge portal')
                return redirect('/home')
            else:
                messages.error(request, 'Invalid Login Credentials')
                return redirect('/')
        else:
            messages.error(request, "User doesn't exist")
            return redirect('/')
        
        
    """Function that handle the User record Creation"""
    def create_user(self, request, firstname, lastname, email, mobile, dob, gender, nationality):
        """Check if Email or Mobile number already exist on the system"""
        if UserManagement.objects.filter(Q(email=email) | Q(phone=mobile)).exists():
            messages.warning(request, "User with this email or mobile number already exist within the system")
            return HttpResponseRedirect('/home')
        else:
            """Create new user"""
            create_new = UserManagement(firstname=firstname, 
                                        lastname=lastname, 
                                        email=email, 
                                        phone=mobile, 
                                        dob=dob, 
                                        nationality=nationality, 
                                        gender=gender)
            create_new.save()
            messages.success(request, "User created successfully")
            return HttpResponseRedirect('/home')
        
    
    """Fuction that do record update"""
    def updateRecord(self, request, id, firstname, lastname, email, mobile, gender, dob, nationality):
        """Get the user record instance"""
        updUser = UserManagement.objects.filter(id=id)
        """Update the instance of the record"""
        updUser.update(firstname=firstname, 
                       lastname=lastname, 
                       email=email, 
                       phone=mobile, 
                       gender=gender, 
                       dob=dob, 
                       nationality=nationality)
        """Display message and redirect back"""
        messages.success(request, "Record Updated successfully")
        return HttpResponseRedirect('/home')
    
    """Delete Record"""
    def deleteRecord(self, id):
        delt = UserManagement.objects.filter(id=id)
        delt.delete()
        pass
    
    """Logout function"""
    def doLogout(self, request):
        s_logout(request)
        messages.success(request, "Logout successfully")
        return HttpResponseRedirect('/')
