from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    TITLE = (
        ("1", "Prof."),
        ("2", "Dr."),
        ("3", "Mrs."),
        ("4", "Ms."),
        ("5", "Mr.")
    )

    DESIGNATION = (
        ("1", "Faculty/Academic."),
        ("2", "Postdoc."),
        ("3", "PhD student."),
        ("4", "Graduate student."),
    )

    REFEREE = (
        ("1", "Yes."),
        ("2", "No."),
    )

    AFFILIATION = (
        ("1", "test1"),
        ("2", "test2"),
        ("3", "test3"),
        ("4", "test4"),
    )

    INTERESTS = (
        ("1", "AGN & Quasars"),
        ("2", "Compact Object Binaries"),
        ("3", "Cosmology"),
        ("4", "Earth Atmosphere"),
        ("5", "Exo-solar Planets"),
        ("6", "Galaxies"),
        ("7", "Gamma Ray Bursts"),
        ("8", "Globular Cluster"),
        ("9", "High-redshift galaxies"),
        ("10", "Individual Star"),
        ("11", "Instrumentation"),
        ("12", "Intergalactic medium"),
        ("13", "Interstellar medium"),
        ("14", "Near Earth Objects"),
        ("15", "Open Cluster"),
        ("16", "Planetary Bodies"),
        ("17", "Solar System"),
        ("18", "Star and Planet Formation"),
        ("19", "Supernovae"),
        ("20", "Surveys"),
    )

    title = models.CharField(max_length=100, choices=TITLE, default="UnKnown Title")
    first_name = models.CharField(max_length=100, default='Unknown first_name')
    last_name = models.CharField(max_length=100, default='Unknown last_name')
    alternate_email_id = models.EmailField(max_length=100, default="user@gmail.com")
    affiliation = models.CharField(max_length=500, choices=AFFILIATION, default='Unknown affiliation')
    designation = models.CharField(max_length=100, choices=DESIGNATION, default='Unknown designation')
    affiliation_name = models.CharField(max_length=500, default='Unknown affiliation_name')
    research_interest = models.CharField(max_length=100, choices=INTERESTS)
    address = models.CharField(max_length=1000, default='Unknown address')
    telephone_number = models.CharField(max_length=15, default='000000000000000')
    mobile_number = models.CharField(max_length=16, default='0000000000000000')
    country = models.CharField(max_length=100, default='Unknown country')
    state = models.CharField(max_length=100, default='Unknown state')
    city = models.CharField(max_length=100, default='Unknown city')
    act_as_referee = models.CharField(max_length=10, choices=REFEREE, default='Unknown')
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images', null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s profile"

    # Resizing images
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)