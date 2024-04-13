from django.utils.timezone import now

from rest_framework import serializers

from .models import Departman, Personal


class DepartmanSerializer(serializers.ModelSerializer):

    personal_count = serializers.SerializerMethodField()

    class Meta:
        model = Departman
        fields = "__all__"
        read_only_fields = ["id"]

    
    def get_personal_count(self, departman_object):
        return departman_object.personals.count()
    


class PersonalSerializer(serializers.ModelSerializer):

    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = Personal
        fields = "__all__"
        read_only_fields = ["id", "user"]

    
    def get_days_since_joined(self, personal_object):
        return (now() - personal_object.start_date).days


    def create(self, validated_data):
        validated_data["user"] = self.context['request'].user
        personal = Personal.objects.create(**validated_data)
        return personal