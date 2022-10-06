import pyowm
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config


config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('82547a1146b5f5312210b1dfae35807e', config_dict)

place = 'Москва'  

mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
weather = observation.weather

temp = weather.temperature('celsius')['temp']
status = weather.detailed_status

print(f'В городе {place} сейчас {status}')
print(f'Температура в городе {temp}')