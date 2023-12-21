from core.abstract.serializers import AbstractSerializer
from core.insurance.models import Insurance


class InsuranceSerializer(AbstractSerializer):

    class Meta:
        model = Insurance
        fields = ['id', 'name', 'email', 'phone_number',
                  'address', 'comment']
