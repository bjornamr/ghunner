import click

try:
    from api.get import getter
except:
    from .api.get import getter


@click.group(name="runner", invoke_without_command=False)
def runner_tools():
    """Tool related commands"""
    pass


runner_tools.add_command(getter)
