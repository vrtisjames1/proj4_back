from django.db import models

# Create your models here.
class Connect4(models.Model):
    username1 = models.CharField(max_length=32)
    user1_choice = models.IntegerField(default=1)
    username2 = models.CharField(max_length=32)
    user2_choice = models.IntegerField(default=2)
    z1 = models.IntegerField(default=0)
    z2 = models.IntegerField(default=0)
    z3 = models.IntegerField(default=0)
    z4 = models.IntegerField(default=0)
    z5 = models.IntegerField(default=0)
    z6 = models.IntegerField(default=0)
    z7 = models.IntegerField(default=0)
    a1 = models.IntegerField(default=0)
    a2 = models.IntegerField(default=0)
    a3 = models.IntegerField(default=0)
    a4 = models.IntegerField(default=0)
    a5 = models.IntegerField(default=0)
    a6 = models.IntegerField(default=0)
    a7 = models.IntegerField(default=0)
    b1 = models.IntegerField(default=0)
    b2 = models.IntegerField(default=0)
    b3 = models.IntegerField(default=0)
    b4 = models.IntegerField(default=0)
    b5 = models.IntegerField(default=0)
    b6 = models.IntegerField(default=0)
    b7 = models.IntegerField(default=0)
    c1 = models.IntegerField(default=0)
    c2 = models.IntegerField(default=0)
    c3 = models.IntegerField(default=0)
    c4 = models.IntegerField(default=0)
    c5 = models.IntegerField(default=0)
    c6 = models.IntegerField(default=0)
    c7 = models.IntegerField(default=0)
    d1 = models.IntegerField(default=0)
    d2 = models.IntegerField(default=0)
    d3 = models.IntegerField(default=0)
    d4 = models.IntegerField(default=0)
    d5 = models.IntegerField(default=0)
    d6 = models.IntegerField(default=0)
    d7 = models.IntegerField(default=0)
    e1 = models.IntegerField(default=0)
    e2 = models.IntegerField(default=0)
    e3 = models.IntegerField(default=0)
    e4 = models.IntegerField(default=0)
    e5 = models.IntegerField(default=0)
    e6 = models.IntegerField(default=0)
    e7 = models.IntegerField(default=0)
    f1 = models.IntegerField(default=0)
    f2 = models.IntegerField(default=0)
    f3 = models.IntegerField(default=0)
    f4 = models.IntegerField(default=0)
    f5 = models.IntegerField(default=0)
    f6 = models.IntegerField(default=0)
    f7 = models.IntegerField(default=0)