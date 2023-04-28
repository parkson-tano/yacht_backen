from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    path('portInformation/', PortInformation.as_view()),
    # path('employee/',EmployeeView.as_view()),
    path('image/', ImageView.as_view()),
    path('document/', DocumentAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),

    path('employee/personalinfo/', EmployeeView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('employee/personalinfo/<int:pk>', EmployeeView.as_view({
        'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'
    })),
    path('employee/port/', PortView.as_view({
        'get': 'list',
    })),
    path('employee/add/', EmployeeAPIView.as_view({
        'post': 'create'
    })),

    path('leave/add', LeaveAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('leave', LeaveDataAPIView.as_view({
        'get': 'list',
    })),
    path('leave/<int:pk>', LeaveAPIView.as_view(
        {'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'})),
    path('leave-policy/add', LeavePolicyAPIView.as_view({'get': 'list',
                                                         'post': 'create'})),
    path('leave-policy/<int:pk>', LeavePolicyAPIView.as_view({'get': 'retrieve',
                                                             'patch': 'partial_update',
                                                              'delete': 'destroy', 'put': 'update'})),
    path('special-leave/add',
         SpecialLeaveAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('special-leave/<int:pk>', SpecialLeaveAPIView.as_view(
        {'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'})),
        path('company-policy/add',
         CompanyLeavePolicyAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('company-policy/<int:pk>', CompanyLeavePolicyAPIView.as_view(
        {'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'})),

    path('company-manual/add', CompanyManualAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('company-manual/<int:pk>', CompanyManualAPIView.as_view({
        'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'
    })),
    path('company-policy-form/add', CompanyPolicyAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('company-policy-form/<int:pk>', CompanyPolicyAPIView.as_view({
        'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'
    })),
    path('company-procedure/add', CompanyProcedureAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('company-procedure/<int:pk>', CompanyProcedureAPIView.as_view({
        'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'
    })),
    path('ims-form/add', IMSFormAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('ims-form/<int:pk>', IMSFormAPIView.as_view({
        'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'
    })),
    path('departmental-procedure/add', DepartmentalProcedureAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('departmental-procedure/<int:pk>', DepartmentalProcedureAPIView.as_view({
        'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'
         })),
    path('manage-ims/add', CompanyIMSFormAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('manage-ims/<int:pk>', CompanyIMSFormAPIView.as_view({
        'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'
    })),
   path('departmental-procedure/list', DepartmentalProcedureListAPIView.as_view({
        'get': 'list',
    })),

    path('departmental-procedure/list/<int:pk>', DepartmentalProcedureListAPIView.as_view({

        'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'

         })),
]
