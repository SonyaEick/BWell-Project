from rest_framework import serializers
from .models import Cause


class CauseSerializer(serializers.ModelSerializer):
    is_local = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cause
        fields = (
            'id',
            'created_at',
            'state_code',
            'state_name',
            'county_code',
            'county_name',
            'strata_id',
            'injury',     # B_Wh_Injury
            'cancer',     # B_Wh_Cancer
            'homicide',   # B_Wh_Homicide
            'suicide',    # C_Wh_Suicide
            'hiv',        # D_Wh_HIV
            'time_span',  # LCD_Time_Span (dates)

            # custom fields
            'is_local',
        )

    def get_is_local(self, obj):
        # check to see if city is within radius of user's city
        is_local = getattr(obj, 'is_local', False)
        return is_local