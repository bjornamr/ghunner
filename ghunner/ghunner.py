import click

try:
    from auth import login
    from runner import runner_tools
except:
    from .auth import login
    from .runner import runner_tools


@click.group(name="ghunner")
def ghunner():
    pass


ghunner.add_command(login)
ghunner.add_command(runner_tools)
ghunner()
