MINS_BEFORE = 90

import gcsa
from gcsa.google_calendar import GoogleCalendar
from gcsa.event import Event

import datetime
from dateutil.relativedelta import relativedelta
import pytz
bgTime = pytz.timezone("Europe/Belgrade")

gc = GoogleCalendar()
now = bgTime.localize(datetime.datetime.now())
upcoming = list(gc.get_events(now - relativedelta(hour = MINS_BEFORE // 60, minute = MINS_BEFORE % 60), now + relativedelta(days=1), order_by="startTime", single_events=True))[0]

if (not upcoming):
    print()
    exit()

hour = 0
minute = 0
summary = upcoming.summary

if len(summary) > 25:
    summary = summary[:22] + "..."

try:
    hour = upcoming.start.hour
    minute = upcoming.start.minute
except:
    print(f' [00:00] {summary}')
    exit()

startDiff = (upcoming.start - now).total_seconds()    
if((startDiff <= MINS_BEFORE * 60) and now <= upcoming.end):
  print(f' [{hour:02d}:{minute:02d}] {summary}')  
  exit()

print()
