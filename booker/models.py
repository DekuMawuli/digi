from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


class Branch(models.Model):
    name = models.CharField(max_length=200)
    is_open = models.BooleanField(default=True)
    call_number = models.CharField(max_length=25, default="")
    location = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Branches"


class Driver(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    license_code = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Bus(models.Model):
    STATUS = [
        (1, "On Road"),
        (2, "Available"),
        (3, "Faulty"),
    ]
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE)
    branch = models.ManyToManyField(Branch, through="BranchBuses")
    capacity = models.IntegerField(default=0)
    number_plate = models.CharField(max_length=10)
    status = models.PositiveSmallIntegerField(default=2, choices=STATUS)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Buses"

    def __str__(self):
        return self.number_plate


@receiver(signal=post_save, sender=Bus)
def bus_added(sender, created, instance, **kwargs):
    if created:
        seats = [BusSeat(bus=instance) for i in instance.capacity]
        BusSeat.objects.bulk_create(seats)
    else:
        seats = BusSeat.objects.filter(bus=instance)
        if len(seats) != instance.capacity:
            BusSeat.objects.filter(bus=instance).delete()
            seats = [BusSeat(bus=instance) for i in instance.capacity]
            BusSeat.objects.bulk_create(seats)


class BranchBuses(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    bus = models.ForeignKey(Bus, on_delete=models.DO_NOTHING)
    destination = models.CharField(max_length=100)
    departure_time = models.TimeField()
    is_full = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Branch Buses"

    def __str__(self):
        return f"Bus Number: {self.bus.number_plate} ;; From: {self.branch.location :::> To: {self.destination}}"


class BusSeat(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100, default="")
    passenger_phone = models.CharField(max_length=10, default="")
    is_booked = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Bus Seats"

    def __str__(self):
        return f"Seat No: {self.id} :::: Booked: {self.is_booked}"
