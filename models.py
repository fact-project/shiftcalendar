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
    CompositeKey
)

from .database import sandbox, calendar
from .logbook_models import Users

class Role(Model):
    name = CharField()
    title = CharField()

    class Meta:
        database = sandbox


class CalendarEntry(Model):
    user = ForeignKeyField(Users)
    role = ForeignKeyField(Role)
    start = DateField()
    end = DateField()

    class Meta:
        database = sandbox

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


