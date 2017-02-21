from peewee import MySQLDatabase
from playhouse.shortcuts import RetryOperationalError
from fact.credentials import get_credentials

class RetryMySQLDatabase(RetryOperationalError, MySQLDatabase):
    ''' Automatically reconnect when connection went down'''
    pass

sandbox = RetryMySQLDatabase(None)
factdata = RetryMySQLDatabase(None)
calendar = RetryMySQLDatabase(None)
logbook_db = RetryMySQLDatabase(None)

def connect_databases():
    config = get_credentials()['database']

    config['database'] = 'factdata'
    factdata.init(**config)
    factdata.connect()

    config['database'] = 'calendar'
    calendar.init(**config)
    calendar.connect()

    config['database'] = 'logbook'
    logbook_db.init(**config)
    logbook_db.connect()

    config = get_credentials()['sandbox']
    sandbox.init(**config)
    sandbox.connect()

