from django.db import models

# Create your models here.

class uploadfile(models.model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    timestamp = models.CharField(max_length=100)
    uploadedfile = models.FileField(upload_to = "Uploaded_Files/")

    class Meta:
        managed = False
        db_table = 'upload'

class Noti(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    timestamp = models.CharField(max_length=100)
    message = models.TextField()
    img_name = models.TextField()
    file_dir = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'dashview_notify'

class DetectedItem(models.Model):
    HAZARDOUS_ITEM = [
        ('aerosol', 'aerosol'),
        ('alcohol', 'alcohol'),
        ('awl', 'awl'),
        ('axe', 'axe'),
        ('battery', 'battery'),
        ('bat', 'bat'),
        ('bullet', 'bullet'),
        ('chisel', 'chisel'),
        ('electronic cigarettes(liquid)', 'electronic cigarettes(liquid)'),
        ('electronic cigarettes', 'electronic cigarettes'),
        ('firecracker', 'firecracker'),
        ('gunparts', 'gunparts'),
        ('gun', 'gun'),
        ('hammer', 'hammer'),
        ('handcuffs', 'handcuffs'),
        ('hdd(external)', 'hdd(external)'),
        ('hdd', 'hdd'),
        ('knife', 'knife'),
        ('laptop', 'laptop'),
        ('lighter', 'lighter'),
        ('liquid', 'liquid'),
        ('match', 'match'),
        ('metalpipe', 'metalpipe'),
        ('nailclippers', 'nailclippers'),
        ('plier', 'plier'),
        ('prtablegas', 'prtablegas'),
        ('saw', 'saw'),
        ('scissors', 'scissors'),
        ('screwdriver', 'screwdriver'),
        ('smartphone', 'smartphone'),
        ('solidfuel', 'solidfuel'),
        ('spanner', 'spanner'),
        ('ssd', 'ssd'),
        ('supplymentarybattery', 'supplymentarybattery'),
        ('tabletpc', 'tabletpc'),
        ('thinner', 'thinner'),
        ('throwing knife', 'throwing knife'),
        ('usb', 'usb'),
        ('zippooilm', 'zippooil')
    ]
    id = models.IntegerField(auto_created=True, primary_key=True)
    timestamp = models.CharField(max_length=100)
    item = models.CharField(max_length=50, choices=HAZARDOUS_ITEM)
    # item = models.CharField(max_length=50)
    confidence = models.FloatField()
    filename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'report_data'

    def __str__(self):
        return '%s %s' % (self.item, self.timestamp)
