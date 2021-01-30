import os
import subprocess
import organizebytype as oft
import wave
import pyaudio

is_open = 0
si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
path = os.getcwd()
par_path = ""

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

def open_folder(folder_name):
    try:
        global path,par_path
        st = 'start /MAX "" "'+path+folder_name+'"'
        close_this()
        subprocess.Popen(st, startupinfo=si,shell=True).wait()
        path += folder_name + "\\"
        par_path = os.path.abspath(os.path.join(path,os.pardir))
    except OSError:
        play_sound('folder_not_exists.wav')
        print('Folder Not Found')
        os.system("start /MAX "+par_path)

def open_drive(drive_name):
    global path,par_path
    path = drive_name+":\\"
    par_path = os.path.abspath(os.path.join(path,os.pardir))
    st = 'start /MAX "" '+drive_name+":"
    subprocess.Popen(st, startupinfo=si,shell=True).wait()

def open_file(file_name):
    global path,par_path
    par_path = path
    path += file_name
    st = 'start /MAX "" "'+path+'"'
    subprocess.Popen(st, startupinfo=si,shell=True).wait()

def close_this():
    global path,par_path
    pth = path[:len(path)-1]
    st = 'taskkill /FI "WINDOWTITLE eq '+pth+'*"'
    subprocess.Popen(st, startupinfo=si,shell=True).wait()
    
def close_current_folder():
    try:
        global path,par_path
        par_path = os.path.abspath(os.path.join(path,os.pardir))
        temp_path = r"{}".format(path)
        temp_path.replace('\\\\','\\')
        st = 'taskkill /FI "WINDOWTITLE eq '+os.path.abspath(temp_path)+'*"'
        subprocess.Popen(st, startupinfo=si,shell=True).wait()
        st = 'start /MAX "" "'+par_path+'"'
        subprocess.Popen(st, startupinfo=si,shell=True).wait()
        path = par_path
    except OSError:
        play_sound('folder_not_exists.wav')
        print("Folder Not Found !!")

def close_current_file(fileName):
    global path,par_path
    st = 'taskkill /FI "WINDOWTITLE eq '+fileName+'*'
    subprocess.Popen(st, startupinfo=si,shell=True).wait()
    par_path = os.path.abspath(os.path.join(path,os.pardir))
    path = par_path

def opening(li):
    global is_open,fil_name,path,par_path
    stri = ""
    open_flag = 0
    file_flag = 0
    drive_flag =  0
    folder_flag = 0
    str = " ".join(li)
    for st in li:
        if st=="open":
            open_flag = 1
        elif st=="drive":
            drive_flag = 1
            stri = li[1]
        elif st=="folder":
            folder_flag = 1
        elif st=="file":
            file_flag=1
                
        if len(li) == 0:
            print("Invalid command")
            break
        elif(open_flag==1 and drive_flag==1):
            open_drive(stri)
            break
        elif(open_flag==1 and folder_flag==1):
            li = li[2:]
            li = "".join(li).lower()
            file_list = os.listdir(path)
            nw_li=[]
            for i in file_list:
                tmp = i.split(" ")
                nw_li.append("".join(tmp).lower())
            if li in nw_li:
                stri = file_list[nw_li.index(li)]
            else :
                play_sound('folder_not_exists.wav')
                break
            open_folder(stri)
            break
        elif(open_flag==1 and file_flag==1):
            sz = len(li)
            li_n = li[2:sz-1]
            li_n = "".join(li_n).lower()
            li_n+='.'
            li_n+=li[-1]
            li_n = li_n.lower()
            file_list = os.listdir(path)
            nw_li=[]
            for i in file_list:
                tmp = i.split(" ")
                nw_li.append("".join(tmp).lower())
            if li_n in nw_li:
                stri = file_list[nw_li.index(li_n)]
            else :
                play_sound('file_not_exists.wav')
                break
            open_file(stri)
            fil_name = stri
            is_open=1
            break
        elif(str == "organize" or str == "organised"):
            oft.organize(path)
            break
        elif (str == "go back"):
            close_current_folder()
            break
        elif (str == "close") and is_open==0:
            close_this()
            break
        elif (str == "close") and is_open==1:
            print(fil_name)
            is_open=0
            close_current_file(fil_name)
        else:
            continue
