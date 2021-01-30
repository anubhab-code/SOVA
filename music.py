from selenium import webdriver
import requests
import bs4
import random
import time
import speech_recognition as sr
import wave
import pyaudio

r = sr.Recognizer()
r.energy_threshold=2000
r.operation_timeout = 2
st="next"

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

def listenn():
    global st
    while True:
        with sr.Microphone() as source :
            #print("Say something!")
            audio = r.listen( source )
        try:
            print(r.recognize_google(audio))
            strr = r.recognize_google(audio)
            strr = strr.lower()
            print(strr)
            if strr=="play":
                st="play"
                break
            elif strr=="pause":
                st="pause"
                break
            elif strr=="next":
                st="next"
                break
            elif strr=="close":
                st="close"
                break
            else:
                print("Unrecognised Command !!")
        except sr.UnknownValueError:
            #print("Google Speech Recognition could not understand audio")
            play_sound('sorry.wav')
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        except sr.TimeoutError as e:
            print("TimeOut Error !!")
    return

state = 1

query_url = "https://soundcloud.com/search/sounds?q="

def play_music(stir):
    def click():
        global state
        browser.find_element_by_css_selector('.sc-button-play.playButton.sc-button.m-stretch').click()
    choice = 0
    global st
    #Path for chromeDriver
    browser = webdriver.Chrome("E:\chromedriver.exe")
    browser.get("https://soundcloud.com")
    if stir.lower()=="sad":
        choice=1
    elif stir.lower()=="happy":
        choice=2
    elif stir.lower()=="excited":
        choice=3
    elif stir.lower()=="depressed":
        choice=4
    
    if choice == 0:
        browser.quit()
    print()
    # search according to the mood
    if choice == 1:
        url = query_url + "sad"
        request = requests.get(url)
        soup = bs4.BeautifulSoup(request.text, "lxml")
    
        tracks = soup.select("h2")[3:]
        track_links = []
        track_names = []
        
        for index, track in enumerate(tracks):
            track_links.append(track.a.get("href"))
            track_names.append(track.text)
            print()
        while True:
            if st=="next":
                choice = random.randint(0,5)
                print("Now playing: " + track_names[choice])
                browser.get("http://soundcloud.com" + track_links[choice])
                browser.find_element_by_css_selector('.sc-button-play.playButton.sc-button.m-stretch').click()
                state=1
                st="play"
                
            listenn()
            if st=="play" and state==0:
                state=1
                click()
            elif st=="pause" and state==1:
                state=0
                click()
            elif st=="close":
                state=0
                browser.quit()
                break
            time.sleep(1)
    
    elif choice == 2:
        url = query_url + "happy"
        request = requests.get(url)
        soup = bs4.BeautifulSoup(request.text, "lxml")
    
        tracks = soup.select("h2")[3:]
        track_links = []
        track_names = []
        
        for index, track in enumerate(tracks):
            track_links.append(track.a.get("href"))
            track_names.append(track.text)
            print()
        st="next"
        while True:
            if st=="next":
                choice = random.randint(0,5)
                print("Now playing: " + track_names[choice])
                browser.get("http://soundcloud.com" + track_links[choice])
                browser.find_element_by_css_selector('.sc-button-play.playButton.sc-button.m-stretch').click()
                state=1
                
            listenn()
            if st=="play" and state==0:
                state=1
                click()
            elif st=="pause" and state==1:
                state=0
                click()
            elif st=="close":
                state=0
                browser.quit()
                break
    elif choice == 3:
        url = query_url + "excited"
        request = requests.get(url)
        soup = bs4.BeautifulSoup(request.text, "lxml")
        
        tracks = soup.select("h2")[3:]
        track_links = []
        track_names = []
    
        for index, track in enumerate(tracks):
            track_links.append(track.a.get("href"))
            track_names.append(track.text)
            print()
        st="next"
        while True:
            if st=="next":
                choice = random.randint(0,5)
                print("Now playing: " + track_names[choice])
                browser.get("http://soundcloud.com" + track_links[choice])
                browser.find_element_by_css_selector('.sc-button-play.playButton.sc-button.m-stretch').click()
                state=1
    
            listenn()
            if st=="play" and state==0:
                state=1
                click()
            elif st=="pause" and state==1:
                state=0
                click()
            elif st=="close":
                state=0
                browser.quit()
                break
    
    elif choice == 1:
        url = query_url + "depressed"
        request = requests.get(url)
        soup = bs4.BeautifulSoup(request.text, "lxml")
    
        tracks = soup.select("h2")[3:]
        track_links = []
        track_names = []
        
        for index, track in enumerate(tracks):
            track_links.append(track.a.get("href"))
            track_names.append(track.text)
            print()
        st="next"
        while True:
            if st=="next":
                choice = random.randint(0,5)
                print("Now playing: " + track_names[choice])
                browser.get("http://soundcloud.com" + track_links[choice])
                browser.find_element_by_css_selector('.sc-button-play.playButton.sc-button.m-stretch').click()
                state=1
            listenn()
            if st=="play" and state==0:
                state=1
                click()
            elif st=="pause" and state==1:
                state=0
                click()
            elif st=="close":
                state=0
                browser.quit()
                break
