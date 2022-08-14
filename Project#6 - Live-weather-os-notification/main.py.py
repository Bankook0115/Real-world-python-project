#24/08/21
#Import module
import requests as rq
from selenium import webdriver
import time
from win10toast import ToastNotifier
import sys
from selenium.webdriver.common.by import By
#define class

n = ToastNotifier() #Create Notifier class
browser = webdriver.Edge()
browser.get("https://weather.com/en-IN/weather/today/l/90167a6786f20df27e576333d9c2d301d0c57fae542c922cefee82c8355bb6ea")
html = browser.page_source

time.sleep(1)

temp_value = browser.find_element(By.CLASS_NAME,"CurrentConditions--tempValue--3a50n") #element data type
temp_phrase = browser.find_element(By.CLASS_NAME,"CurrentConditions--phraseValue--2Z18W")
feel_like = browser.find_element(By.CLASS_NAME,"TodayDetailsCard--feelsLikeTempValue--Cf9Sl")
#convert to text
text_temp_value = str(temp_value.text)
text_temp_phrase = str(temp_phrase.text)
text_feel_like = str(feel_like.text)
result = "Current Temperature in Khlong Luang, \nPathum Thani is  " + text_temp_value + "\nWeather condition : " + text_temp_phrase + "\nToday feel like : " + text_feel_like
#print(result)
#print(html)
browser.close()
#Make notification on window 10
n.show_toast("Weather update", result, duration = 10)
quit()

