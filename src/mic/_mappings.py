from mic._utils import get_complex
from modelcatalog import Model, DatasetSpecification, SoftwareVersion, Parameter, Person, SampleResource

mapping_model = {
    'Name': {"id": 'label'},
    'Description': {"id": 'description'},
    'keywords': {"id": 'keywords'},
    'website': {"id": 'website'},
    'documentation': {"id": 'has_documentation'},
    'versions': {"id": 'has_version'}
}
mapping_model_version = {
    'Name': {"id": 'label'},
    'Description': {"id": 'description'},
    'Version': {"id": 'has_version_id'},
}
mapping_dataset_specification = {
    'Name': {"id": 'label'},
    'Format': {"id": 'has_format'},
}
mapping_parameter = {
    'Name': {"id": 'label'},
    'Value': {"id": 'has_fixed_value'},
}
mapping_model_configuration = {
    'Name': {"id": 'label'},
}
mapping_person = {
    'name': {"id": 'label'},
    'email': {"id": 'email'},
    'website': {"id": 'website'}
}
mapping_sample_resource = {
    'URL': {"id": 'value'}
}
get_complex(mapping_model, Model)
get_complex(mapping_model_version, SoftwareVersion)
get_complex(mapping_dataset_specification, DatasetSpecification)
get_complex(mapping_parameter, Parameter)
get_complex(mapping_person, Person)
get_complex(mapping_sample_resource, SampleResource)
