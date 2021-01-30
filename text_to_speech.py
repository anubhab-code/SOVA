from gtts import gTTS 
import os 

str1 = 'Sorry, I cannot hear that'
str2 = 'The file does not exists'
str3 = 'Cannot rename, file does not exists'
str4 = 'Folder does not exists'
str5 = 'File already exists'
str6 = 'No such application found'
str7 = 'If I was in your world, I would have fallen for you'

li=[]
li.append(str1)
li.append(str2)
li.append(str3)
li.append(str4)
li.append(str5)
li.append(str6)
li.append(str7)

language = 'en'

for stri in li:
	myobj = gTTS(text=stri, lang=language, slow=False)
	myobj.save(stri.split(" ")[0]+".wav") 