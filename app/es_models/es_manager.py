from flask_script import Manager
from .dummy_test import DummyTest1, DummyTestManager

manager = Manager(usage="Perform es operation")


@manager.command
def create_indexes():
    DummyTest1.init()


@manager.command
def create_command():
    DummyTestManager.create('xyz')