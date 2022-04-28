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


class DetectedItem(models.Model):
    # HAZARDOUS_ITEM = [
    #     ('GN', 'Gun'),
    #     ('KN', 'Knife'),
    #     ('BA', 'Battery'),
    #     ('HD', 'Harddisk')
    # ]
    id = models.IntegerField(auto_created=True, primary_key=True)
    timestamp = models.CharField(max_length=100)
    # item = models.CharField(max_length=50, choices=HAZARDOUS_ITEM)
    item = models.CharField(max_length=50)
    confidence = models.FloatField()
    filename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'report_data'

    def __str__(self):
        return '%s %s' % (self.item, self.timestamp)
