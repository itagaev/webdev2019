from rest_framework import serializers
from api.models import Competition,Members
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class CompetitionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    created_by = UserSerializer(read_only=True)
    city = serializers.CharField()
    due_on = serializers.DateTimeField()
    requirements = serializers.CharField()
    field = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        model = Competition
        fields = ('id', 'name', 'created_by','city','due_on','requirements','field','email')



class MemberSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    membername = serializers.CharField(required=True)
    memberlocation = serializers.CharField()
    memberemail = serializers.EmailField()
    comps = CompetitionSerializer()
    class Meta:
        model = Members
        fields = '__all__'