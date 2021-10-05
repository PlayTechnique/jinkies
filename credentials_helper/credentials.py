#!/usr/bin/env python3

import copy
import os
from pathlib import Path
import re
import sys
from typing import List

from mako.lookup import TemplateLookup
from mako.template import Template

class CredentialArgNotSupplied(Exception):
    """Custom exception class for indicating that an internal method did not find an argument to the --credential
    flag """
    pass


class CredentialNameNotFound(Exception):
    """Custom exception class for making it clear that the arg to the --credential flag did not correspond to a credential
    type"""
    pass


def get_credential_template_path_from_argv(private_argv: list = None, arg_to_search_for: str = None,
                                           valid_values: List[str] = None) -> str:
    """

    Param: private_argv: a copy of argv that allows for modification.
    Param: arg_to_search_for: currently only "--credential" is actually supported here. This method contains a combination of
    both knowing how to parse argv for the argument to something and information about a 'credentials path' type that
    is only defined informally. Most of the parsing methods should be separable from the logic of this.

    Param: valid_values: Although the private_argv array is untyped, we do perform string checks against the argument to
    --credential to see that contents to see if they're valid. If your string is not matched within valid_values,
    a CredentialNameNotFound exception shall raise.

    This idea is pretty paranoid, but I'm testing a new idea out to see what it gives me.

    Return: In the case of success, a path that corresponds to a template file in the credentials_templates directory.

    The idea is that the --credential argument is given a portion of a template file name in the credential_templates
    directory, and then the file path corresponding to that file is returned as a string.

    >>> get_credential_template_path_from_argv(private_argv = ["--foo", "--credential", "roflcopter"], \
      arg_to_search_for = "--credential", valid_values=("roflcopter"))
    'credentials_templates/roflcopter.yml.mako'


    >>> get_credential_template_path_from_argv(private_argv = ["--foo", "--credential"], \
    arg_to_search_for="--credential", valid_values=("party_down",) )
    Traceback (most recent call last):
       ...
    credentials.CredentialNameNotFound: --credential specified, but no credential type given. Valid credentials are
    party_down you supplied <None>
    """
    credential_name = get_single_value_from_args(private_argv, arg_to_search_for)

    if not credential_name in valid_values:
        raise CredentialNameNotFound(f"""--credential specified, but no credential type given. Valid credentials are
{"".join(valid_values)} you supplied <{credential_name}>""")

    credential_path = f"credentials_templates/{credential_name}"
    return credential_path


def get_single_value_from_args(private_argv: list = None, arg_for_value: str = None):
    """
    :param private_argv:
    :param arg_for_value: we search the array for this value and then (a) remove it from the array, (b) return the entry
    afterwards, which we assume is the value intended to be indicated by the argument, and (c) also remove the value
    from the array.
    :return: The argument value that we wanted to retrieve from within the array.

    >>> get_single_value_from_args(["--foo", "--bar", "bam"], "--bar")
    'bam'

    >>> get_single_value_from_args(['./credentials.py', '--credential', 'plain-text.yml.mako'], "--bar")
    'bam'
    """
    for i, arg in enumerate(private_argv):

        if arg == arg_for_value:

            try:
                value = private_argv[i + 1]
            except IndexError:
                return None

            private_argv.pop(i + 1)
            private_argv.pop(i)

            return value

    return None

# Prospective method for parsing the
# --credentials-paper-whatever
# def get_values_from_args(arg_for_values):
#     for i, arg in enumerate(sys.argv):
#         if arg == arg_for_values:
#             value = sys.argv[i + 1]
#
#     yield value

# Prospective method for parsing the
# --credentials-var stuff on the cli
# def get_template_properties():
#     matcher = re.compile(r'--(.*)-var')
#
#     template_properties = get_values_from_args("--")
#     return None


def helpful_help(default_templates_dir, credential_arg, list_arg):
    this_script_name = sys.argv[0]
    return f"""{this_script_name} - generates a credentials file to standard out. Pop it where you need it \n
and then mount it in to your jinkies. 😎

This script both helps you understand a correctly formatted credentials file's format, and lets you enter text into 
template credential files to complete them with your own data.

Environment Variables

TEMPLATES_DIR="path/to/dir" (defaults to "{default_templates_dir}", the built in templates)

-h --help - display this help message
{list_arg}    - list all known credentials names
{credential_arg} <credential_name>   - output the template file format for the <name> credentials. If variables are provided, 
                                   interpolate those values.
--<credential_name>-<var_name> <value>  - set a variable to interpolate into the named template. Requires '--credential <name>' to
                                        be provided. 
"""


def main():
    default_templates_dir = "./credentials_templates"
    TEMPLATES_DIR = os.path.abspath(os.environ.get("TEMPLATES_DIR", default_templates_dir))

    # The two strings to accept on argv for arguments.
    # We expect to see the string "--credentials" in argv followed by an argument which corresponds to
    # everything in the name of a credentials_templates file up to the file extension.
    credentials_arg = "--credentials"
    # --list does not take an arg. It's a command, really.
    list_arg = "--list"

    # Make a private copy of argv so that I can make edits to the contents with careless frivolity.
    private_argv = copy.deepcopy(sys.argv)

    if len(private_argv) <= 1:
        print(helpful_help(default_templates_dir, credentials_arg, list_arg))
        sys.exit(1)

    if "-h" in private_argv or "--help" in private_argv:
        print(helpful_help(default_templates_dir))
        sys.exit(0)

    if not os.path.isdir(TEMPLATES_DIR):
        sys.stderr.write(f"TEMPLATES_DIR {TEMPLATES_DIR} must be provided.")
        sys.stderr.write(helpful_help(default_templates_dir))
        sys.exit(1)

    os.chdir = TEMPLATES_DIR
    known_template_names = [str(path.name) for path in Path(TEMPLATES_DIR).rglob(f'*')]

    if "--list" in private_argv:
        print(known_template_names)
        sys.exit(0)

    try:
        template_path = get_credential_template_path_from_argv(private_argv=private_argv,
                                                               arg_to_search_for=credentials_arg,
                                                               valid_values=known_template_names
                                                               )
    except CredentialNameNotFound as e:
        sys.stderr.write(f"Credential name not found. Did you forget your argument to {credentials_arg}?\n")
        sys.stderr.write("Stack trace to follow:\n\n")
        raise e
    except CredentialArgNotSupplied as e:
        sys.stderr.write(f"Credential arg is blank. {credentials_arg} takes a value. See help for more.\n")
        sys.stderr.write("Stack trace to follow:\n\n")
        raise e

    my_template = Template(filename=template_path)
    print(my_template.render())


if __name__ == "__main__":
    main()
