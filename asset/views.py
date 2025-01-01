from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import AssetGroup, Asset, Task, CompletedTasks, WorkOrder, Image

# AssetGroup Views
class AssetGroupListView(ListView):
    model = AssetGroup
    template_name = 'assetgroup_list.html'
    context_object_name = 'assetgroups'

class AssetGroupDetailView(DetailView):
    model = AssetGroup
    template_name = 'assetgroup_detail.html'
    context_object_name = 'assetgroup'

class AssetGroupCreateView(CreateView):
    model = AssetGroup
    template_name = 'assetgroup_form.html'
    fields = ['thumbnail', 'group_name']
    success_url = reverse_lazy('assetgroup_list')

class AssetGroupUpdateView(UpdateView):
    model = AssetGroup
    template_name = 'assetgroup_form.html'
    fields = ['thumbnail', 'group_name']
    success_url = reverse_lazy('assetgroup_list')

class AssetGroupDeleteView(DeleteView):
    model = AssetGroup
    template_name = 'assetgroup_confirm_delete.html'
    success_url = reverse_lazy('assetgroup_list')

# Asset Views
class AssetListView(ListView):
    model = Asset
    template_name = 'asset_list.html'
    context_object_name = 'assets'

class AssetDetailView(DetailView):
    model = Asset
    template_name = 'asset_detail.html'
    context_object_name = 'asset'

class AssetCreateView(CreateView):
    model = Asset
    template_name = 'asset_form.html'
    fields = ['thumbnail', 'assetid', 'asset_type', 'location', 'status', 'group', 'maintenance_schedule_days', 'technical_details']
    success_url = reverse_lazy('asset_list')

class AssetUpdateView(UpdateView):
    model = Asset
    template_name = 'asset_form.html'
    fields = ['thumbnail', 'assetid', 'asset_type', 'location', 'status', 'group', 'maintenance_schedule_days', 'technical_details']
    success_url = reverse_lazy('asset_list')

class AssetDeleteView(DeleteView):
    model = Asset
    template_name = 'asset_confirm_delete.html'
    success_url = reverse_lazy('asset_list')

# Task Views
class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['asset', 'task_name', 'task_description', 'status']
    success_url = reverse_lazy('task_list')

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['asset', 'task_name', 'task_description', 'status']
    success_url = reverse_lazy('task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

# CompletedTasks Views
class CompletedTasksListView(ListView):
    model = CompletedTasks
    template_name = 'completedtasks_list.html'
    context_object_name = 'completedtasks'

class CompletedTasksDetailView(DetailView):
    model = CompletedTasks
    template_name = 'completedtasks_detail.html'
    context_object_name = 'completedtask'

class CompletedTasksCreateView(CreateView):
    model = CompletedTasks
    template_name = 'completedtasks_form.html'
    fields = ['image_before', 'image_after', 'task', 'description_before', 'description_after', 'issues']
    success_url = reverse_lazy('completedtasks_list')

class CompletedTasksUpdateView(UpdateView):
    model = CompletedTasks
    template_name = 'completedtasks_form.html'
    fields = ['image_before', 'image_after', 'task', 'description_before', 'description_after', 'issues']
    success_url = reverse_lazy('completedtasks_list')

class CompletedTasksDeleteView(DeleteView):
    model = CompletedTasks
    template_name = 'completedtasks_confirm_delete.html'
    success_url = reverse_lazy('completedtasks_list')

# WorkOrder Views
class WorkOrderListView(ListView):
    model = WorkOrder
    template_name = 'workorder_list.html'
    context_object_name = 'workorders'

class WorkOrderDetailView(DetailView):
    model = WorkOrder
    template_name = 'workorder_detail.html'
    context_object_name = 'workorder'

class WorkOrderCreateView(CreateView):
    model = WorkOrder
    template_name = 'workorder_form.html'
    fields = ['work_description', 'tasks', 'assigned', 'scheduled']
    success_url = reverse_lazy('workorder_list')

class WorkOrderUpdateView(UpdateView):
    model = WorkOrder
    template_name = 'workorder_form.html'
    fields = ['work_description', 'tasks', 'assigned', 'scheduled']
    success_url = reverse_lazy('workorder_list')

class WorkOrderDeleteView(DeleteView):
    model = WorkOrder
    template_name = 'workorder_confirm_delete.html'
    success_url = reverse_lazy('workorder_list')
