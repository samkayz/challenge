from django.shortcuts import render
from django.contrib import messages
from user.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import user_logged_in
from django.dispatch.dispatcher import receiver
from . funct import *
from django.http import HttpResponseRedirect, response
new_funct = Main()




@receiver(user_logged_in)
def remove_other_sessions(sender, user, request, **kwargs):
    # remove other sessions
    Session.objects.filter(usersession__user=user).delete()

    # save current session
    request.session.save()

    # create a link from the user to the current session (for later removal)
    UserSession.objects.get_or_create(
        user=user,
        session=Session.objects.get(pk=request.session.session_key)
    )
## Views that render the index page

def index(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        # call the login object/function from the general Class
        resp = new_funct.do_login(request, email, password)
        return resp
    else:
        return render(request, 'index.html')
    

"""View Function that handle the Home/dashboard"""
@login_required(login_url='/')
def home(request):
    """Get all the data from the database and pass it to the view"""
    show = UserManagement.objects.filter().order_by('-id')
    return render(request, 'home.html',{'show':show})


"""View Function the get data from the form and send it to the function the do the creation"""
@login_required(login_url='/')
def handle_form(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        gender = request.POST['gender']
        dob = request.POST['dob']
        mobile = request.POST['mobile']
        nationality = request.POST['nationality']
        
        """Call the create user object"""
        resp = new_funct.create_user(request, firstname, lastname, email, mobile, dob, gender, nationality)
        return resp
    else:
        messages.error(request, "Invalid Request")
        return HttpResponseRedirect('/home')
    
"""Delete user view function"""
@login_required(login_url='/')
def delete_user(request, id):
    """Call Delete Record function"""
    new_funct.deleteRecord(id)
    messages.success(request, "Record Deleted Successfully")
    return HttpResponseRedirect('/home')


"""Edit Record view function"""
@login_required(login_url='/')
def edit_user(request, id):
    """Get the record for edit"""
    rec = get_object_or_404(UserManagement, id=id)
    return render(request, 'edit.html', {'rec':rec})



"""View function that handle Update record"""
@login_required(login_url='/')
def update_record(request):
    if request.method == "POST":
        id = request.POST['id']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        gender = request.POST['gender']
        dob = request.POST['dob']
        nationality = request.POST['nationality']
        
        """Get the object that will do the update"""
        resp = new_funct.updateRecord(request, id, firstname, lastname, email, mobile, gender, dob, nationality)
        return resp
    else:
        messages.error(request, "Invalid Request")
        return HttpResponseRedirect('/home')
    


"""Logout View function"""
def logout(request):
    """call logout function"""
    resp = new_funct.doLogout(request)
    return resp


def deleteSelected(request, id=None):
    if request.method == "POST":
        """Get the list of id's in the table"""
        selected = request.POST.getlist('selected')
        """Loop Through the list of ID in the table"""
        for id in selected:
            """call the delete record function"""
            new_funct.deleteRecord(id)
        messages.success(request, "Record Deleted Successfully")
        return HttpResponseRedirect('/home')
    else:
        messages.error(request, "Invalid Request")
        return HttpResponseRedirect('/home')
        
        
        