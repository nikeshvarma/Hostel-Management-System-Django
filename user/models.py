from django.contrib.auth.models import User
from hostel.models import Room
from django.db import models


class Profile(models.Model):
    COURSES = [
        ('BE', 'BE'),
        ('B.Tech', 'B.Tech'),
        ('M.Tech', 'M.Tech'),
        ('B. Pharma', 'B. Pharma'),
        ('MBA', 'MBA'),
        ('CA', 'CA')
    ]

    DURATION = [
        ('3', 'Quarterly'),
        ('6', 'Half Yearly'),
        ('12', 'Yearly'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    roll_no = models.CharField(max_length=12, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    course = models.CharField(max_length=20, choices=COURSES, null=True)
    permanent_address = models.TextField(blank=True, null=True)
    temporary_address = models.TextField(blank=True)
    allotted = models.BooleanField(default=False)
    apply = models.BooleanField(default=False)
    room_allocation_date = models.DateField(null=True, blank=True)
    room_expiry_date = models.DateField(null=True)
    contact_no = models.CharField(blank=True, null=True, unique=True, max_length=13)
    parent_no = models.CharField(blank=True, null=True, unique=True, max_length=13)
    profile_pic = models.FileField(verbose_name='profile_pic', upload_to='profile_picture/', blank=True)
    duration = models.CharField(choices=DURATION, max_length=20, default=3)
    billing_amount = models.IntegerField(default=0)
    payment_request = models.BooleanField(default=False)
    payment_request_date = models.DateField(null=True)
    payment_status = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    class Meta:
        db_table = 'Student_Profile'
