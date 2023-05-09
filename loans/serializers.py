from rest_framework import serializers
from .models import Loan
from users.serializers import UserSerializer
from copies.serializers import CopySerializer


class LoanSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    copy = CopySerializer(required=False)

    user_id = serializers.IntegerField(write_only=True)
    copy_id = serializers.IntegerField(write_only=True)

    def update(self, instance: Loan, validated_data: dict) -> Loan:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.copy.is_avaliable = True
        instance.save()

        return instance

    class Meta:
        model = Loan
        fields = [
            "id",
            "copy",
            "user",
            "user_id",
            "copy_id",
            "allocated_at",
            "return_date",
            "returned_at",
        ]
        extra_kwargs = {
            "return_date": {"read_only": True},
        }
