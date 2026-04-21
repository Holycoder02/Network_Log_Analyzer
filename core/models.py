from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class LogFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='logs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

 # only to show each log's uploader and upload time in dashboard
    def __str__(self):
        return f"Log uploaded by {self.user.username} at {self.uploaded_at}"



    
