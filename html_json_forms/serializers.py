from rest_framework import serializers
from rest_framework.utils import html
from .utils import parse_json_form


class JSONFormSerializer(serializers.Serializer):
    def to_internal_value(self, data):
        if html.is_html_input(data):
            data = parse_json_form(data)
        return super(JSONFormSerializer, self).to_internal_value(data)


class JSONFormModelSerializer(JSONFormSerializer, serializers.ModelSerializer):
    pass
