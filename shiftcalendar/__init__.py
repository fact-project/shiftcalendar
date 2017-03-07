from .models import  Role, CalendarEntry, LegacyCalendarEntry, MoonBreak
from .models import setup_databases
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

    users = list(
        Users.select(Users.username, Users.uid)
        .dicts()
        .execute()
    )
    username2uid = {u['username']:u['uid'] for u in users}
    uid2username = {u['uid']:u['username'] for u in users}


    old_entries = sorted(
        list(LegacyCalendarEntry.select()),
        key=lambda entry: entry.date
    )

    # get rid of non-personal entries like "ETHZ" and "TUDO"
    old_entries = [e for e in old_entries if e.u in username2uid]

    debug_shift_entries = [oe for oe in old_entries if oe.x]
    normal_shift_entries = [oe for oe in old_entries if not oe.x]

    normal_shift_entries_by_date = []
    last_date = None
    for e in normal_shift_entries:
        if e.date != last_date:
            last_date = e.date
            normal_shift_entries_by_date.append([])
        normal_shift_entries_by_date[-1].append(e)



    new_entries = []
    for e in debug_shift_entries:

        shift_start = start_of_shift(e.date)
        shift_end = end_of_shift(e.date)
        # debug shift is only half as long
        shift_end = shift_start + (shift_end - shift_start)/2.;

        new_entries.append(dict(
            user_id=username2uid[e.u],
            role=roles.DEBUG_SHIFT,
            start=shift_start,
            end=shift_end,
        ))

    for group in normal_shift_entries_by_date:
        shift_start = start_of_shift(group[0].date)
        shift_end = end_of_shift(group[0].date)
        shift_duration = shift_end - shift_start
        part_duration = shift_duration / len(group)

        for i, e in enumerate(group):
            part_start = shift_start + i * part_duration
            new_entries.append(dict(
                user_id=username2uid[e.u],
                role=roles.SHIFTER_AWAKE,
                start=part_start,
                end=part_start + part_duration,
            ))

    with sandbox.atomic():
        CalendarEntry.insert_many(new_entries).execute()


def fill_MoonBreak_from_Legacy():


    old_moon_breaks = sorted(
        list(
            LegacyCalendarEntry.select()
                .where(LegacyCalendarEntry.u == 'moon')
        ),
        key=lambda entry: entry.date
    )
    new_entries = [{'date':e.date} for e in old_moon_breaks]

    with sandbox.atomic():
        MoonBreak.insert_many(new_entries).execute()


def fill_legacy():
    connect_databases()
    setup_databases(drop=True)
    fill_CalendarEntry_from_Legacy()
    fill_MoonBreak_from_Legacy()