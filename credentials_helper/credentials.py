#!/usr/bin/env python3

import argparse
import os
from pathlib import Path
import sys

from string import Template



class CredentialNameNotFound(Exception):
    """Custom exception class for making it clear that the arg to the --credential flag did not correspond to a credential
    type"""
    pass

def helpful_help() -> str:
    return """
Run with just a credentials-type 
This script outputs a credential as yaml to standard out, so you can mount it in to your jinkies. 😎

Running the script with just the credentials type argument will dump to stdout a file with variables that can be 
filled out. The --vars option offers a cli syntax that lets you enter text into the variables associated with a file 
type,  to complete them  with your own data.


Example:
For a credential type that looks like:

=============
---

- long_description: "$description"
- short_description: "$short_description"
=============

Complete the content with the var argument. Each invocation of --var accepts a key=value pair

--var 'description="this is the long description" --var short_description=shorty

The data structure is cast to a dictionary.
"""

def helpful_afterword() -> str:
    """
    Environment Variables:

TEMPLATES_DIR=/path/to/dir   defaults to a built in templates directory, but you can update this variable to point
the script at an arbitrary directory. Templates inside the directory python's built-in String Templates
    """


def main():
    DEFAULT_TEMPLATE_DIR = "./credentials_templates"
    TEMPLATES_DIR = os.path.abspath(os.environ.get("TEMPLATES_DIR", DEFAULT_TEMPLATE_DIR))

    parser = argparse.ArgumentParser(description=helpful_help(), epilog=helpful_afterword())
    parser.add_argument("credentials_type", help="a type of credential. ")
    parser.add_argument("-l", "--list", action="store_true", help="list all known credentials types")
    parser.add_argument("-v", "--var", metavar="var=value", action='append',
                        type=lambda kv: kv.split("="), help="Each invocation specifies a variable to map; into the "
                                                            "credentials file")

    if not os.path.isdir(TEMPLATES_DIR):
        sys.stderr.write(f"TEMPLATES_DIR {TEMPLATES_DIR} must exist.")
        sys.exit(1)

    os.chdir(TEMPLATES_DIR)

    known_template_names = [str(path.name) for path in Path(TEMPLATES_DIR).rglob(f'*')]

    # We handle -l and --list separately, so that a user can specify credentials.py -l to get info about the types
    # available
    if "-l" in sys.argv or "--list" in sys.argv :
        print(" ".join(known_template_names))
        sys.exit(0)

    args = parser.parse_args()

    credentials_type = args.credentials_type

    content = None

    with open(credentials_type) as file:
        content = file.read()

    if args.var:

        values = dict(args.var)
        content = Template(content)
        content = content.safe_substitute(values)

    print(content)


if __name__ == "__main__":
    main()
