import click
from mic._utils import ask_simple_value
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


def select_resource(request, action):
    """
    Second menu: Selecting the property
    """
    click.clear()
    print_request(request)
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


def print_request(request):
    table = []
    headers = ["Property", "Value"]
    for key, value in request.items():
        table.append([key, value])
    print(tabulate(table, headers, tablefmt="grid"))


def print_choices(choices):
    for index, choice in enumerate(choices):
        click.echo("[{}] {}".format(index + 1, choice))


def edit_menu(request, resource_name):
    click.clear()
    var_selected = select_resource(request, action="edit")
    request[var_selected] = ask_simple_value(var_selected, resource_name=resource_name)


def remove_menu(request):
    pass


def save_menu(request):
    pass


def push_menu(request):
    pass


def parse(value):
    return int(value)
