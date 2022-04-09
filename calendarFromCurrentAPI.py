#
from flask_restx import Namespace, Resource, reqparse, inputs
from pytz import timezone, common_timezones, country_timezones

#
from commonFunctions import *

CalendarNamespace = Namespace('calendar', description='Namespace to date and time in many calendars in the world (Gregorian, Julian, Chinese, Solar Hijri, Maya, Republican...)...')

#
@CalendarNamespace.route('/list')
class CalendarList(Resource):

    #
    def get(self):

        #
        return {"available_calendars": getAllCalendars()}, 200