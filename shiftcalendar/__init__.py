from .models import  Role, CalendarEntry, LegacyCalendarEntry, setup_databases
from .logbook_models import Users
from .database import connect_databases, sandbox
from . import roles
from datetime import timedelta
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

    with sandbox.atomic():
        for e in tqdm(old_entries):
            if not e.u in username2uid:
                print(e.u, 'not found ... skipping', e)
                continue

            shift_start = e.date + timedelta(hours=20)
            shift_end = e.date + timedelta(hours=30)

            new_entry = CalendarEntry.create(
                user_id=username2uid[e.u],
                role=roles.LEGACY_SHIFTER if not e.x else roles.LEGACY_EXPERT,
                start=shift_start,
                end=shift_end,
            )

connect_databases()
setup_databases(drop=True)
fill_CalendarEntry_from_Legacy()