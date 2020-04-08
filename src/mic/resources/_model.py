import logging
import modelcatalog
from mic._utils import get_api
from mic._mappings import *
from modelcatalog import ApiException
import click

from mic._menu import call_menu_select_property

RESOURCE = "Model"


def create(request=None):
    click.clear()
    call_menu_select_property(mapping_model, RESOURCE, request)



def push(request):
    configuration, username = get_api()
    api_instance = modelcatalog.ModelApi(modelcatalog.ApiClient(configuration=configuration))
    try:
        api_response = api_instance.models_post(username, model=request)
    except ApiException as e:
        logging.error("Exception when calling ModelConfigurationSetupApi->modelconfigurationsetups_post: %s\n" % e)
        quit()
    print(api_response)

