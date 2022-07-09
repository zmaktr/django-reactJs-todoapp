from dataclasses import fields
from rest_framework import serializers
from . models import React

class ReactSerilizers(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['name', 'detail']