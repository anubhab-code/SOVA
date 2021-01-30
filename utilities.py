import zipfile
import os
import subprocess
from pynput.keyboard import Key, Controller
import time
import ctypes
import struct
import random
import wave
import pyaudio

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

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


def compress_file(path):
    ind = path.rfind("\\")
    zpath = path[:ind]
    zpath += "\\" 
    li = []
    li = path.split("\\")
    zpath += path.split("\\")[len(li) - 1] + ".zip"
    
    fzip = zipfile.ZipFile(zpath, 'w')
    
    for folder, subfolders, files in os.walk(path):
        for file in files:
            fzip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), path), compress_type = zipfile.ZIP_DEFLATED)
    
    fzip.close()

def decompress_file(path):
    ind = path.rfind(".")
    dpath = path[:ind]
    fzip = zipfile.ZipFile(path)
    fzip.extractall(dpath)
    fzip.close()

def tabs_switching_operation() :
    keyboard = Controller()
    keyboard.press(Key.alt)
    time.sleep(0.5)
    keyboard.press(Key.tab)
    time.sleep(0.5)
    keyboard.release(Key.tab)
    keyboard.release(Key.alt)  

def search_file(path, file_name):
    #path is the path of directory where file is located
    file_list = os.listdir(path)
    if file_name in file_list:
        print("File Exists in: ", path)
    else:
        play_sound('file_not_exists.wav')
        #print("File not found")

def rename_file(path, file_name, after_rename):
    file_list = os.listdir(path)

    if file_name in file_list:
        if(after_rename == file_name):
            play_sound('file_exists.wav')
            #print('File already exists')
        cur_path = path+'/'+file_name
        renamed_path = path+'/'+after_rename
        os.rename(cur_path, renamed_path)
    else :
        play_sound('cannot_rename.wav')
        #print("Cannot rename file! File does not exist")

def shutdown():
    subprocess.Popen("shutdown /s", startupinfo=si, shell=True).wait()

def restart():
    subprocess.Popen("shutdown /r", startupinfo=si, shell=True).wait()

def is_64_windows():
    return struct.calcsize('P') * 8 == 64

def get_sys_parameters_info():
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA
        
def change_wallpaper(path):
    SPI_SETDESKWALLPAPER = 20
    li = []
    li = os.listdir(path)
    sys_parameters_info = get_sys_parameters_info()
    sz = len(li)
    index = random.randint(0, sz - 1)
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, path + "\\"+li[index], 3)
    if not r:
        print(ctypes.WinError())
