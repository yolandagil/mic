from mic._utils import first_line_new, ask_simple_value, ask_simple_value_definition

RESOURCE = "Parameter"

mapping_parameter = {
    'Name': {'_id': 'label', 'definition': 'Name of the parameter', 'required': True},
    'Data type': {'_id': 'hasDataType', 'definition': 'Tpe of the parameter. Accepted values are string, integer, '
                                                      'float or boolean', 'required': True},
    'Value': {'_id': 'hasFixedValue', 'definition': 'Value of this parameter in this setup. Setting up a value will '
                                                    'make the parameter non-editable on execution',
              'required': False},
    'Default Value': {'_id': 'hasDefaultValue', 'definition': 'Default value of the parameter', 'required': False},
    'Minimum accepted value': {'_id': 'hasMinimumAcceptedValue', 'definition': 'Minimum value the parameter can have',
                               'required': False},
    'Maximum accepted value': {'_id': 'hasMaximumAcceptedValue', 'definition': 'Maximum value the parameter can '
                                                                               'have [Optional]', 'required': False},
}


def add_parameter(i):
    first_line_new(RESOURCE, i+1)
    item = {"position": [i + 1]}
    for key in mapping_parameter:
        #value = ask_simple_value(key, RESOURCE)
        value = ask_simple_value_definition(key, RESOURCE, mapping_parameter[key])
        item[mapping_parameter[key]['_id']] = value
    return item
