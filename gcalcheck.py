MINS_BEFORE = 90
WHOLE_DAY = True

from gcsa.google_calendar import GoogleCalendar

import datetime
from dateutil.relativedelta import relativedelta
import pytz
bgTime = pytz.timezone("Europe/Belgrade")

gc = GoogleCalendar()
now = bgTime.localize(datetime.datetime.now())
upcoming = None

for event in gc.get_events(now + relativedelta(hours = -12), now + relativedelta(days=1), order_by="startTime", single_events=True):
    try:
        event.start.hour
    except AttributeError:
        if (WHOLE_DAY):    
            upcoming = event
            break
        else:
            continue

    if (event.end > now):
        upcoming = event
        break
  
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
except AttributeError:
    print(f' [00:00] {summary}')
    exit()

startDiff = (upcoming.start - now).total_seconds()    
if((startDiff <= MINS_BEFORE * 60) and now <= upcoming.end):
    print(f' [{hour:02d}:{minute:02d}] {summary}') 
    exit()

print()    
      
