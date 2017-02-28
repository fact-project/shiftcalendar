from .models import  Role, CalendarEntry, LegacyCalendarEntry, setup_databases
from .logbook_models import Users
from .database import connect_databases, sandbox
from . import roles
import datetime
from tqdm import tqdm

import ephem
import numpy as np

fact_site = ephem.Observer()
fact_site.lon = '-17:53:28.0'
fact_site.lat = '28:45:41.9'
fact_site.elevation = 2200
fact_site.horizon = np.deg2rad(0)


def start_of_shift(dt):
    """
    `dt` is a datetime.date which points to 00:00am of the day, where the shifts
    starts in the evening.
    So if we ask for the next sun_set all is fine, we get the evening of this day.
    """
    fact_site.date = dt
    return fact_site.next_setting(ephem.Sun()).datetime()

def end_of_shift(dt):
    """
    `dt` is a datetime.date which points to 00:00am of the day, where the shifts
    starts in the evening.
    So if we ask for the next sun_rise, we would get the morning before the shift even started.
    So we need to add one-day to get the right morning.
    """
    fact_site.date = dt + datetime.timedelta(days=1)
    return fact_site.next_rising(ephem.Sun()).datetime()


def fill_CalendarEntry_from_Legacy():

    old_entries = sorted(
        list(LegacyCalendarEntry.select()),
        key=lambda entry: entry.date
    )

    users = list(
        Users.select(Users.username, Users.uid)
        .dicts()
        .execute()
    )
    username2uid = {u['username']:u['uid'] for u in users}
    uid2username = {u['uid']:u['username'] for u in users}

    new_entries = []
    for e in old_entries:
        if not e.u in username2uid:
            continue

        shift_start = start_of_shift(e.date)
        shift_end = end_of_shift(e.date)

        if not e.x:
            role = roles.SHIFTER_AWAKE
        else:
            role = roles.DEBUG_SHIFT
            shift_end = shift_start + (shift_end - shift_start)/2.;

        new_entries.append(dict(
            user_id=username2uid[e.u],
            role=role,
            start=shift_start,
            end=shift_end,
        ))

    with sandbox.atomic():
        CalendarEntry.insert_many(new_entries).execute()

connect_databases()
setup_databases(drop=True)
fill_CalendarEntry_from_Legacy()