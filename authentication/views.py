from rest_framework_simplejwt.serializers import (TokenObtainPairSerializer)
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from . import serializers


class SignupViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    serializer_class = serializers.SignupSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # username_field= User.EMAIL_FIELD
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['username'] = self.user.username
        # data['groups'] = self.user.groups.values_list('name', flat=True)
        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Add custom claims
        token['username'] = user.username
        token['is_student'] = user.is_student

        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer