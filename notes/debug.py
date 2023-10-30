from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import UserProposal

class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    #added

    affiliation = forms.CharField(max_length=500,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    designation = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=1000,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    telephone_number = forms.IntegerField(
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    mobile_number = forms.IntegerField(
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['avatar','first_name','last_name','bio','affiliation', 'designation', 'address', 'telephone_number', 'mobile_number', 'country']



class UpdateProposalForm(forms.ModelForm):

    CHOICES =(
    ("1", "ARIES (33%)"),
    ("2", "Indian Time (60%)"),
    ("3", "Belgian (7%)"),
    
)

    proposal_category = forms.CharField(label='Proposal Category', widget=forms.RadioSelect(choices=CHOICES,))

    proposal_title = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    TYPE_CHOICES =(
    ("1", "Long Term (New)"),
    ("2", "Long Term (Ongoing)"),
    ("3", "Short Term"),
    ("4", "Thesis Project"),
    )

    TARGET_CHOICES = (
        ("1", "YES"),
        ("2", "NO"),
    )

    SCHEDULING_REQUEST = (
        ("1", "Bright"),
        ("2", "Grey"),
        ("3", "Dark"),
        ("4", "Time Critical Observation"),
        ("5", "Other")
    )

    OBSERVING_TIME = (
        ("1", "Hours"),
        ("2", "Nights"),
    )

    OBSERVATION_MODE= (
        ("1", "Imaging"),
        ("2", "Spectroscopy"),
        ("3", "Imaging and Spectroscopy"),
    )


    proposal_type = forms.CharField(label='Proposal Type', widget= forms.Select(choices=TYPE_CHOICES, attrs={'class': 'form-control'}))

    target_opportunity = forms.CharField(label='Proposal Type', widget= forms.Select(choices=TARGET_CHOICES, attrs={'class': 'form-control'}))

    co_proposers = forms.CharField(max_length=100,
                                required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    co_pi = forms.CharField(max_length=100,
                                required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    present_ob = forms.CharField(max_length=100,
                                required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    abstract = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    successful_proposals = forms.CharField(label='Proposal Category', widget=forms.RadioSelect(choices=TARGET_CHOICES,))

    scheduling_request = forms.CharField(label='Proposal Type', widget= forms.Select(choices=SCHEDULING_REQUEST, attrs={'class': 'form-control'}))

    observing_time = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    preferred_date = forms.DateField(required = False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    impossible_date = forms.DateField(required = False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    justification = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    obervation_mode = forms.CharField(label='Proposal Type', widget= forms.Select(choices=OBSERVATION_MODE, attrs={'class': 'form-control'}))

    tech_justify = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    plans = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    scientific_justify = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    technical_justify = forms.FileField(required = False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    ongoing_proposal_status = forms.FileField(required = False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    previous_obser = forms.CharField(required = False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    
    class Meta:
        model = UserProposal
        # fields = ['avatar', 'bio', 'affiliation', 'designation', 'address', 'telephone_number', 'mobile_number', 'country']
        fields = ['proposal_category','proposal_title','proposal_type','target_opportunity','co_proposers','co_pi','present_ob']



