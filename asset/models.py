from django.db import models

class AssetGroup(models.Model):
    technical_details = models.JSONField()

class Asset(models.Model):
    assetid = models.CharField(max_length=6, primary_key=True)
    asset_type = models.TextField()
    location = models.TextField()
    status = models.CharField(max_length=20)
    group = models.ForeignKey(AssetGroup, related_name="assets")
