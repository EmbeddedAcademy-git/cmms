from django.contrib import admin
from .models import AssetGroup, Asset, Task, CompletedTasks, WorkOrder, Image

admin.site.register(AssetGroup)
admin.site.register(Asset)
admin.site.register(Task)
admin.site.register(CompletedTasks)
admin.site.register(WorkOrder)
admin.site.register(Image)
