#now join models with view
from django.db.models import fields
from django.http.response import Http404
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse,Http404, request
from django.urls.base import reverse_lazy
from .forms import Register,logform
from .models import album,song,profile
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,View,CreateView,UpdateView,DeleteView
# Create your views here.
#def home(request):
    #return HttpResponse('<h1>site under construction</h1>')

# def home(request):
#     return  render (request,'music/home.html')
"""def home(request):
    a=album.objects.all()
    str=''
    for i in a:
        str=str+"<h1>"+i.title+"</h1>"
    print(str)
    return HttpResponse(str)    

def home(request):
    a=album.objects.all()
    return render(request,"music\home.html",{'data':a})"""

class Home(ListView):
    #kis html par bhejna ha 
    template_name="music\home.html"
    #kis nam se bhjna ha
    context_object_name='data'
    #kya bhjna ha 
    def get_queryset(self):
        return {'car':enumerate(album.objects.all()),'dt':album.objects.all()}

# def dts(request,val):
#     # try:
#     #     a=album.objects.get(id=val)
#     # except:
#     #     raise Http404("matching querry does not exist")
#     a=get_object_or_404(album,id=val)
#     if a.song_set.all():
#         st=''
#         for i in a.song_set.all():
#             st+="<h1>"+i.title+"</h1>"
#         return HttpResponse(st) 
#     else:
#         return HttpResponse("<h1>no song to display</h1>")
#  # print(data,p)      
    
class Dts(DetailView):
    model=album
    template_name="music/song.html"
    context_object_name="data"



# def signup(request):
#     f=Register(request.POST or None)
#     if f.is_valid(): #ISVALID HERE THE CALLING OF CLEAN
    #     data=f.save(commit=False)
    #     p=f.cleaned_data.get('password')
    #     data.set_password(p)
    #     data.save()
    #     return HttpResponse("user added")
    # return render(request,'music/signup.html',{"data":f})
class signup(View):
    def get(self,request):
        f=Register(None)
        return render(request,'music/signup.html',{"data":f})
    def post(self,request):
        f=Register(request.POST)
        if f.is_valid():
            data=f.save(commit=False)
            p=f.cleaned_data.get('password')
            data.set_password(p)
            data.save()
            return redirect('music:home')
        return render(request,'music/signup.html',{"data":f})
            


'''def signin(request):
    f=logform(request.POST or None)
    if f.is_valid():
        u=f.cleaned_data.get('username')
        return HttpResponse(f"user:{u} logged in successfully")
    return render(request,"music/login.html",{'data':f})'''

class signin(View):
    def get(self,request):
        f=logform(None)
        return render(request,"music/login.html",{'data':f})
    def post(self,request):
        f=logform(request.POST)
        if f.is_valid():
             u=f.cleaned_data.get('username')
             p=f.cleaned_data.get('password')
             ur=authenticate(username=u,password=p)
             nxt=request.GET.get('next')
             if ur:
                 login(request,ur)
                 if nxt:
                     return redirect(nxt)
             return redirect('music:home') #home ka url load krwane ke liye return mein
        return render(request,"music/login.html",{'data':f})
   

def signout(request):
    logout(request)
    return redirect('music:home')
    
class AddAlbum(LoginRequiredMixin,CreateView):
    login_url='music:login'
    model=album
    fields=['title','artist','genre','release','image']
    template_name='music/addalbum.html'
                           

class upalbum(LoginRequiredMixin,UpdateView):
    login_url='music:login'
    model=album
    fields=['title','artist','genre','release','image']
    template_name='music/upalbum.html'

class Delalbum(LoginRequiredMixin,DeleteView):
    login_url='music:login'
    model=album
    success_url=reverse_lazy('music:home')
    template_name='music/delalbum.html'
    context_object_name='data'    


class Addsong(LoginRequiredMixin,CreateView):
    login_url='music:login'
    model=song
    fields=['title','artist','genre','lyricist','file']
    template_name='music/addalbum.html'

    def form_valid(self, form):
        p=self.kwargs.get('pk')
        a=album.objects.get(id=p)
        form.instance.al_id=a
        return super().form_valid(form)



class upsong(UpdateView):
    model=song
    fields=['title','artist','genre','lyricist','file']
    template_name='music/addalbum.html'            

class delsong(DeleteView):
    model=song
    success_url=reverse_lazy('music:home')
    template_name='music/delalbum.html'
    context_object_name='data'  


class AddProfile(LoginRequiredMixin,CreateView):
    login_url='music:login'
    model=profile
    fields=['image','address','intrest','dob']
    template_name='music/addalbum.html'

    def form_valid(self, form):
        p=self.request.user.id
        a=User.objects.get(pk=p)
        form.instance.u_id=a
        return super().form_valid(form)    

def show_profile(request):
    return render(request,'music/profile_page.html')