#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
Script principal
"""

from __future__ import print_function
from flask_script import Manager
from flask_script import Server
from ueki import create_app
from ueki import create_db


SETTINGS = {
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'
}
app = create_app(SETTINGS)

manager = Manager(app)
manager.add_command('runserver', Server(host='0.0.0.0', port=5000))


@manager.command
def initdb():
    """Initialize the database."""
    create_db()
    print(u'Init the db')


if __name__ == "__main__":
    manager.run()
