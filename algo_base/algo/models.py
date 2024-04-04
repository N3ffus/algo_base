from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class AlgoTheme(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DataStructureTheme(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Algorithm(models.Model):
    name = models.CharField(max_length=255)
    theme = models.ForeignKey('AlgoTheme', on_delete=models.SET_NULL, null=True)
    url_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class DataStructure(models.Model):
    name = models.CharField(max_length=255)
    theme = models.ForeignKey('DataStructureTheme', on_delete=models.SET_NULL, null=True)
    url_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class ProblemSite(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name


class Problem(models.Model):
    name = models.CharField(max_length=255)
    difficulty = models.IntegerField()
    url = models.URLField()
    site = models.ForeignKey('ProblemSite', on_delete=models.CASCADE)
    tags_algo = models.ManyToManyField(Algorithm, blank=True) # список алгоритмов, к которым относится задача
    tags_ds = models.ManyToManyField(DataStructure, blank=True) # список структур данных, к которым относится задача

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['difficulty']


class Article(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    tag_algo = models.ForeignKey('Algorithm', on_delete=models.CASCADE, null=True, blank=True)
    tag_ds = models.ForeignKey('DataStructure', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    tag_algo = models.ForeignKey('Algorithm', on_delete=models.CASCADE, null=True, blank=True)
    tag_ds = models.ForeignKey('DataStructure', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    problems = models.ManyToManyField(Problem, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
