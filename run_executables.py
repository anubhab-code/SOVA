import os
import subprocess
from glob import glob
import time
import win32gui
import speech_recognition as sr
import wave
import pyaudio

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
r = sr.Recognizer()
r.energy_threshold=2500
r.operation_timeout = 2

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
    while True:
        with sr.Microphone() as source :
            print("Say something!")
            audio = r.listen( source )
        try:
            strr = r.recognize_google(audio)
            strr = strr.lower()
            return strr
        except sr.UnknownValueError:
            play_sound('sorry.wav')
            #print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

def run_executable(exec_name):
    exec_name = ''.join(exec_name.split(" "))
    exec_name += '.lnk'
    exec_name = exec_name.lower()

    result = [y for x in os.walk("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs") for y in glob(os.path.join(x[0], '*.lnk'))]

    shortcuts=[]
	
    index = 0
    for files in result:
    	index = files.rfind('\\') + 1
    	shortcuts.append(files[index:])
    nw_names=[]    
    for names in shortcuts:
    	nw_names.append(''.join(names.split(" ")).lower())

    if exec_name in nw_names:
        index = nw_names.index(exec_name)
        stri = shortcuts[index]
        cm = "start "+'"" '+'"'+'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\'+stri+'"'
        subprocess.Popen(cm, startupinfo=si,shell=True).wait()
        time.sleep(2)
        while True:
            strr = listenn()
            if strr=="close":
                w=win32gui
                cwn = w.GetWindowText(w.GetForegroundWindow())
                st = 'taskkill /FI "WINDOWTITLE eq '+cwn+'*"'
                subprocess.Popen(st, startupinfo=si,shell=True).wait()
                break
    else:
        play_sound('no_app.wav')
        #print('No such application found')
