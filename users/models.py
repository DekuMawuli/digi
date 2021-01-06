from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.dispatch import receiver
from django.db.models.signals import post_save


class CustomUser(AbstractUser):
    ROLE = [
        (1, "Regular"),
        (2, "Admin"),
        (3, "Branch Admin"),
    ]
    role = models.PositiveSmallIntegerField(default=1, choices=ROLE)
    phone = models.CharField(max_length=10, default="")


@receiver(signal=post_save, sender=CustomUser)
def user_created(sender, instance, created, **kwargs):
    regular, ct = Group.objects.get_or_create(name="Regular")
    admin, ct = Group.objects.get_or_create(name="Admin")
    branch_admin, ct = Group.objects.get_or_create(name="Branch Admin")

    if created:
        if instance.role == 1:
            instance.groups.add(regular)
        elif instance.role == 2:
            instance.groups.add(admin)
        else:
            instance.groups.add(branch_admin)
    else:
        if instance.role == 1:
            instance.groups.clear()
            instance.groups.add(regular)
        elif instance.role == 2:
            instance.groups.clear()
            instance.groups.add(admin)
        else:
            instance.groups.clear()
            instance.groups.add(branch_admin)
