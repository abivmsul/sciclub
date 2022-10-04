from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
# Create your views here.

def home(request):
  return render(request, 'index.html')

def register(request):

  if request.method == 'POST':
      messages.success(request, 'You have successfully registerd!')
      return redirect('register')     
        # username = request.POST['username']
        # password = request.POST['password']

        # user = auth.authenticate(username=username, password=password)

        # if user is not None:
        #     auth.login(request, user)
        #     messages.success(request, 'You are now logged in')
        #     if request.user.groups.filter(name='Researcher').exists():
        #         return redirect('researcherhome')
        #     elif request.user.groups.filter(name='Custodian').exists():
        #         return redirect('custodianhome')
        #     elif request.user.groups.filter(name='Department').exists():
        #         return redirect('departmenthome')
        #     elif request.user.groups.filter(name='Director').exists():
        #         return redirect('directorhome')
        #     else:
        #         messages.warning(request, 'Invalid credentials')
        #         return redirect('login')
    


  return render(request, 'register.html')