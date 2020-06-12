from django.db import models
# slugify changes to url format
from django.utils.text import slugify

# link embedding
import misaka
# Create your models here.

from django.contrib.auth import get_user_model
# call off of current user session
User = get_user_model()
from django import template
# use custom template tag
register = template.Library()


class Group(models.Model):

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(blank=True, editable=False, default='')
    memebers = models.ManyToManyField(user, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        self.slug=slugify(self.name)
        self.description_html=misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url():
        return reverse('groups:single', kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']


class GroupMember(models.Model):

    group = models.ForeignKey(Group, related_name='memberships')
    user = models.ForeignKey(User, related_name='user_groups')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')