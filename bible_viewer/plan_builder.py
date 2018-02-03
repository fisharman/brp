import os
from datetime import date, timedelta

from brp.settings import BASE_DIR


# read start date chapters in OSIS format
def _readfile():
    filename = 'bible_viewer/reading_plan.txt'
    activities = []


    try:
        file = open(os.path.join(BASE_DIR, filename))
        year, month, day = map(int, file.readline().split())
        for elements in file:
            activities.append(elements.strip())
        file.close()

        return year, month, day, activities
    except FileNotFoundError:
        # report file missing
        print("file not found")
        pass


def plan():
    plan_dict = {}
    year, month, day, activities = _readfile()

    if year and month and day and activities:
        plan_date = date(year, month, day)
        day_incr = timedelta(days=1)

        for elements in activities:
            plan_dict[plan_date] = elements
            plan_date += day_incr
    else:
        # list should not be empty
        pass

    return plan_dict
