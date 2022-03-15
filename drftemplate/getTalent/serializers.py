from rest_framework import serializers
from getTalent.models import User
from getTalent.forms import UserForm

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ValidEmailSerializer(FormSerializer):
    class Meta:
        form: UserForm
        fields = '__all__'