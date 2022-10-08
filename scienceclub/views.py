from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from .models import Student
# Create your views here.

def home(request):
  return render(request, 'index.html')

def register(request):

  if request.method == 'POST':
      fname = request.POST.get('fname')
      lname = request.POST.get('lname')
      mname = request.POST.get('mname')
      # age = request.POST.get('age')
      # gender = request.POST.get('gender')
      # grade = request.POST.get('grade')
      # department = request.POST.get('dept')
      # idea = request.POST.get('idea')
      if Student.objects.filter(fname=fname).exists() and Student.objects.filter(lname=lname).exists() :
        messages.warning(request, 'You have already registerd!')
        return redirect('register')
      else:
        student = Student.objects.create()    
        student.fname = request.POST.get('fname')
        student.lname = request.POST.get('lname')
        student.mname = request.POST.get('mname')
        student.age = request.POST.get('age')
        student.gender = request.POST.get('gender')
        student.grade = request.POST.get('grade')
        student.department = request.POST.get('dept')
        student.idea = request.POST.get('idea')
        student.save()      
        messages.success(request, 'Thank You, You have successfully registerd! we will inform you shortly if you are Accepted or Not')
        return redirect('register')     
  return render(request, 'register.html')


def sciclub(request):
  page = 'sci'
  sci = Student.objects.filter(department= 'Science and Technolgy')
  total = Student.objects.filter(department= 'Science and Technolgy').count()
  context = { 'sci':sci, 'total':total , 'page': page}
  return render(request, 'students.html',context)


def comclub(request):
  page = 'com'
  com = Student.objects.filter(department= 'Computer')
  total = Student.objects.filter(department= 'Computer').count()
  context = { 'com':com, 'total':total , 'page': page}
  return render(request, 'students.html',context)

def coordinator(request):
  sci = Student.objects.filter(department= 'Science and Technolgy').count()
  com = Student.objects.filter(department= 'Computer').count()
  both = Student.objects.filter(department= 'Both').count()
  total = Student.objects.all().count()
  context = {'sci':sci, 'com':com, 'total':total , 'both':both}
  return render(request, 'coordinator.html',context)

def accept (request,pk):
  stu= Student.objects.get(id=pk)
  stu.accepted = True
  stu.save()
  messages.success(request, 'Thank You, You have Accepted The Student To Become A Memmber')
  next = request.GET.get('next', '/')
  return redirect(next)

def asciclub(request):
  page = 'sci'
  sci = Student.objects.filter(department= 'Science and Technolgy', accepted=True)
  total = Student.objects.filter(department= 'Science and Technolgy', accepted=True).count()
  context = { 'sci':sci, 'total':total , 'page': page}
  return render(request, 'accepted.html',context)


def acomclub(request):
  page = 'com'
  com = Student.objects.filter(department= 'Computer', accepted=True)
  total = Student.objects.filter(department= 'Computer', accepted=True).count()
  context = { 'com':com, 'total':total , 'page': page}
  return render(request, 'accepted.html',context)