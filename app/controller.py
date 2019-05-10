import requests, os
import re

DARK_SKY_API_KEY = os.environ['DARK_SKY_KEY']
option_list = "exclude=currently,minutely,hourly,alerts&units=si"

p = re.compile('\d+(\.\d+)?')

class Controller:
    
    def check_data(self, data):
        for key in data.keys():
            if len(data[key])==0 or p.match(data[key]) is None:
                return '{} is empty or is not number'.format(key)
                
        return None


    def get_decision(self, data):
        #date_from = data['date_from']
        #date_to = data['date_to']



        weather_reports = []


        return 'No'
