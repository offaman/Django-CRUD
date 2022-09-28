from rest_framework import serializers
from StudentApi.models import StudentInfo

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = ('StudentName','StudentRollNo', 'StudentBranch','StudentGPA','StudentSection')