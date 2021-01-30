class WindowMgr:
    def __init__ (self):
        self._handle = None
    def find_window(self, class_name, window_name=None):
        self._handle = win32gui.FindWindow(class_name, window_name)
    def _window_enum_callback(self, hwnd, wildcard):
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd
    def find_window_wildcard(self, wildcard):
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)
    def set_foreground(self):
        win32gui.SetForegroundWindow(self._handle)

import cv2
import re
import time
import win32gui
import threading
import pyaudio
import wave

def play_sound():
    chunk = 1024  
    f = wave.open(r"webcam.wav","rb")  
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

def openWebcam() :
    cv2.namedWindow("preview",cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("preview",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    vc = cv2.VideoCapture(0)
    w = WindowMgr()
    w.find_window_wildcard("preview")
    w.set_foreground()
    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False
    in_t = time.time()
    while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        en_t = time.time()
        if en_t-in_t>=5: # exit on ESC
            break
    cv2.destroyAllWindows()
    vc.release()

def trigger():
    t2 = threading.Thread(target=openWebcam)
    t1 = threading.Thread(target=play_sound)
    t2.start()
    time.sleep(1)
    t1.start()
    t1.join()
    t2.join()
