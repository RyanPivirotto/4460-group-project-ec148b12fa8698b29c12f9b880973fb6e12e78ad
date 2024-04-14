from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Award, Director, Drama, Actor, User
from django.views import View
from .forms import DirectorForm, DramaForm, ActorForm, AwardForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .serializers import DramaSerializer 
from rest_framework import generics


# Create your views here.        
class DramaList(generics.ListCreateAPIView):
    serializer_class = DramaSerializer
    def get(self,request):
        dramas = Drama.objects.all()
        return render(request=request, template_name='drama_list.html',context={'dramas':dramas})
     
class DramaDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DramaSerializer
    def get(self,request,id):
        drama = Drama.objects.get(pk=id)
        return render(request=request, template_name='drama_details.html',context={'drama':drama})

class ActorList(View):
    def get(self,request):
        actors = Actor.objects.all()
        return render(request=request, template_name='actor_list.html',context={'actors':actors})

class DirectorList(View):
    def get(self,request):
        directors = Director.objects.all()
        return render(request=request, template_name='director_list.html',context={'directors':directors})

class HomepageView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'homepage.html', {'form':form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                return render(request, 'homepage.html', {'form': form, 'login_failed': True})
        else:
            return render(request, 'homepage.html', {'form': form})

##############################
# CRUD Operations for KDRAMA #
##############################
class DramaAdd(View):
    def get(self, request):
        form = DramaForm()
        return render(request=request, template_name='drama_add.html', context={'form': form})

    def post(self, request):
        form = DramaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage') 
        else:
            return render(request=request, template_name='drama_add.html', context={'form': form})
        
class DramaDelete(View):
    def get(self, request, id):
        drama = get_object_or_404(Drama, id=id)
        return render(request, 'drama_delete.html', {'drama': drama})
    
    def post(self, request, id):
        drama = get_object_or_404(Drama, id=id)
        drama.delete()
        return redirect('drama-list')   
    

class DramaEdit(View):
    def get(self, request, id):
        drama = get_object_or_404(Drama, id=id)
        form = DramaForm(instance=drama)
        return render(request, 'drama_edit.html', {'form': form, 'drama': drama})
    
    def post(self, request, id):
        drama = get_object_or_404(Drama, id=id)
        form = DramaForm(request.POST, instance=drama)
        if form.is_valid():
            form.save()
            return redirect('drama-list')
        return render(request, 'drama_edit.html', {'form': form, 'drama': drama})

#############################
# CRUD Operations for Actor #
#############################
class ActorAdd(View):
    def get(self, request):
        form = ActorForm()
        return render(request, 'actor_add.html', {'form': form})

    def post(self, request):
        form = ActorForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('actor-list')
        else:
            return render(request, 'actor_add.html', {'form': form})

class ActorUpdate(View):
    def get(self, request, id):
        actor = Actor.objects.get(id=id)
        form = ActorForm(instance=actor)
        return render(request, 'actor_update.html', {'form': form, 'actor': actor})

    def post(self, request, id):
        actor = Actor.objects.get(id=id)
        form = ActorForm(request.POST, instance=actor)
        if form.is_valid():
            form.save()
            return redirect('actor-list')
        return render(request, 'actor_update.html', {'form': form, 'actor': actor})
    
class ActorDelete(View):
    def get(self, request, id):
        actor = get_object_or_404(Actor, id=id)
        return render(request, 'actor_delete.html', {'actor': actor})

    def post(self, request, id):        
        actor = get_object_or_404(Actor, id=id)        
        actor.delete()        
        return redirect('actor-list')

############################
# CRUD Operations for User #
############################
class UserAdd(View):
    def get(self,request):

        user = User.objects.all()

        return redirect('login')

class UserUpdate(View):

    def get(self,request,user_id=None):
        if user_id:
            user = User.objects.get(pk=user_id)
        else:
            user = User()

        return render(request, 'homepage.html')
    
    def post(self,request,user_id=None):

        if user_id:
            user = User.objects.get(pk=user_id)
        else:
            user = User()
        
        return render(request, 'homepage.html')
    
class UserDelete(View):

    def get(self,request,user_id=None):

        if user_id:
            user = User.objects.get(pk=user_id)
        else:
            user = User()

        return render(request, 'homepage.html')
      
    
    def post(self,request,user_id=None):

        user = User.objects.get(pk=user_id)

        user.delete()

        return render(request, 'homepage.html')
    
##################
# LOGIN##
#################

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'homepage.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
        return render(request, 'homepage.html', {'form': form})
    
#########
# AWARD CRUDS#
########
class AwardList(View):
    def get(self, request):
        awards = Award.objects.all()
        return render(request, 'award_list.html', {'awards':awards})

class AwardAdd(View):
    def get(self, request):
        form = AwardForm()
        return render(request, 'award_add.html', {'form': form})

    def post(self, request):
        form = AwardForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('award-list')
        else:
            return render(request, 'award_add.html', {'form': form})

class AwardUpdate(View):
    def get(self, request, id):
        award = Award.objects.get(id=id)
        form = AwardForm(instance=award)
        return render(request, 'award_update.html', {'form': form, 'award': award})

    def post(self, request, id):
        award = Award.objects.get(id=id)
        form = AwardForm(request.POST, instance=award)
        if form.is_valid():
            form.save()
            return redirect('award-list')
        return render(request, 'award_update.html', {'form': form, 'award': award})
    
class AwardDelete(View):
    def get(self, request, id):
        award = get_object_or_404(award, id=id)
        return render(request, 'award_delete.html', {'award': award})

    def post(self, request, id):        
        award = get_object_or_404(award, id=id)        
        award.delete()        
        return redirect('award-list')
    
    #############################
# CRUD Operations for Director #
#############################
class DirectorAdd(View):
    def get(self, request):
        form = DirectorForm()
        return render(request, 'director_add.html', {'form': form})

    def post(self, request):
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('director-list')
        else:
            return render(request, 'director_add.html', {'form': form})

class DirectorUpdate(View):
    def get(self, request, id):
        director = Director.objects.get(id=id)
        form = DirectorForm(instance=director)
        return render(request, 'director_update.html', {'form': form, 'director': director})

    def post(self, request, id):
        director = Director.objects.get(id=id)
        form = DirectorForm(request.POST, instance=director)
        if form.is_valid():
            form.save()
            return redirect('director-list')
        return render(request, 'director_update.html', {'form': form, 'director': director})
    
class DirectorDelete(View):
    def get(self, request, id):
        director = get_object_or_404(Director, id=id)
        return render(request, 'director_delete.html', {'director': director})

    def post(self, request, id):        
        director = get_object_or_404(Director, id=id)        
        director.delete()        
        return redirect('director-list')
