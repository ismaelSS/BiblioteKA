from rest_framework import serializers
from .models import Loan


class LoanSerializer(serializers.ModelSerializer):
    def update(self, instance: Loan, validated_data: dict) -> Loan:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model = Loan
        fields = [
            "id",
            "user_id",
            "copy_id",
            "allocated_at",
            "return_date",
            "returned_at",
        ]
        extra_kwargs = {
            "return_date": {"read_only": True},
        }
