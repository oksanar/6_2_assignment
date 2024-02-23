from typing import List, Tuple
from convertor import distance, temperature


METRIC_FORMAT='metric'
ENGLISH_FORMAT='en'
TEMPERATURE_KEY='temperature'
DISTANCE_KEY='distance'
CELSIUS_SUFFIX='°C'
FAHRENHEIT_SUFFIX='°F'
METERS_SUFFIX='m'
FOOT_SUFFIX='ft'

def convert_data(data: List[dict], format=METRIC_FORMAT):
     def get_temperature(s: str)-> Tuple[float, str]:
          if s.endswith(CELSIUS_SUFFIX):
               return (float(s[:-2]), METRIC_FORMAT)
          elif s.endswith(FAHRENHEIT_SUFFIX):
               return (float(s[:-2]), ENGLISH_FORMAT)
          else:
               raise ValueError('Invalid temperature format')
     
     def get_distance(s: str)-> Tuple[float, str]:
          if s.endswith(METERS_SUFFIX):
               return (float(s[:-1]), METRIC_FORMAT)
          elif s.endswith(FOOT_SUFFIX):
               return (float(s[:-2]), ENGLISH_FORMAT)
          else:
               raise ValueError('Invalid distance format')
     for i in range(len(data)):
          row = data[i]
          _temperature = get_temperature(row[TEMPERATURE_KEY])
          _distance = get_distance(row[DISTANCE_KEY])
          if _temperature[1] == ENGLISH_FORMAT and format == METRIC_FORMAT:
               data[i][TEMPERATURE_KEY] = f'{temperature.from_fahrenheit_to_celsius(_temperature[0])}{CELSIUS_SUFFIX}'
          elif _temperature[1] == METRIC_FORMAT and format == ENGLISH_FORMAT:
               data[i][TEMPERATURE_KEY] = f'{temperature.from_celsius_to_fahrenheit(_temperature[0])}{FAHRENHEIT_SUFFIX}'
          
          if _distance[1] == ENGLISH_FORMAT and format == METRIC_FORMAT:
               data[i][DISTANCE_KEY] = f'{distance.from_feets_to_meters(_distance[0])}{METERS_SUFFIX}'
          elif _distance[1] == METRIC_FORMAT and format == ENGLISH_FORMAT:
               data[i][DISTANCE_KEY] = f'{distance.from_meters_to_feets(_distance[0])}{FOOT_SUFFIX}'
     return data
