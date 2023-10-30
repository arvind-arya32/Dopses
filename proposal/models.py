from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import datetime, date

# myapp/models.py
# from django.db import models

# class Publication(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=200)
#     year = models.IntegerField()
#     journal = models.CharField(max_length=200)
#     volume = models.CharField(max_length=20)
#     pages = models.CharField(max_length=50)

#     def __str__(self):
#         return self.title



    
# Extending User Model Using a One-To-One Link
class UserProposal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='userproposal')
    CHOICES = (
        ("ARIES (33%)",       "ARIES (33%)"),
        ("Indian Time (60%)", "Indian Time (60%)"),
        ("Belgian (7%)",      "Belgian (7%)"),
    )

    TYPE_CHOICES = (
        ("Long Term (New)",    "Long Term (New)"),
        ("Long Term (Ongoing)","Long Term (Ongoing)"),
        ("Short Term",         "Short Term"),
        ("Thesis Project",     "Thesis Project"),
    )

    TARGET_CHOICES = (
        ("YES", "YES"),
        ("NO", "NO"),
    )

    SCHEDULING_REQUEST = (
        ("Bright", "Bright"),
        ("Grey", "Grey"),
        ("Dark", "Dark"),
        ("Time Critical Observation", "Time Critical Observation"),
        ("Other", "Other")
    )

    OBSERVING_TIME = (
        ("Hours", "Hours"),
        ("Nights", "Nights"),
    )

    OBSERVATION_MODE = (
        ("Imaging",                  "Imaging"),
        ("Spectroscopy",             "Spectroscopy"),
        ("Imaging and Spectroscopy", "Imaging and Spectroscopy"),
    )
    SUCC = (
        ("YES", "YES"),
        ("NO", "NO"),
    )

    proposal_category = models.CharField(
        max_length=100,
        choices=CHOICES,
        verbose_name='Proposal Category', default='Unknown first_name',
    )

    proposal_title = models.CharField(
        max_length=100,
        verbose_name='Proposal Title',default='Unknown Proposal_title',
    )

    proposal_type = models.CharField(
        max_length=100,
        choices=TYPE_CHOICES,
        verbose_name='Proposal Type',default='Unknown first_name',
    )

    target_opportunity = models.CharField(
        max_length=100,
        choices=TARGET_CHOICES,
        verbose_name='Target Opportunity',default='Unknown first_name',
    )

    co_proposers = models.CharField(
        max_length=100,
        verbose_name='Co-Proposers',default='Unknown first_name',
    )

    co_pi = models.CharField(
        max_length=100,
        verbose_name='Co-PI Among Co-Proposers',default='Unknown first_name',
    )

    present_ob = models.CharField(
        max_length=100,
        verbose_name='Present OB',default='Unknown first_name',
    )

    #----------------COVER PAGE END HERE----------------------------------------------------#

    abstract = models.TextField(
        verbose_name='Abstract',default='Unknown first_name',
    )

    successful_proposals = models.CharField(
        max_length=100,
        choices=TARGET_CHOICES,
        verbose_name='Successful Proposals',default='Unknown first_name',
    )

    #----------------AbstractDetails PAGE END HERE----------------------------------------------------#



    scheduling_request = models.CharField(
        max_length=100,
        choices=SCHEDULING_REQUEST,
        verbose_name='Scheduling Request',default='Unknown Scheduling request',
    )

    observing_time = models.CharField(max_length=50,
        verbose_name='Observing Time', default='example-3nights',null=False,blank=True
    )

    preferred_date = models.DateField(
        verbose_name='Preferred Date',auto_now_add=False, auto_now=False,null=True,blank=True
    )

    impossible_date = models.DateField(
        verbose_name='Impossible Date',auto_now_add=False,auto_now=False,null=True,blank=True
    )

    justification = models.TextField(
        verbose_name='Justification',default='Unknown first_name',
    )


    #----------------ShedulingRequest PAGE END HERE----------------------------------------------------#


    observation_mode =models.CharField(
        max_length=100,
        choices=OBSERVATION_MODE,
        verbose_name='Observation Mode',default='Unknown Observation_Mode',
    )

    #----------------InstrumentsSetup PAGE END HERE----------------------------------------------------#



    list_of_objects = models.TextField(
        verbose_name='List of Objects',default='Unknown first_name',
    )



    #----------------ListOfObjects PAGE IS END HERE-------------------------------------------------#




    tech_justify = models.TextField(
        verbose_name='Technical Justification',default='Unknown first_name',
    )

    plans = models.TextField(
        verbose_name='Plans',default='Unknown first_name',
    )






    #----------------ObservationStrategy PAGE  IS END HERE------------------------------------------------#



    scientific_justify = models.FileField(upload_to='scientific_justifications/', default='default.jpg',)

    technical_justify = models.FileField(upload_to='technical_justifications/', default='default.jpg',)
    
    ongoing_proposal_status = models.FileField(upload_to='ongoing_proposal_status/', default='default.jpg',)


    #----------------AttachmentsDetails PAGE IS END HERE--------------------------------------------------#





    previous_obser = models.TextField(
        verbose_name='Previous Observation',default='Unknown first_name',
    )
    previous_obser = models.TextField(
        verbose_name='Previous Observation',default='Unknown first_name',
    )

    publication_relevant = models.CharField(
        max_length=100,
        verbose_name='Publication relevant',default='Unknown first_name',
    )

    publication_list = models.CharField(
        max_length=100,
        verbose_name='Publication list',default='Unknown first_name',
    )
    
    #----------------PublicationDetails PAGE IS END HERE--------------------------------------------------#
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, null=True, blank=True)
    
def __str__(self):
     return f"{self.user.username}'s"


    # resizing images
def save(self, *args, **kwargs):
    super().save()
    img = Image.open(self.scientific_justify.path)
    if img.height > 100 or img.width > 100:
        new_img = (100, 100)
        img.thumbnail(new_img)
        img.save(self.scientific_justify.path)
