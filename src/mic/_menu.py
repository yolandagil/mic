import click
from mic._utils import first_line_new
from mic._mappings import *
from tabulate import tabulate
import json


def edit_menu(choice, request, resource_name, mapping):
    var_selected = list(request.keys())[choice - 1]
    print('Current value for '+var_selected+' is: ' + str(request[var_selected]))
    print('Insert new value (c to cancel)')
    response = ask_value(var_selected, resource_name=resource_name, mapping=mapping)
    if response != ["c"]:
        print(response)
        request[var_selected] = response
    #click.clear()


def default_menu(request, resource_name, mapping):
    """
    First menu: Selection the action
    """
    print_request(request, mapping)
    properties_choices = list(request.keys())
    actions_choices = ["save", "send", "load", "exit"]
    choices = properties_choices + actions_choices
    #print_choices(properties_choices)
    action = click.prompt("Select the property to edit",
                          default=1,
                          show_choices=True,
                          type=click.Choice(list(range(1, len(properties_choices) + 1)) + actions_choices),
                          value_proc=parse
                          )
    if type(action) == str:
        action = handle_actions(request, action)
    return action


def handle_actions(request, action):
    if action == "exit":
        return 0
    if action == "save":
        save_menu(request)
    elif action == "send":
        push_menu(request)
    elif action == "load":
        req_aux = load_menu(request)
        # copy dictionary values (cannot assign to request directly)
        for key in request:
            request[key] = None
            if key in req_aux:
                request[key] = req_aux[key]
    return -1


def create_request(keys):
    """
    Create a dictionary to send the model catalog
    @param keys: List with properties of the resource
    @return: dict
    """
    request = {}
    for key in keys:
        request[key] = None
    return request


def print_request(request, mapping):
    table = []
    headers = ["id", "Property", "Value", "Complex"]
    i = 1
    for key, value in request.items():
        table.append([i, key, value, mapping[key]["complex"]])
        i = i+1
    print(tabulate(table, headers, tablefmt="grid"))


def print_choices(choices):
    for index, choice in enumerate(choices):
        click.echo("[{}] {}".format(index + 1, choice))


def remove_menu(request):
    pass


def save_menu(request):
    """
    Function to save the current request as a JSON file
    :param request: JSON to save
    :return:
    """
    try:
        # print_request(request)
        file_name = click.prompt('Enter the file name to save: ')
        file_name += '.json'
        with open(file_name, 'w') as outfile:
            json.dump(request, outfile)
        print('File saved successfully')
        # this will show status if saved.
        # click.confirm('File saved successfully. Do you want to continue editing?', abort=True)
    except:
        print('An error occurred when saving the file')
    pass


def load_menu(request):
    """
    Method that loads a JSON file of a model
    TO DO: Does not distinguish type at the moment (assumes it's a model)
    :param request: Current JSON request (initialized)
    :return: the JSON with the loaded file in request
    """
    try:
        file = click.prompt("Please type the path if the file to load")
        with open(file) as json_file:
            loaded_file = json.load(json_file)
        print('File loaded successfully')
    except:
        print('Error when loading the file')
        # click.confirm('Error loading the file. Continue?', abort=True)
    # print_request(request)
    # click.prompt('Press enter to continue',default='a')
    return loaded_file


def push_menu(request):
    pass


def parse(value):
    try:
        return int(value)
    except:
        return value


def ask_value(variable_name, resource_name, mapping, default_value=""):
    if mapping[variable_name]["complex"]:
        value = ask_complex_value(variable_name, resource_name, mapping)
    else:
        value = ask_simple_value(variable_name, resource_name)
    return value


def ask_complex_value(variable_name, resource_name, mapping, default_value=""):
    sub_resource = create_request(mapping_model_version.keys())
    if mapping[variable_name]["id"] == "has_version":
        return top_resource(mapping_model_version, SoftwareVersion)
    pass


def ask_simple_value(variable_name, resource_name, default_value=""):
    if variable_name.lower() == "name":
        default_value = None
    value = click.prompt('{} - {} '.format(resource_name, variable_name), default=default_value)
    if value:
        return [value]
    else:
        return []


def top_resource(mapping, resource_name):
    request = create_request(mapping.keys())
    while True:
        click.clear()
        first_line_new(resource_name)
        choice = default_menu(request, resource_name, mapping)
        if choice == 0:
            break
        elif choice == -1:
            #click.confirm("Continue editing?", abort=True)
            continue
        else:
            edit_menu(choice, request, resource_name, mapping)
    return [request]
