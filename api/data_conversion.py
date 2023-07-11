```python
def convert_data(data_input, format_type):
    converted_data = None

    if format_type == 'json':
        import json
        try:
            converted_data = json.loads(data_input)
        except json.JSONDecodeError:
            return None

    elif format_type == 'xml':
        import xml.etree.ElementTree as ET
        try:
            converted_data = ET.fromstring(data_input)
        except ET.ParseError:
            return None

    elif format_type == 'csv':
        import csv
        import io
        try:
            reader = csv.reader(io.StringIO(data_input))
            converted_data = list(reader)
        except csv.Error:
            return None

    return converted_data
```