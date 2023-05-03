from rest_framework import serializers
from .models import Loan


class LoanSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    copy_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Loan.objects.create(**validated_data)

    class Meta:
        model = Loan
        fields = [
            "id",
            "user_id",
            "copy_id",
            "allocated_at",
            "return_date",
            "retuned_at"
        ]
