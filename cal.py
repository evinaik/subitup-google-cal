import os, urllib2
from json import loads
from pytz import timezone
from icalendar import Calendar, Event
from datetime import date, datetime, tzinfo
from calendar import monthrange

url = 'https://account.subitup.com/API2/employee/schedule.asmx/getEmployeeSchedule?employeeKey='
key = 'c2rI87k9nmQ%3d'
d = date.today()
m = d.month
y = d.year
sDate =  str(m) + '-01-' + str(y)
eDate = str(m) + '-' + str(monthrange(y, m)[1]) + '-' + str(y)
token = 'QI619nKp8I3xwXYDndAyu%2fHOzsQ9OmI1ib7DclIirB%2bqnTgtB9f%2fpQ%3d%3d'

cal = Calendar()
cal.add('prodid', '-//Ekansh Vinaik//SubItUp//EN')
cal.add('version', '1.0')
cal.add('summary', 'SubItUp Shifts in ICS')

response = urllib2.urlopen(url + key + '&startdate=' + sDate + '&enddate=' + eDate + '&deptKey=0&token=' + token)
j = loads(response.read())

for i in xrange(0, len(j)):
	start = timezone('US/Eastern').localize(datetime.strptime(j[i]['start'], '%m/%d/%Y %I:%M:%S %p'))
	end = timezone('US/Eastern').localize(datetime.strptime(j[i]['end'], '%m/%d/%Y %I:%M:%S %p'))
	event = Event()
	event.add('dtstart', start)
	event.add('dtend', end)
	event.add('location', 'Stamp Student Union')
	cal.add_component(event)

directory = os.getcwd()
f = open(os.path.join(directory, 'stamp.ics'), 'wb')
f.write(cal.to_ical())
f.close()