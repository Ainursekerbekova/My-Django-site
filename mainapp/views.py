from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View
from .models import post
from .forms import UserForm


def index(request):
    users=User.objects.all()
    return render(request,"mainapp/main_page.html",{'users':users})


def profile(request,user_id):
    user=get_object_or_404(User,pk=user_id)
    his_posts = post.objects.filter(user=user)
    return render(request,"mainapp/profile.html",{'user':user,'object_list':his_posts})


class PostView(generic.ListView):
    template_name = "mainapp/posts.html"

    def get_queryset(self):
        return post.objects.all()

class DetailView(generic.DetailView):
    model = post
    template_name = "mainapp/post.html"

class PostCreate(CreateView):
    model = post
    fields = ['title','body','img']
    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(PostCreate, self).form_valid(form)


class PostUpdate(UpdateView):
    model = post
    fields = ['title','body','img']

class PostDelete(DeleteView):
    model = post
    success_url = reverse_lazy('posts')



def LikePost(request,post_id,after):
    Post = get_object_or_404(post,pk=post_id)
    Post.likes = Post.likes+1
    Post.save()
    if(after=="all"):
        posts=post.objects.all()
        return render(request,"mainapp/posts.html",{'object_list':posts})
    else:
        Post = get_object_or_404(post,pk=post_id)
        return render(request,"mainapp/post.html",{'post':Post})

def SavePost(request,post_id,after):
    Post = get_object_or_404(post,pk=post_id)
    Post.is_saved = True
    Post.save()
    if(after=="all"):
        posts=post.objects.all()
        return render(request,"mainapp/posts.html",{'object_list':posts})
    else:
        Post = get_object_or_404(post,pk=post_id)
        return render(request,"mainapp/post.html",{'post':Post})




class UserFormView(View):
    form_class=UserForm
    template_name = "mainapp/registration_form.html"

    #display blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})


    #process form data
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            #dont save
            user=form.save(commit=False)

            #cleaned(normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()#save

            #Returns user object if all ok
            user=authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("index")
        return render(request,self.template_name,{'form':form})
