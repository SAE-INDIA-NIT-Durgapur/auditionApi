from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile
from SaeAudition.models import Answer

class ProfileAllSerializer(serializers.ModelSerializer):
    #answer = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    answer = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='answer_text'
     )
    class Meta:
        model = Profile
        fields = ('pk','user','first_name','last_name','curr_round','current_status','created_at','member','completed','answer')

    # def get_answer_set(self, instance):
    #     songs = instance.answer_set.all().order_by('-question')
    #     return serializers(songs, many=True).data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name')


User._meta.get_field('email')._unique = True


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'profile')
        extra_kwargs = {
            'password': {'write_only': True},
            # 'id':{'write_only':True},
            # 'first_name': {'required': True},
            # 'last_name': {'required': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        # user=User.objects.create(
        # username=validated_data['username'],
        # email=validated_data['email'],
        # password=validated_data['password'],
        # )
        profile_data = validated_data.pop('profile')
        profile = Profile.objects.create(
            user=user,
            first_name=profile_data['first_name'],
            last_name=profile_data['last_name'],
        )

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
