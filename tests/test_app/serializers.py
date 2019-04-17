from rest_framework import serializers
from html_json_forms.serializers import JSONFormModelSerializer
from .models import Parent, Child


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        exclude = ('parent',)


class ParentSerializer(JSONFormModelSerializer):
    children = ChildSerializer(many=True)

    def create(self, validated_data):
        children = validated_data.pop('children')
        parent = super(ParentSerializer, self).create(validated_data)
        for child in children:
            parent.children.create(**child)
        return parent

    class Meta:
        model = Parent
        fields = '__all__'
