from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProposal



@receiver(post_save, sender = User)
def create_user_proposal(sender,instance, created, **kwargs):
    if created:
        UserProposal.objects.get_or_create(user=instance)


@receiver(post_save,sender=User)
def save_user_proposal(sender,instance,**kwargs):
    instance.profile.save()

    