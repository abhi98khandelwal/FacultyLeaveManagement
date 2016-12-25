"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import Leave_Form
from django.contrib.auth.models import User
from app.models import Leave_Status

@login_required(login_url='/')
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def login_view(request):
    """ Log In View"""
    if request.user.is_authenticated():
        return HttpResponseRedirect("/index")
    else:
        status = "Please Login"
        username = ''
        password = ''
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                try:
                    if user.details:
                        pass
                except:
                    from app.models import User_Details
                    add_details = User_Details(user=user,department = "")
                    add_details.save()
                status = 'Loged In'
                return HttpResponseRedirect('/index')
            else:
                status = "Your credentials were incorrect.Please login again."
        return render(
            request,
            'app/login.html',
            {
                'title' : "Log In",
                'status' : status,
                'username' : username,
                'password' : password
                }
            )

def logout_view(request):
    """Log Out View"""
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/')
def applyleave(request):
    """Gets the Leave Data"""
    error_stat = ""
    if request.method == 'POST':
        leave_form = Leave_Form(request.POST)
        if leave_form.is_valid():
            new = leave_form.save(commit=False)
            cur_user = request.user
            new.user = str(cur_user.get_username())
            days_leave = int((new.end_date - new.start_date).days)
            if days_leave > 0:
                bridge = True
                if str(new.type) == 'medical':
                    cur_user.details.medical -= days_leave
                    if cur_user.details.medical < 0:
                        bridge = False
                elif str(new.type) == 'earned':
                    cur_user.details.earned -= days_leave
                    if cur_user.details.earned < 0:
                        bridge = False
                elif str(new.type) == 'casual':
                    cur_user.details.casual -= days_leave
                    if cur_user.details.casual< 0:
                        bridge = False
                elif str(new.type) == 'holiday':
                    cur_user.details.earned -= days_leave
                    if cur_user.details.earned < 0:
                        bridge = False
                elif str(new.type) == 'study':
                    cur_user.details.study -= days_leave
                    if cur_user.details.study < 0:
                        bridge = False
                if bridge:
                    cur_user.details.save()
                    new.save()
                    return HttpResponseRedirect('/index')
                else:
                    error_stat = "Leaves Not Available"
            else:
                error_stat = "Please Enter valid Dates"
        else:
            error_stat = "Please fill valid details in form"
    else:
        leave_form = Leave_Form(instance=request.user)

    return render(
        request,
        'app/applyleave.html',
        {'leave_form' : leave_form , 
        'error_stat' : error_stat}
        )

def layout(request):
    return render(request,'app/layout.html')

@login_required(login_url='/')
def previousleave(request):
    if request.method == 'GET':
        leaves = Leave_Status.objects.filter(user = request.user.get_username())
    return render(request,'app/previousleave.html',{'leaves' : leaves})

@login_required(login_url='/')
def pendingleave(request):
    if request.method == 'GET':
        pending = Leave_Status.objects.filter(user = request.user.get_username(),status = False)
    return render(
        request,
        'app/pendingleave.html',
        {'pending' : pending}        
        )

def approveleave(request):
    return render(
        request,
        'app/approve.html'
        )
