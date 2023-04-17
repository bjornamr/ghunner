import click
import keyring
from keyring.errors import PasswordSetError


@click.command(no_args_is_help=True)
@click.option("--token", required=True, help="github token e.g. ghp token")
def login(token: str):
    """ability to save token using keyring
    :param token: github token
    :type token: str
    """
    try:
        keyring.set_password("gunner", "TOKEN", token)
    except PasswordSetError as e:
        click.echo("error setting token", err=True, color=True)
        raise
