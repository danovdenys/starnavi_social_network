from rest_framework import serializers

from analytics.models import UserActivity


class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = '__all__'
        read_only_fields = ['user', 'activity', 'date']
        extra_kwargs = {
            'request_path': {'write_only': True}
        }
class LikeActivitySerializer(serializers.Serializer):
    date = serializers.DateField()
    count = serializers.IntegerField()

    class Meta:
        fields = '__all__'
    
    