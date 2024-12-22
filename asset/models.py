from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    file = models.ImageField(upload_to='/images')

class AssetGroup(models.Model):
    thumbnail = models.ForeignKey(Image, on_delete=models.CASCADE)
    group_name = models.TextField(unique=True)

class Asset(models.Model):
    thumbnail = models.ForeignKey(Image, on_delete=models.CASCADE)
    assetid = models.CharField(max_length=6, primary_key=True)
    asset_type = models.TextField()
    location = models.TextField()
    status = models.CharField(max_length=20)
    group = models.ForeignKey(AssetGroup, related_name="assets")
    maintenance_schedule_days = models.IntegerField(blank=True, null=True)
    technical_details = models.JSONField()

class Task(models.Model):
    asset = models.ForeignKey(Asset, related_name="tasks")
    task_id = models.IntegerField(primary_key=True)
    task_name = models.TextField()
    task_description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)

class CompletedTasks(models.model):
    image_before = models.ManyToManyField(Image, on_delete=models.CASCADE)
    image_after = models.ManyToManyField(Image, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, related_name="completed")
    description_before = models.TextField()
    description_after = models.TextField
    issues = models.TextField()
    completed_at = models.DateTimeField(auto_now_add=True)

class WorkOrder(models.Model):
    work_description = models.TextField()
    tasks = models.ManyToManyField(Task, related_name='work_order')
    assigned = models.ManyToManyField(User, related_name="work_order")
    scheduled = models.DateTimeField()
