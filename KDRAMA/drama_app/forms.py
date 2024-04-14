from django import forms
from .models import Award, Character, Director, Drama, Actor



class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = '__all__'

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'

class DramaForm(forms.ModelForm):
    class Meta:
        model = Drama
        fields = '__all__'

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
