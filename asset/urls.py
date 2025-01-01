from django.urls import path
from .views import (
    AssetGroupListView, AssetGroupDetailView, AssetGroupCreateView, AssetGroupUpdateView, AssetGroupDeleteView,
    AssetListView, AssetDetailView, AssetCreateView, AssetUpdateView, AssetDeleteView,
    TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView,
    CompletedTasksListView, CompletedTasksDetailView, CompletedTasksCreateView, CompletedTasksUpdateView, CompletedTasksDeleteView,
    WorkOrderListView, WorkOrderDetailView, WorkOrderCreateView, WorkOrderUpdateView, WorkOrderDeleteView,
)

urlpatterns = [
    # AssetGroup URLs
    path('assetgroups/', AssetGroupListView.as_view(), name='assetgroup_list'),
    path('assetgroups/<int:pk>/', AssetGroupDetailView.as_view(), name='assetgroup_detail'),
    path('assetgroups/create/', AssetGroupCreateView.as_view(), name='assetgroup_create'),
    path('assetgroups/<int:pk>/update/', AssetGroupUpdateView.as_view(), name='assetgroup_update'),
    path('assetgroups/<int:pk>/delete/', AssetGroupDeleteView.as_view(), name='assetgroup_delete'),

    # Asset URLs
    path('assets/', AssetListView.as_view(), name='asset_list'),
    path('assets/<int:pk>/', AssetDetailView.as_view(), name='asset_detail'),
    path('assets/create/', AssetCreateView.as_view(), name='asset_create'),
    path('assets/<int:pk>/update/', AssetUpdateView.as_view(), name='asset_update'),
    path('assets/<int:pk>/delete/', AssetDeleteView.as_view(), name='asset_delete'),

    # Task URLs
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),

    # CompletedTasks URLs
    path('completedtasks/', CompletedTasksListView.as_view(), name='completedtasks_list'),
    path('completedtasks/<int:pk>/', CompletedTasksDetailView.as_view(), name='completedtasks_detail'),
    path('completedtasks/create/', CompletedTasksCreateView.as_view(), name='completedtasks_create'),
    path('completedtasks/<int:pk>/update/', CompletedTasksUpdateView.as_view(), name='completedtasks_update'),
    path('completedtasks/<int:pk>/delete/', CompletedTasksDeleteView.as_view(), name='completedtasks_delete'),

    # WorkOrder URLs
    path('workorders/', WorkOrderListView.as_view(), name='workorder_list'),
    path('workorders/<int:pk>/', WorkOrderDetailView.as_view(), name='workorder_detail'),
    path('workorders/create/', WorkOrderCreateView.as_view(), name='workorder_create'),
    path('workorders/<int:pk>/update/', WorkOrderUpdateView.as_view(), name='workorder_update'),
    path('workorders/<int:pk>/delete/', WorkOrderDeleteView.as_view(), name='workorder_delete'),
]
