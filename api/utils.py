def convertData(data_input, format_type):
    if format_type == 'json':
        return data_input.to_json()
    elif format_type == 'csv':
        return data_input.to_csv()
    elif format_type == 'xml':
        return data_input.to_xml()
    else:
        return "Invalid format type"