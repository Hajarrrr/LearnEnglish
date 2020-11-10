from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView
from .models import User
from django.contrib.auth import authenticate,login

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            #user.username = user.email

            messages.success(request, f'{username}, account created !')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('blog-home')
		else:
			messages.info(request, 'Email OR password is incorrect')

	context = {}
	return render(request, 'users/login.html', context)



#added soon
'''class UserCreateView(CreateView):
        
        model = User
        template_name =  'users/login.html'
        fields = ('name', 'email', 'password')
        def get_success_url(request):
            all_users = User.objects.all()
            return render(request,'blog/home.html',{'User': all_users})
            #return redirect('/')
        class Meta:
            all_users = User.objects.all()
def UserCreateView(request):
        
        model = User
        template_name =  'users/login.html'
        fields = ('name', 'email', 'password')
        #def get_success_url(request):
        all_users = User.objects.all()
        return render(request,'blog/home.html',{'User': all_users})
            #return redirect('/')   '''




@login_required
def profile(request):
    return render(request, 'users/profile.html')

