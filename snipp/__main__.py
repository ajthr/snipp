#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
:Author: Ajith
:Date: 11/10/2023
:Copyright: © 2023, Ajith
:License: MIT
"""

import click

from snipp import __version__
from snipp import db

@click.group()
@click.help_option()
@click.version_option(version=__version__)
def main():
    pass

@main.command(name="save", help="save a new snippet")
@click.option("-t", "--title", help="Title for the snippet", prompt=True, prompt_required=False)
@click.option("-c", "--content", help="Snippet Content", prompt=True, prompt_required=False)
def save(title, content):
    db_helper = db.DBConnection()
    if title is None:
        title = ""
    if content is None:
        MARKER = "# add contents here save and exit #"
        content = click.edit(MARKER)
        if content is not None:
            content = content.split(MARKER, 1)[1].strip()
    db_helper.add_snipp(title, content)

@main.command(name="views", help="view a single snippet")
@click.argument("id", nargs=1)
def view_single(id):
    db_helper = db.DBConnection()
    data = snipp[2]
    click.echo(data[:7] + (data[7:] and '...'))

@main.command(name="view", help="view all saved snippet")
def view():
    db_helper = db.DBConnection()
    for snipp in db_helper.get_all_snipp():
        data = snipp[2]
        click.echo(data[:7] + (data[7:] and '...'))

@main.command(name="delete", help="delete a snippet")
@click.argument("id", nargs=1)
def delete(id):
    db_helper = db.DBConnection()
    db_helper.delete_snipp(id)

if __name__ == '__main__':
    main()
