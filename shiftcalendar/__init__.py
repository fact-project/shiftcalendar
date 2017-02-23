from .models import  Role, CalendarEntry, LegacyCalendarEntry, setup_databases
from .logbook_models import Users
from .database import connect_databases, sandbox
from . import roles
import datetime as dt
from tqdm import tqdm
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

        shift_start = dt.datetime.combine(e.date, dt.time()) + dt.timedelta(hours=20)
        shift_end = dt.datetime.combine(e.date, dt.time()) + dt.timedelta(hours=20+10 if not e.x else 20+5)

        new_entry = dict(
            user_id=username2uid[e.u],
            role=roles.LEGACY_SHIFTER if not e.x else roles.LEGACY_EXPERT,
            start=shift_start,
            end=shift_end,
        )
        new_entries.append(new_entry)

    with sandbox.atomic():
        CalendarEntry.insert_many(new_entries).execute()

connect_databases()
setup_databases(drop=True)
fill_CalendarEntry_from_Legacy()