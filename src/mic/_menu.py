import click
from mic._utils import first_line_new
from mic._mappings import *
from tabulate import tabulate


def edit_menu(choice, request, resource_name, mapping):
    var_selected = list(request.keys())[choice-1]
    request[var_selected] = ask_value(var_selected, resource_name=resource_name, mapping=mapping)
    click.clear()

def default_menu(request, resource_name, mapping):
    """
    First menu: Selection the action
    """
    print_request(request, mapping)
    properties_choices = list(request.keys())
    actions_choices = ["save", "send", "exit"]
    choices = properties_choices + actions_choices
    print_choices(properties_choices)
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
    if action == "save":
        save_menu(request)
    elif action == "send":
        push_menu(request)
    return 0

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
    headers = ["Property", "Value", "Complex"]
    for key, value in request.items():
        table.append([key, value, mapping[key]["complex"]])
    print(tabulate(table, headers, tablefmt="grid"))


def print_choices(choices):
    for index, choice in enumerate(choices):
        click.echo("[{}] {}".format(index + 1, choice))



def remove_menu(request):
    pass


def save_menu(request):
    pass


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
        else:
            edit_menu(choice, request, resource_name, mapping)



    return [request]
