# html-json-forms

An implementation of the [HTML JSON Form] specification for use with the [Django REST Framework].  Extracted from [wq.db] for general use.

HTML JSON Forms use an array-style naming convention that makes it possible to represent complex nested JSON objects with regular HTML fields.  The idea is that client applications (such as [wq.app]) and eventually browsers could parse these fields and submit structured JSON to the server.  For backwards compatibility with older clients, the spec recommends implementing a fallback parser on the server to ensure that older clients can submit forms using the traditional method.  This Python package is an implementation of that algorithm.

```html
<!-- Input -->
<form>
  <input name="items[0][name]" value="Example">
  <input name="items[0][count]" value="5">
</form>

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

[HTML JSON Form]: https://www.w3.org/TR/html-json-forms/
[Django REST Framework]: http://www.django-rest-framework.org/
[wq.db]: https://wq.io/wq.db
[wq.app]: https://wq.io/wq.app
