from app.models.event import *
import datetime

event1 = Event(datetime.date(2020, 12, 24), "Christmas Ball", 200, "Hilton", "The biggest event of the year!")
event2 = Event(datetime.date(2020, 12, 25), "Christmas Hangover Breakfast", 100, "Hilton", "The second biggest event of the year!")
events = [event1, event2]


def add_new_event(event):
    events.append(event)

# event1 = Event(datetime.date(2020, 5, 17), "Staff Meeting", 35,  True, 'EDI1', "All staff meeting")
# event2 = Event(datetime.date(2020, 6, 18), "1-1 review", 2,  False, 'GLA3', "1-1 Review for weekend Homework")
# event3 = Event(datetime.date(2020, 7, 19), "Quiz Night", 40,  False, 'Open Area', "Quiz night for all cohorts")
