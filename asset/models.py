from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    def image_upload_to(instance, filename):
        return f'images/{filename}'

    file = models.ImageField(upload_to=image_upload_to)

    def __str__(self):
        return self.file.name

class AssetGroup(models.Model):
    thumbnail = models.ForeignKey(Image, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.group_name

class Asset(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('maintenance', 'Maintenance'),
        ('retired', 'Retired'),
    ]

    thumbnail = models.ForeignKey(Image, on_delete=models.CASCADE)
    assetid = models.CharField(max_length=6, primary_key=True)
    asset_type = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    group = models.ForeignKey(AssetGroup, related_name="assets", on_delete=models.CASCADE)
    maintenance_schedule_days = models.PositiveIntegerField(blank=True, null=True)
    technical_details = models.JSONField(default=dict)

    def __str__(self):
        return self.assetid

class Task(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('maintenance', 'Maintenance'),
        ('retired', 'Retired'),
    ]
    asset = models.ForeignKey(Asset, related_name="tasks", on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255)
    task_description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.task_name

class CompletedTasks(models.Model):
    image_before = models.ManyToManyField(Image, related_name='completed_before')
    image_after = models.ManyToManyField(Image, related_name='completed_after')
    task = models.ForeignKey(Task, related_name="completed", on_delete=models.CASCADE)
    description_before = models.TextField()
    description_after = models.TextField()
    issues = models.TextField()
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Completed Task: {self.task.task_name}"

class WorkOrder(models.Model):
    work_description = models.TextField()
    tasks = models.ManyToManyField(Task, related_name='work_order')
    assigned = models.ManyToManyField(User, related_name="work_order")
    scheduled = models.DateTimeField()

    def __str__(self):
        return f"Work Order: {self.scheduled}"