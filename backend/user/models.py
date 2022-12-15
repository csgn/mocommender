# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib import admin
from django.db import models

from movie.models.mcmetadata.mcmetadata import McMetadata


class Mcuser(models.Model):
    username = models.CharField(max_length=32)
    is_active = models.BooleanField()

    movie = models.ManyToManyField(McMetadata, through='Mcusermovie')

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'mcuser'


class Mcusermovie(models.Model):
    user = models.ForeignKey('Mcuser', on_delete=models.CASCADE)
    movie = models.ForeignKey(McMetadata, on_delete=models.CASCADE)
    is_played = models.BooleanField()
    is_recommended = models.BooleanField()
    is_liked = models.BooleanField()
    is_saved = models.BooleanField()
    play_runtime = models.FloatField()
    play_date = models.DateField()


    class Meta:
        managed = False
        db_table = 'mcusermovie'
        unique_together = (('user', 'movie'),)



@admin.register(Mcuser)
class McuserAdmin(admin.ModelAdmin):
    pass