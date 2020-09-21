from django.urls import path

from .views import (CreateStatus,
                    StatusDetailView,
                    StatusListView,
                    CustomSerarch,
                    UpdateStatusView,
                    DeleteStatusView,
                    adminSearchTask,adminDetailTask,
                    emailTask)

app_name = 'status'

urlpatterns = [
    path('create/', CreateStatus.as_view(),name = 'create'),
    path('detail/<int:pk>', StatusDetailView.as_view(),name = 'detail'),
    path('list/', StatusListView.as_view(),name = 'list'),
    path('search/', CustomSerarch,name = 'search'),
    path('update/<int:pk>', UpdateStatusView.as_view(),name = 'update'),
    path('delete/<int:pk>', DeleteStatusView.as_view(), name = 'delete'),
    path('admin/search/', adminSearchTask.as_view(),name='admin_search'),
    path('admin/detail/<int:pk>',adminDetailTask,name ='admin_detail'),
    path('email/',emailTask,name ='email'),
]
