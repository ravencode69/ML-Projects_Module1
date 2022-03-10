import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get(
    'https://forecast.weather.gov/MapClick.php?lat=38.89759000000004&lon=-77.03664999999995')
soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(id='seven-day-forecast-body')
items = week.find_all(class_='tombstone-container')
# print(items[0].find(class_='period-name').get_text())
# print(items[0].find(class_='short-desc').get_text())
# print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
short_desc = [item.find(class_='short-desc').get_text() for item in items]
tem = [item.find(class_='temp').get_text() for item in items]
print(period_names)
print(tem)
print(short_desc)

weather_thing = pd.DataFrame({
    'period': period_names,
    'short_des': short_desc,
    'temp': tem,
})

print(weather_thing)
weather_thing.to_csv('weather.csv')
