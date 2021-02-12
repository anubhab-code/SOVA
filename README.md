<p align="center"> 
<img src="https://camo.githubusercontent.com/c2c83648ee009d0c658825e63b29900a186829298a4c77d75863a9dc5229a777/687474703a2f2f692e696d6775722e636f6d2f785a38783945532e6a7067">
</p>


# S.O.V.A.
S.O.V.A. is our attempt to automate tasks performed on Microsoft Windows. It would help people not familiar with technology to operate computer systems relatively easily. People alien to this domain face difficulties in getting used to technology, S.O.V.A. here serves as a handy tool. S.O.V.A. performs all common tasks like opening applications, opening and closing files and folders, moving, renaming and organizing files, searching for files, compressing and decompressing files, changing system background, switching tabs, accessing utilities like webcam and microphone, shutting down the system etc. It also has additional features like playing music according to mood, reporting errors, etc.   

## Getting Started

You need a PC with Microsoft Windows support.

### Prerequisites

We need to install following libraries and environment before we begin our task.
```
python 3.6 or above
selenium
pipwin
winspeech
pyaudio
speech_recognition
wave
BeautifulSoup4
```
In case getting some error, install the required module.

### Healthy Practice : Setting Up a Virtual Environment
In order to avoid collisions during imports and other situations created due to different version requirements for different projects , it is often essential to build / create a virtual environment before trying to install project dependencies. You can easily do this using ```pip``` as :
  
  ```pip install venv```
  
Once ```venv``` is installed on your computer you can go forward to create a virtual environment for your project by executing the following command :

  ```python -m venv venv```
  
This command will create a folder named ```venv``` containing all the necessary scripts . The same folder is also going to store all our dependencies used in the project. Once the virtual environment is setup , you need to activate it . . .

```cd``` into the ```venv``` folder followed by the ```Scripts``` folder. And then use the ```activate``` command inside the ```Scripts``` folder.

  ```python cd venv/Scripts```
  
Once you are inside the Scripts folder , ```activate``` the virtual environment :
  
  ```/venv/Scripts/ > activate```
  
Or ```deactivate``` the virtual environment :

  ```/venv/Scripts/ > deactivate```

### Installing 

#### 1. Python
  From here install the latest version of Python for Windows [here](https://www.python.org/downloads/)
  
#### 2. Selenium 
```pip install selenium   #using pip```

Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires geckodriver, which needs to be installed before the below examples can be run. Make sure it’s in your PATH.

**Note:** Failure to observe this step will give you an error selenium.common.exceptions.WebDriverException: Message: ‘geckodriver’ executable needs to be in PATH.

We will be using Chrome WebDriver , you can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)

#### 3. Speech Recoginition

In order to use the SpeechRecognition Library for Windows you need to install an additional dependency called winspeech .

  ```pip install winspeech```
  
Now we can install the SpeechRecognition library

  ```pip install SpeechRecognition```
  
To use its functionality we need PyAudio (for microphone users) . For Windows , you once again need to install a system level dependency called ```pipwin```

  ```pip install pipwin```
  
Now we continue with our installation of PyAudio

  ```pip install pyaudio```

#### 4. BeautifulSoup4

  Use ```pip install beautifulsoup4``` to install it or 
   
  ```python -m pip install beautifulsoup4``` do the same work.

#### 5. wave

  Use ```pip install Wave``` to install wave.
  
 ## Features 
 
 * Performing Microsoft Windows operations and utilities
 * Working with file systems, performing all operations on files and folders, etc.
 * Play music according to mood 
 * Surfing the web using voice commands
 * Organizing files and maintaining todo lists 
 
 ## Running the tests
 
  ```python3 main.py``` or ```python main.py```
  
 Enjoy !!!
 
 ## Authors
 
 * **Anubhab Swain** [github](https://github.com/anubhab-code/)
 * **Ansh Sarkar** [github](https://github.com/ansh-sarkar/)
