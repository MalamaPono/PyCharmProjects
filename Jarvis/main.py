import speech_recognition as sr
import pyttsx3
import pyaudio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import datetime
import wikipedia
import pyjokes
import time

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[33].id)

driver = webdriver.Chrome('/Users/malamapono/chromedriver')
executor_url = driver.command_executor._url
session_id = driver.session_id

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command(delay=False):
    command = ''
    try:
        with sr.Microphone() as source:
            if delay:
                talk('Yes')
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command

def run():
    global executor_url, session_id
    command = take_command()
    while 'siri' not in command:
        if command == 'quit':
            quit()
        command = take_command()
    command = take_command(True)
    if command.startswith('open'):
        driver2 = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
        driver2.session_id = session_id
        base_url = 'https://www.google.com/search?source=lnms&tbm=vid&q='
        channel = command.replace('open','') + ' channel'
        channel = channel.replace(' ', '%20')
        driver2.get(base_url + channel)
        video_element = driver2.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/a')
        video_element.click()
    elif command.startswith('play'):
        driver3 = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
        driver3.session_id = session_id
        song = command.replace('play', '')
        talk('playing ' + song)
        base_url = 'https://www.google.com/search?source=lnms&tbm=vid&q='
        song = song.replace(' ', '%20')
        driver3.get(base_url + song)
        video_element = driver3.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/a')
        video_element.click()
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('It is ' + current_time)
    elif 'who is' in command:
        search = command.replace('who is', '')
        info = wikipedia.summary(search,sentences=3)

        talk(info)
    elif 'what is' in command:
        search = command.replace('what is', '')
        info = wikipedia.summary(search,sentences=3)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke(category='twister'))
    elif 'stock' in command:
        driver4 = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
        driver4.session_id = session_id
        base_url = 'https://www.google.com/search?q='
        search = command.replace(' ','+')
        driver4.get(base_url + search)
        price = driver4.find_element(By.XPATH,'//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/div[2]/div[1]/span[1]/span/span[1]').text
        percent_change = driver4.find_element(By.XPATH,'//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/div[2]/div[1]/span[2]/span[2]/span[1]').text
        percent_change = float(percent_change[1:-2])
        driver4.close()
        if percent_change <= 0:
            direction = 'down'
        else:
            direction = 'up'
        stock = ' '.join(search.split('+')[0:2])
        quote = stock + f' is {direction} {percent_change} percent to {price}'
        talk(quote)
    else:
        talk('try again')


text = 'What can I do for you?'
talk(text)
while True:
    run()
