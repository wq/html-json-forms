# html-json-forms

An implementation of the [HTML JSON Form] specification for use with the [Django REST Framework].  Extracted from [wq.db] for general use.

HTML JSON Forms use an array-style naming convention that makes it possible to represent complex nested JSON objects with regular HTML fields.  The idea is that client applications (such as [wq.app]) and eventually browsers could parse these fields and submit structured JSON to the server.  For backwards compatibility with older clients, the spec recommends implementing a fallback parser on the server to ensure that older clients can submit forms using the traditional method.  This Python package is an implementation of that algorithm.

```html
<!-- Input -->
<form>
  <input name="items[0][name]" value="Example">
  <input name="items[0][count]" value="5">
</form>
```

```js
// Output
{
    "items": [
        {
            "name": "Example",
            "count": "5"
        }
    ]
}
```

Note that the HTML JSON Form spec was never finalized.  The implementation is still useful as a formal way of representing structured data via traditional HTML forms.

[![Latest PyPI Release](https://img.shields.io/pypi/v/html-json-forms.svg)](https://pypi.org/project/html-json-forms)
[![Release Notes](https://img.shields.io/github/release/wq/html-json-forms.svg)](https://github.com/wq/html-json-forms/releases)
[![License](https://img.shields.io/pypi/l/html-json-forms.svg)](https://github.com/wq/html-json-forms/blob/master/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/wq/html-json-forms.svg)](https://github.com/wq/html-json-forms/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/wq/html-json-forms.svg)](https://github.com/wq/html-json-forms/network)
[![GitHub Issues](https://img.shields.io/github/issues/wq/html-json-forms.svg)](https://github.com/wq/html-json-forms/issues)

[![Travis Build Status](https://img.shields.io/travis/wq/html-json-forms/master.svg)](https://travis-ci.org/wq/html-json-forms)
[![Python Support](https://img.shields.io/pypi/pyversions/html-json-forms.svg)](https://pypi.org/project/html-json-forms)
[![Django Support](https://img.shields.io/pypi/djversions/html-json-forms.svg)](https://pypi.org/project/html-json-forms)

## Usage

`html-json-forms` is available via PyPI:

```bash
pip3 install html-json-forms
```

### Functional

```python
from html_json_forms import parse_json_form

parse_json_form({
    'items[0][name]': "Example",
    'items[0][count]': "5",
})
```

### DRF Integration
To enable HTML JSON Form parsing in Django REST Framework, subclass `JSONFormSerializer`:

```python
from rest_framework import serializers
from html_json_forms.serializers import JSONFormSerializer
from .models import Parent, Child

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child

class ParentSerializer(JSONFormSerializer, serializers.ModelSerializer):
    children = ChildSerializer(many=True)
    class Meta:
        model = Parent

# Alternatively you can use the pre-mixed JSONFormModelSerializer:
# class ParentSerializer(JSONFormModelSerializer):
#    ...
```

Note that only the top-level serializer needs to have the `JSONFormSerializer` mixin; the nested serializers will "just work" as if the data had been submitted via JSON.  Note further that this module only handles processing nested form data; it is still up to you to figure out how to handle [writing nested models][nested] (unless you are using [wq.db]'s [patterns] module, which includes writable nested serializers by default).

[HTML JSON Form]: https://www.w3.org/TR/html-json-forms/
[Django REST Framework]: http://www.django-rest-framework.org/
[wq.db]: https://wq.io/wq.db
[wq.app]: https://wq.io/wq.app
[nested]: http://www.django-rest-framework.org/api-guide/serializers/#writable-nested-representations
[patterns]: https://wq.io/docs/about-patterns
