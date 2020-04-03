import click


def parse(value):
    return int(value)

def default_menu():
    click.echo("")
    click.echo("======== ACTIONS ======")
    click.echo("Available actions are:")
    choices = ["Edit", "Remove", "Save", "Send", "Exit"]
    print_choices(choices)
    action = click.prompt("Select the action",
                          default=1,
                          show_choices=False,
                          type=click.Choice(range(1, len(choices)+1)),
                          value_proc=parse
                          )
    return action

def select_resource(request, action):
    click.clear()
    print_request(request)
    choices = request.keys()
    print_choices(choices)
    action = click.prompt("Select the resource to {}".format(action),
                          default=1,
                          show_choices=False,
                          type=click.Choice(range(1, len(choices)+1)),
                          value_proc=parse
                          )
    print(action)
    return action

def create_request(keys):
    request = {}
    for key in keys:
        request[key] = None
    return request


def print_request(request):
    for key, value in request.items():
        click.echo("{}: {}".format(key, value))


def print_choices(choices):
    for index, choice in enumerate(choices):
        click.echo("[{}] {}".format(index+1, choice))


def edit_menu(request):
    select_resource(request, action="edit")
    #print_choices(request.keys())

def remove_menu(request):
    pass

def save_menu(request):
    pass

def push_menu(request):
    pass
