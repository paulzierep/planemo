"""Module describing the planemo ``list_alias`` command."""
import click
import json

from planemo.galaxy import profiles
from planemo import options
from planemo.cli import command_function
from planemo.config import planemo_option
from planemo.io import info

try:
    from tabulate import tabulate
except ImportError:
    tabulate = None

# try:
#     import namesgenerator
# except ImportError:
#     namesgenerator = None


@click.command('list_alias')
@options.profile_option(required=True)
@command_function
def cli(ctx, profile, **kwds):
    """
    List aliases for a path or a workflow or dataset ID. Aliases are associated with a particular planemo profile.
    """
    info("Looking for profiles...")    
    aliases = profiles.list_alias(ctx, profile)
    if tabulate:
        print(tabulate({"Alias": aliases.keys(), "Object": aliases.values()}, headers="keys"))
    else:
        print(json.dumps(aliases, indent=4, sort_keys=True))
    
    info("{} aliases were found for profile {}.".format(len(aliases), profile))

    ctx.exit(0)
    return