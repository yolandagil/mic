import logging
import modelcatalog
from mic._utils import get_api_configuration, first_line_new, get_complex
from mic._person import add_person


from mic._model_version import create as create_model_version
from modelcatalog import ApiException, Model
import click

from mic._menu import default_menu, create_request, print_request, edit_menu, remove_menu, save_menu, push_menu

mapping_model = {
    'Name': {"id": 'label'},
    'Description':  {"id": 'description'},
    'keywords':  {"id": 'keywords'},
    'website':  {"id": 'website'},
    'documentation':  {"id": 'has_documentation'},
    'versions':  {"id": 'has_version'}
}
get_complex(mapping_model, Model)

RESOURCE = "Model"


def create():
    click.clear()
    request = create_request(mapping_model.keys())

    while True:
        click.clear()
        first_line_new(RESOURCE)
        print_request(request, mapping_model)
        action = default_menu()

        if action == 1:
            edit_menu(request, RESOURCE, mapping_model)
        elif action == 2:
            remove_menu()
        elif action == 3:
            save_menu()
        elif action == 4:
            push_menu()
        elif action == 5:
            break



def push(request):
    configuration, username = get_api_configuration()
    api_instance = modelcatalog.ModelApi(modelcatalog.ApiClient(configuration=configuration))
    try:
        api_response = api_instance.models_post(username, model=request)
    except ApiException as e:
        logging.error("Exception when calling ModelConfigurationSetupApi->modelconfigurationsetups_post: %s\n" % e)
        quit()
    print(api_response)


