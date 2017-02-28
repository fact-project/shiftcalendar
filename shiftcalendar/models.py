import datetime
from peewee import (
    Model,
    CharField,
    IntegerField,
    BooleanField,
    ForeignKeyField,
    FixedCharField,
    TextField,
    MySQLDatabase,
    DateField,
    DateTimeField,
    CompositeKey
)

from .database import sandbox, calendar
from .logbook_models import Users

class Role(Model):
    name = CharField()
    title = CharField()
    color = CharField()
    active = BooleanField(help_text="true, if this Role can be chosen in the webinterface.")

    class Meta:
        database = sandbox

    def __repr__(self):
        return "{0}({1}, {2}, {3})".format(
            self.__class__.__name__,
            self.name,
            self.title,
            self.color)

class CalendarEntry(Model):
    user_id = IntegerField()
    role = ForeignKeyField(Role)
    start = DateTimeField()
    end = DateTimeField()

    class Meta:
        database = sandbox

def setup_databases(drop=False):
    '''
    Initiliaze all tables in the databse
    If drop is True, drop all tables before recreating them.
    '''
    tables = [Role, CalendarEntry]
    if drop is True:
        print('dropping existing tables')
        sandbox.drop_tables(tables, cascade=True, safe=True)

    sandbox.create_tables(tables, safe=True)

    from .roles import all_roles
    for r in all_roles:
        r.save()

class LegacyCalendarEntry(Model):

    y = IntegerField()
    m = IntegerField()
    d = IntegerField()
    u = CharField()
    x = IntegerField()

    class Meta:
        database = calendar
        db_table = 'Data'
        primary_key = CompositeKey('y', 'm', 'd')

    @property
    def date(self):
        return datetime.date(self.y, self.m+1, self.d)

    def __repr__(self):
        return "{0.date}: {0.u} {0.x}".format(self)


