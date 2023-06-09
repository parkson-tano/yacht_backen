from rest_framework import serializers
from .models import *
from account.serializer import UserSerializer


class PortDataSerializer(serializers.ModelSerializer):
    class Meta():
        model = PortData
        fields = "__all__"

class EmployeeDataSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta():
        model = EmployeeData
        fields = "__all__"

class EmployeeDataRegisterSerializer(serializers.ModelSerializer):
    class Meta():
        model = EmployeeData
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    class Meta():
        model = Image
        fields = "__all__"
         
class DocumentSerializer(serializers.ModelSerializer):
    class Meta():
        model = Document
        fields = "__all__"

class PortDataV(serializers.ModelSerializer):
    
    class Meta:
        model = PortData
        fields = ['id', ]

class LeaveSerializer(serializers.ModelSerializer):
    class Meta():
        model = Leave
        fields = "__all__"

class LeaveDataSerializer(serializers.ModelSerializer):
    employee = UserSerializer(read_only=True)
    approved_by = UserSerializer(read_only=True)
    class Meta():
        model = Leave
        fields = "__all__"


class LeavePolicySerializer(serializers.ModelSerializer):
    class Meta():
        model = LeavePolicy
        fields = "__all__"

class SpecialLeaveSerializer(serializers.ModelSerializer):
    class Meta():
        model = SpecialLeave
        fields = "__all__"

class CompanyLeavePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyLeavePolicy
        fields = "__all__"

class CompanyManualSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyManual
        fields = "__all__"

class CompanyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyPolicy
        fields = "__all__"

class CompanyIMSFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyIMSForm
        fields = "__all__"

class IMSProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = IMSProcedure
        fields = "__all__"

class IMSFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = IMSForm
        fields = "__all__"

class DepartmentalProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentalProcedure
        fields = "__all__"

class DepartmentalFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentalForm
        fields = "__all__"

class IMSFormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = IMSFormData
        fields = "__all__"

class DepartmentalFormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentalFormData
        fields = "__all__"

class DepartmentalFormDataViewSerializer(serializers.ModelSerializer):
    employee = UserSerializer(read_only=True)
    class Meta:
        model = DepartmentalFormData
        fields = "__all__"

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

class ReportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportType
        fields = "__all__"

class SubmitToSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmitTo
        fields = "__all__"

class EventSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSummary
        fields = "__all__"