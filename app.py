from .models import  Role, CalendarEntry, LegacyCalendarEntry

def setup_database(database, drop=False):
    '''
    Initiliaze all tables in the databse
    If drop is True, drop all tables before recreating them.
    '''
    tables = [CalendarEntry, Role]
    if drop is True:
        log.info('dropping tables')
        database.drop_tables(tables, safe=True, cascade=True)

    database.create_tables(tables, safe=True)

def fill_CalendarEntry_from_Legacy():

    for entry in LegacyCalendarEntry.select(LegacyCalendarEntry.x == False):
        shift_start = fact.get_sunset_after(entry.date)
        shift_end = fact.get_sunrise_after(shift_start)

        new_entry = CalendarEntry(
            title='',
            start=shift_start,
            end=shift_end,
            allDay=False,
            role='shifter'
        )


