import logging
import modelcatalog
from mic._utils import ask_simple_value, get_api_configuration, first_line_new
from mic._person import add_person


from mic._model_version import create as create_model_version
from modelcatalog import ApiException
import click

from mic._menu import default_menu, create_request, print_request, edit_menu, remove_menu, save_menu, push_menu

mapping_parameter = {
    'Short Description': 'label',
    'Value': 'hasFixedValue',
}

mapping_model = {
    'Name': 'label',
    'Description': 'description',
    'keywords': 'keywords',
    'website': 'website',
    'documentation': 'documentation',
}


RESOURCE = "Model"
def create():
    click.clear()
    request = create_request(mapping_model.keys())

    while True:
        click.clear()
        first_line_new(RESOURCE)
        print_request(request)
        action = default_menu()

        if action == 1:
            edit_menu(request, RESOURCE)
        elif action == 2:
            remove_menu()
        elif action == 3:
            save_menu()
        elif action == 4:
            push_menu()
        elif action == 5:
            break



    model_versions = []
    request = {}
    for key in mapping_model:
        value = ask_simple_value(key, RESOURCE)
        request[mapping_model[key]] = value

    request["author"] = add_person("Author")
    request["contributor"] = add_person("contributors")

    first_line_new(RESOURCE)
    while click.confirm('Do you want create a new version for the model?'):
        model_versions.append(create_model_version())
        if not click.confirm('Do you want create another version for the model?'):
            break
    request["hasVersion"] = model_versions
    push(request)




def push(request):
    configuration, username = get_api_configuration()
    api_instance = modelcatalog.ModelApi(modelcatalog.ApiClient(configuration=configuration))
    try:
        api_response = api_instance.models_post(username, model=request)
    except ApiException as e:
        logging.error("Exception when calling ModelConfigurationSetupApi->modelconfigurationsetups_post: %s\n" % e)
        quit()
    print(api_response)


