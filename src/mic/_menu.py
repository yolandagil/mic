import click
from mic._mappings import *
from tabulate import tabulate


def default_menu():
    """
    First menu: Selection the action
    """
    click.echo("")
    click.echo("======== ACTIONS ======")
    click.echo("Available actions are:")
    choices = ["Edit", "Remove", "Save", "Send", "Exit"]
    print_choices(choices)
    action = click.prompt("Select the action",
                          default=1,
                          show_choices=False,
                          type=click.Choice(range(1, len(choices) + 1)),
                          value_proc=parse
                          )
    return action


def select_resource(request, action, mapping):
    """
    Second menu: Selecting the property
    """
    click.clear()
    print_request(request, mapping)
    choices = request.keys()
    print_choices(choices)
    action = click.prompt("Select the resource to {}".format(action),
                          default=1,
                          show_choices=False,
                          type=click.Choice(range(1, len(choices) + 1)),
                          value_proc=parse
                          )
    return list(choices)[action - 1]


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


def edit_menu(request, resource_name, mapping):
    click.clear()
    var_selected = select_resource(request, mapping=mapping, action="edit")
    request[var_selected] = ask_value(var_selected, resource_name=resource_name, mapping=mapping)


def remove_menu(request):
    pass


def save_menu(request):
    pass


def push_menu(request):
    pass


def parse(value):
    return int(value)


def ask_value(variable_name, resource_name, mapping, default_value=""):
    if mapping[variable_name]["complex"]:
        value = ask_complex_value(variable_name, mapping, resource_name=resource_name)
    else:
        value = ask_simple_value(variable_name, resource_name=resource_name)
    return value


def ask_complex_value(variable_name, resource_name, mapping, default_value=""):
    sub_resource = [{}]
    if mapping[variable_name] == "has_version":
        edit_menu(sub_resource, "Model Version", mapping_model_version)
    pass

def ask_simple_value(variable_name, resource_name, default_value=""):
    if variable_name.lower() == "name":
        default_value = None
    value = click.prompt('{} - {} '.format(resource_name, variable_name), default=default_value)
    if value:
        return [value]
    else:
        return []
