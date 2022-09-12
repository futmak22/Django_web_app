from django.db import models

# Create your models here.
class Pacient(models.Model):
    name = models.CharField(max_length=100)
    age  = models.IntegerField()

    def __str__(self):
        return self.name

class Phase(models.Model):
    pacient = models.ForeignKey('Pacient', on_delete=models.CASCADE)
    name    = models.CharField(max_length=100)
    number  = models.IntegerField()

    def __str__(self):
        return str(self.number)

class Day(models.Model):
    phase  = models.ForeignKey('Phase', on_delete=models.CASCADE)
    number = models.IntegerField()
    date   = models.DateTimeField()

    def __str__(self):
        return str(self.number)

class Track(models.Model):
    day      = models.ForeignKey('Day', on_delete=models.CASCADE)
    number   = models.IntegerField()
    duration = models.TimeField(auto_now=False, auto_now_add=False, default=0)

    def __str__(self):
        return str(self.number)

class Note(models.Model):
    track = models.ForeignKey('Track', on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    note  = models.TextField()

    def __str__(self):
        return str(self.number)
