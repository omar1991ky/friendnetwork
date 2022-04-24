from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView
from .models import *
from .Forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator

# Create your views here.

class Signup_view(CreateView):
    model=User
    form_class = SignupForm
    template_name = 'signup.html'



    def form_valid(self, form):
        user=form.save()
        login(self.request,user)
        return redirect('profile')
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('profile')
        return super(Signup_view,self).get(*args,**kwargs)


def Login (request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == "GET" :
           return render(request,'login.html')
        elif request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            User =authenticate(username=username,password=password)
            if User is not None :
                login(request,User)
                return redirect('home')
            else:
                print("wrong user name")
                return redirect('login')
def log_out(request):
    logout(request)
    return redirect('login')
@ method_decorator(login_required(login_url='login'),name='dispatch')
class profile (ListView):
    model = post
    template_name = 'profile.html'
    paginate_by = 5

    def get_queryset(self):
        return post.objects.filter(user=self.request.user).order_by('-date_created')





def welcom (request):
    return render(request, 'welcomepage.html')

@ method_decorator(login_required(login_url='login'),name='dispatch')
class profile_stteing(UpdateView):
    modle=User
    fields = ['first_name','last_name','profile_pic','bio']
    template_name = 'profilesetting.html'
    success_url = '/profile/'
    def get_object(self, queryset=None):
        return self.request.user

@method_decorator(login_required(login_url='login'), name='dispatch')
class great_post(CreateView):
    model = post
    fields = ['caption']
    template_name = 'posts.html'
    success_url = '/profile/'

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)
@ method_decorator(login_required(login_url='login'),name='dispatch')
class friend_profile (ListView):
    model = post
    template_name = 'friend-profile.html'
    paginate_by = 5
    def get(self,*args,**kwargs):
        friendusername = self.kwargs['username']
        usernamefriend = self.request.user.username
        if friendusername == usernamefriend:
            return redirect('profile')
        else :
            return super(friend_profile,self).get(*args,**kwargs)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        friendusername = self.kwargs['username']
        friend = User.objects.get(username=friendusername)
        context['friend'] = friend
        is_following= self.request.user.is_follwoing(friend)
        context['is_following']= is_following
        return context

    def get_queryset(self):
        friendusername= self.kwargs ['username']
        friend = User.objects.get(username=friendusername)
        return post.objects.filter(user=friend).order_by('-date_created')
@ method_decorator(login_required(login_url='login'),name='dispatch')
class searchview (ListView):
    model = User
    template_name = 'search-results.html'
    paginate_by = 5
    def get_queryset(self):
        search_term=self.request.GET ['search-term']
        x = User.objects.filter(username__contains=search_term)

        return x
@login_required(login_url='login')
def friend_follwo(request,id):
    user_A= request.user
    user_B = User.objects.get(id=id)
    friend_add = Freinds_con(user_A=user_A,user_B=user_B)
    friend_add.save()
    return redirect('/user/'+ user_B.username)

@login_required(login_url='login')
def friend_unfollwo(request,id):
    user_A= request.user
    user_B = User.objects.get(id=id)
    Freinds_con.objects.filter(user_A=user_A, user_B=user_B).delete()
    return redirect('/user/'+ user_B.username)
@ method_decorator(login_required(login_url='login'),name='dispatch')
class HomePage (ListView):
    model = User
    template_name = 'homepage.html'
    paginate_by = 5
    def get_queryset(self):
        x= self.request.user.get_following()
        return post.objects.filter(user__id__in=x).order_by('-date_created')







