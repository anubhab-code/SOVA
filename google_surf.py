from selenium import webdriver
import requests
import bs4
import random
import time
import speech_recognition as sr
from pynput.keyboard import Key,Controller
import wave
import pyaudio

keyboard = Controller()
r = sr.Recognizer()
r.energy_threshold=2500
r.operation_timeout = 2
num_list = ['one','two','to','too','three','four','five','1','2','3','4','5']
num_dic = {'one':1,'two':2,'three':3,'four':4,'five':5,'to':2,'too':2}


def play_sound(music_name):
    chunk = 1024  
    f = wave.open(r"{}".format(music_name),"rb")  
    p = pyaudio.PyAudio()  
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                    channels = f.getnchannels(),  
                    rate = f.getframerate(),  
                    output = True)  
    data = f.readframes(chunk)  
    while data:  
        stream.write(data)  
        data = f.readframes(chunk)  
    stream.stop_stream()  
    stream.close()  
    p.terminate() 


def back_click():
    keyboard.press(Key.alt)
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    keyboard.release(Key.alt)

def listenn():
    while True:
        with sr.Microphone() as source :
            #print("Say something!")
            audio = r.listen( source )
        try:
            strr = r.recognize_google(audio)
            strr = strr.lower()
            sx = strr.split(" ")
            if sx[0]=="open" and sx[2] in num_list:
                if len(sx[2])==1:
                    return int(sx[2])
                return num_dic[sx[2]]
            print(strr)
            return strr
        except sr.UnknownValueError:
            play_sound('sorry.wav')
            #print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

query_url = "https://google.com/search?q="

def search():
    browser = webdriver.Chrome("E:\chromedriver.exe")
    browser.get("https://google.com")
    st = listenn()
    if st=="close":
        browser.quit()
    st = st.split(" ")
    st = "+".join(st)
    url = query_url + st
    request = requests.get(url)
    browser.get(url)
    soup = bs4.BeautifulSoup(request.text, "lxml")
    tracks = soup.select("h3")[3:]
    track_links = []
    track_names = []

    for index, track in enumerate(tracks):
        track_links.append(track.a.get("href"))
        track_names.append(track.text)
    while True:
        choice = listenn()
        if choice == "close":
            browser.quit()
            break
        elif choice == "go back":
            back_click()
            continue
        elif choice == "scroll":
            tm_nw = time.time()
            while True:
                tm_tmp = time.time()
                if tm_tmp-tm_nw>0.01:
                    break
                keyboard.press(Key.down)
            keyboard.release(Key.down)
            continue
        print("Opening : " + track_names[choice])
        browser.get("http://google.com" + track_links[choice])
