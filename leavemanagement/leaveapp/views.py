from django.shortcuts import render,redirect
from .models import student,Teacher,leaverequest
from .forms import StudentForm,LeaveForm,TeacherRegForm
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')

def studentlogin(request):
    form = StudentForm()
    return render(request,'studentlogin.html',{'form':form})

  

def studentlog(request):
    if request.method=='POST':
        name= request.POST.get('name')
        password= request.POST.get('password')
        cr= student.objects.filter(name=name,password=password)
        if cr:
            user_details=student.objects.get(name=name,password=password)
            id=user_details.id
            name=user_details.name
            age=user_details.age
            email=user_details.email
            department=user_details.department
            gender=user_details.gender



            request.session['id']=id
            request.session['name']=name
            request.session['age']=age
            request.session['email']=email
            request.session['department']=department
            request.session['gender']=gender

            return redirect('studentprofile')
        else:
            form = StudentForm()
            ce="Invalid Username or Password"
            return render(request,'studentlogin.html',{'ce':ce,'form':form})
    else:
        return render(request,'about.html')  
    

def studentprofile(request):
    name=request.session['name']
    cr=student.objects.get(name=name)
    return render(request,'studentprofile.html',{'cr':cr})

def studentupdate(request,name):
    cr = student.objects.get(name=name)
    form = StudentForm(instance= cr)
    if request.method=="POST":
        form = StudentForm(request.POST,instance=cr)
        if form.is_valid():
            form.save()
            return redirect('studentprofile')
    return render(request, "studentupdate.html",{'form':form})


def studentleaverequest(request):
    form=LeaveForm()
    if request.method=='POST':
        form=LeaveForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('studentprofile')
    return render(request,'leaverequest.html',{'form':form})    

def Teacherlogin(request):
    form = TeacherRegForm()
    return render(request,'teacherlogin.html',{'form':form})

def Teacherlog(request):
    if request.method=='POST':
        name= request.POST.get('name')
        password= request.POST.get('password')
        cr= Teacher.objects.filter(name=name,password=password,loginapproval=True)
        cm= Teacher.objects.filter(name=name,password=password,loginapproval=False)
        if cr:
            user_details=Teacher.objects.get(name=name,password=password)
            id=user_details.id
            name=user_details.name
            age=user_details.age
            email=user_details.email
            request.session['id']=id
            request.session['name']=name
            request.session['age']=age
            request.session['email']=email

            return redirect('Teacherprofile')
        elif cm:
            form = TeacherRegForm()
            ce="Wait for Admin Approval"
            return render(request,'teacherlogin.html',{'ce':ce,'form':form})
        else:
            form = TeacherRegForm()
            ce="Invalid Username or Password"
            return render(request,'teacherlogin.html',{'ce':ce,'form':form})
    else:
        return render(request,'login.html')  
    

def TeacherReg(request):
    form = TeacherRegForm()
    if request.method == "POST":
        form = TeacherRegForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Teacherlogin')
    return render(request,'TeacherReg.html',{'form':form})  

def Teacherprofile(request):
    name=request.session['name']
    cr=Teacher.objects.get(name=name)
    return render(request,'Teacherprofile.html',{'cr':cr})


def Teacherupdate(request,name):
    cr = Teacher.objects.get(name=name)
    form = TeacherRegForm(instance= cr)
    if request.method=="POST":
        form = TeacherRegForm(request.POST,instance=cr)
        if form.is_valid():
            form.save()
            return redirect('Teacherprofile')
    return render(request, "Teacherupdate.html",{'form':form})

def viewleaverequest(request):
    cr = leaverequest.objects.filter(leaveapprovalstatus=False)
    return render(request,"viewleaverequest.html",{'cr':cr})

def leaveapproval(request,pk):
    cr = leaverequest.objects.get(id=pk)
    form = LeaveForm(instance= cr)
    if request.method=="POST":
        form = LeaveForm(request.POST,instance=cr)
        if form.is_valid():
            form.save()
            return redirect('viewleaverequest')
    return render(request, "leaveapproval.html",{'form':form})
    
def viewleaverequest(request):
    cr = leaverequest.objects.filter(leaveapprovalstatus=False)
    return render(request,"viewleaverequest.html",{'cr':cr})    

def approvalstatus(request):
    cr=leaverequest.objects.filter(student=request.session['id'])
    return render(request,"approvalstatus.html",{'cm':cr})

def logoutuser(request):
    logout(request)
    return redirect("login") 