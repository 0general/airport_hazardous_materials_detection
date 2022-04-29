from django.db import models

# Create your models here.
class Noti(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    timestamp = models.CharField(max_length=100)
    message = models.TextField()
    img_name = models.TextField()
    class Meta:
        managed = False
        db_table = 'dashview_notify'
