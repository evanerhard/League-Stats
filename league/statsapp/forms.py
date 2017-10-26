from django import forms
from .models import *
from statsapp import models

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class registration_form(UserCreationForm):
    email = forms.EmailField(
        label = "Email",
        required = True,
    )
    first_name = forms.CharField(label="First Name", max_length=30)
    last_name = forms.CharField(label="Last Name", max_length=30)

    class Meta:
        model = User
        fields = ("username", "email","password1","password2")

    def save(self, commit=True):
        user=super(registration_form,self).save(commit=False)
        user.email=self.cleaned_data["email"]
        # user.first_name=self.first_name
        # user.last_name=self.last_name
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username=forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name':'username'
        })
    )
    password=forms.CharField(
        label="Password",
        max_length=32,
        widget=forms.PasswordInput()
    )

class SearchForm(forms.Form):
    POSITION_CHOICES = (
        ("None","Pick a Position."),
        ("QB","QuarterBack(QB)"),
        ("RB","RunningBack(RB)"),
        ("FB","FullBack(FB)"),
        ("LT","Left Tackle(LT)"),
        ("LG","Left Guard(LG)"),
        ("C","Center(C)"),
        ("RG","Right Guard(RG)"),
        ("RT","Right Tackle(RT)"),
        ("TE","Tight End(TE)"),
        ("WR","Wide Receiver(WR)"),
        ("DE","Defensive End(DE)"),
        ("DT","Defensive Tackle(DT)"),
        ("OLB","Outside LineBacker(OLB)"),
        ("ILB","Inside LineBacker(ILB)"),
        ("CB","CornerBack(CB)"),
        ("SS","Strong Safety(SS)"),
        ("FS","Free Safety(FS)"),
        ("K","Kicker(K)"),
        ("P","Punter(P)"),
        ("KR","Kick Returner(KR)"),
        ("PR","Punt Returner(PR)"),
    )
    TEAM_CHOICES = (
        ("None","Pick a Team."),
        ("ARI","Arizona Cardinals"),
        ("ATL","Atlanta Falcons"),
        ("BAl","Baltimore Ravens"),
        ("BUF","Buffalo Bills"),
        ("CAR","Carolina Panthers"),
        ("CHI","Chicago Bears"),
        ("CIN","Cincinnati Bengals"),
        ("CLE","Cleveland Browns"),
        ("DAL","Dallas Cowboys"),
        ("DEN","Denver Broncos"),
        ("DET","Detroit Lions"),
        ("GB","Green Bay Packers"),
        ("HOU","Houston Texans"),
        ("IND","Indianapolis Colts"),
        ("JAC","Jacksonville Jaguars"),
        ("KC","Kansas City Chiefs"),
        ("MIA","Miami Dolphins"),
        ("MIN","Minnesota Vikings"),
        ("NE","New England Patriots"),
        ("NO","New Orleans Saints"),
        ("OAK","Oakland Raiders"),
        ("PHI","Philadelphia Eagles"),
        ("PIT","Pittsburgh Steelers"),
        ("SD","San Diego Chargers"),
        ("SEA","Seattle Seahawks"),
        ("SF","San Francisco 49ers"),
        ("STL","St. Louis Rams"),
        ("TB","Tampa Bay Buccaneers"),
        ("TEN","Tennessee Titans"),
        ("WAS","Washington Redskins"),
        ("NYG","New York Giants"),
        ("NYJ","New York Jets"),
        ("LA","Los Angeles Rams"),
        ("JAX","Jacksonville Jaguars"),
        ("LAC","Los Angeles Chargers"),
    )
    position = forms.ChoiceField(choices = POSITION_CHOICES,
        label= "Position",
        required=False
        )
    full_name = forms.CharField(label = "Enter a name:",
        required=False,
        max_length=255,
        strip = True
        )
    team = forms.ChoiceField(choices=TEAM_CHOICES,
        label = "Team",
        required=False
    )
