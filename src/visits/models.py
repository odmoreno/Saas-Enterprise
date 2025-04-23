from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL  # auth.User # Assuming you have a custom user model
# Create your models here.
class PageVisit(models.Model):
    # db -> table
    # id -> hidden -> primary key -> autofield -> 1, 2, 3, 4, 5
    path = models.TextField(blank=True, null=True)  # col
    timestamp = models.DateTimeField(auto_now_add=True)  # col
    subdomain = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
