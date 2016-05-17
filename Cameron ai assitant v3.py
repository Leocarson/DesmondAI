import sys
import time
import os
import pyttsx
import webbrowser
import speech_recognition as sr
import Tkinter as tk
API_AI_CLIENT_ACCESS_TOKEN = "b4ed0c44a01740d1a0440abba185a1d1" # api.ai keys are 32-character lowercase hexadecimal strings
WIT_AI_KEY = "4KNQOUSF542XVFYLXM7TLYF5MJGR6"
r = sr.Recognizer()
engine = pyttsx.init()
voices = engine.getProperty('voices')
def say(text):
    try:
        genfile = open('gender.txt', 'r')
        gend = genfile.read()
        genfile.close()
        if gend == "male":
            engine.say(text)
            print text
            engine.runAndWait()
        elif gend == "female":
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            print text
            engine.runAndWait()       
    except IOError:
        engine.say(text)
        print text
        engine.runAndWait()

def say2(text, text2):
    try:
        genfile = open('gender.txt', 'r')
        gend = genfile.read()
        genfile.close()
        if gend == "male":
            engine.say(text + text2)
            print text + text2
            engine.runAndWait()
        elif gend == "female":
            engine.setProperty('voice', voices[1].id)
            engine.say(text + text2)
            print text + text2
            engine.runAndWait()       
    except IOError:
        engine.say(text + text2)
        print text + text2
        engine.runAndWait()
comaskfile = 'comask.txt'
namefile = 'name.txt'
# OR subprocess.call([r"C:\Windows\system32\shutdown.exe", "/t", str(time)])
#      specified the absolute path of the shutdown.exe
#      The path may vary according to the installation.
app_list = "Unity   Foldit   MusicBee   GW2   Arduino   Chrome   Firefox   NXT   Filezilla   iTunes    Steam   OBS   VLC   Skype   Python27   Word   Dropbox" 
command = ""
command_list = "leave   help   open (app name)   applications   Calculator   web   Command Line   Update   Settings"
try:
    nafile = open(namefile, 'r')
    name = nafile.read()
    nafile.close()
    say2("Welcome back, ", name)
except IOError:
    say("Hello, I am Cameron, your Personal AI Assistant")
    say("what is your name?")
    name = raw_input('>> ')
    say2("Hi ", name)
    nafile = open(namefile, 'w')
    nafile.write(name)
    nafile.close()
try:
    comask = open(comaskfile, 'r')
    com = comask.read()
    comask.close()
    if com != "no":
   
        while True:
            say("Would you like me to open the command list?(yes or no)")
            with sr.Microphone() as source:
                print "Say command"
                audio = r.listen(source)
            try:
                command = r.recognize_api(audio, client_access_token=API_AI_CLIENT_ACCESS_TOKEN)
            except sr.RequestError as e:
                command = r.recognize_wit(audio, key=WIT_AI_KEY)
            except sr.RequestError as e:
                command = r.recognize_google(audio)

                
                time.sleep(1)
            if command == "yes" :
                print command_list
                break
            elif command == "no":
                say("Would you like me to leave?(yes or no)")
                with sr.Microphone() as source:
                    print "Say command"
                    audio = r.listen(source)
                try:
                    command = r.recognize_api(audio, client_access_token=API_AI_CLIENT_ACCESS_TOKEN)
                except sr.RequestError as e:
                    command = r.recognize_wit(audio, key=WIT_AI_KEY)
                except sr.RequestError as e:
                    command = r.recognize_google(audio)
                if commandA == "yes":
                    sys.exit()
                else:
                    say("Ok")
                    break
            else:
                say("Please say yes or no")
                say("I think you said")
                say(command)

except IOError:   
    while True:
        say("Would you like me to open the command list?(yes or no)")
        with sr.Microphone() as source:
            print "Say command"
            audio = r.listen(source)
        try:
            command = r.recognize_api(audio, client_access_token=API_AI_CLIENT_ACCESS_TOKEN)
        except sr.RequestError as e:
            command = r.recognize_wit(audio, key=WIT_AI_KEY)
        except sr.RequestError as e:
            command = r.recognize_google(audio)

            
            time.sleep(1)
        if command == "yes" :
            print command_list
            break
        elif command == "no":
            say("Would you like me to leave?(yes or no)")
            with sr.Microphone() as source:
                print "Say command"
                audio = r.listen(source)
            try:
                command = r.recognize_api(audio, client_access_token=API_AI_CLIENT_ACCESS_TOKEN)
            except sr.RequestError as e:
                command = r.recognize_wit(audio, key=WIT_AI_KEY)
            except sr.RequestError as e:
                command = r.recognize_google(audio)
            if commandA == "yes":
                sys.exit()
            else:
                say("Ok")
                break
        else:
            say("Please say yes or no")
            say("I think you said")
            say(command)
while True:
    command = ""
    with sr.Microphone() as source:
            print "say command"
            audio = r.listen(source)   
    try:
        command = r.recognize_api(audio, client_access_token=API_AI_CLIENT_ACCESS_TOKEN)
    except sr.RequestError as e:
        command = r.recognize_wit(audio, key=WIT_AI_KEY)
    except sr.RequestError as e:
         command = r.recognize_google(audio)       
    if command == "leave" or command == "live" or command == "leave it":
        say("ok")
        sys.exit()
    elif command == "applications":
        print app_list
    elif command == "help":
        print command_list
    elif command == "open Unity" or command == "open unity" or command == "Open unity" or command == "Open Unity":
        os.startfile('C:\Program Files\Unity\Editor\Unity')
    elif command == "open foldit" or command == "open forget it" or command == "open phone app" or command == "open photos":
        os.startfile('C://Foldit/Foldit')
    elif command == "open guild wars 2":
        os.startfile('C://Program Files (x86)/Guild Wars 2/Gw2')
    elif command == "open Arduino" or command == "open we know" or command == "open agree now" or command == "open are doing now" or command == "open arduino" or command == "open or do you know":
        os.startfile('C://Program Files (x86)/Arduino/arduino')
    elif command == "open Chrome" or command == "open chrome":
        os.system('start chrome')
    elif command == "open iTunes" or command == "open itunes":
        os.startfile('C://Program Files/iTunes/iTunes')
    elif command == "open Steam" or command == "open steam":
        os.system('start steam:')
    elif command == "open Firefox" or command == "open firefox" or command == "open fire fox":
        os.startfile('C://Program Files (x86)/Mozilla Firefox/firefox')
    elif command == "open Filezilla" or command == "open file zelda" or command == "open file zilla" or command == "open filezilla" or command == "open files ella":
        os.startfile('C://Program Files/FileZilla FTP Client')
    elif command == "open NXT" or command == "open the t" or command == "open x t" or command == "open nxt" or command == "open n x t" or command == "open m a t" or command == "open a t":
        os.startfile('C://Program Files (x86)/LEGO Software/LEGO MINDSTORMS Edu NXT/MINDSTORMSNXT')
    elif command == "open OBS" or command == "open up yes" or command == "open o b s" or command == "open the yes":
        os.startfile('C://Program Files (x86)/OBS/OBS')
    elif command == "open VLC" or command == "open v l c" or command == "open v l v" or command == "open d l c" or command == "open we'll see" or command == "open v o c" or command == "open c" or command == "open the l c":
        os.startfile('C://Program Files (x86)/VideoLAN/VLC/vlc')
    elif command == "open Skype" or command == "open skype":
        os.startfile('C://Program Files (x86)/Skype/Phone/Skype')
    elif command == "Calculator" or command == "calculator":
        os.system('calc.exe')
    elif command == "open python 2.7" or command == "open place on two point seven" or command == "open play on two point seven" or command == "open python two point seven" or command == "open my phone two point seven" or command == "open play store two point seven":
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Python 2.7\IDLE (Python GUI)')
    elif command == "command line" or command == "command":
        say("Entering Command Line")
        while True:
            say("Enter a command for windows or exit")
            command = raw_input(">> ")
            if command == "exit":
                say("exiting")
                break
            os.system(command)
    elif command == "open word":
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word 2016')
    
    elif command == "web":
        say("going into web mode")
        while True:
            
            say("say website with out https:// or exit")
            with sr.Microphone() as source:
                print "Say command"
                audio = r.listen(source)
            try:
                website = r.recognize_api(audio, client_access_token=API_AI_CLIENT_ACCESS_TOKEN)
            except sr.RequestError as e:
                website = r.recognize_wit(audio, key=WIT_AI_KEY)
            if website == "exit":
                say("exiting")
                break
            webbrowser.open("https://" + website)
    elif command == "open dropbox" or command == "open drop box":
        os.startfile('C:\Program Files (x86)\Dropbox\DropboxOEM\DropboxOEM')
    elif command == "open musicBee" or command == "open music bee" or command[:10] == "open music":
        os.startfile('C:\Program Files (x86)\MusicBee\MusicBee')
    elif command == "update":
        webbrowser.open("https://github.com/Leocarson/DesmondAI")
        say("If any, download the new python file")
    elif command == "settings" or command == "set lights":
        say("for easy changing of settings this section will not use voice")
        while True:
            say("here are settings you can change or type exit to exit")
            print "Your Name   Voice Gender   Command List"
            setting = raw_input(">> ")
            if setting == "Your Name" or setting == "your name" or setting == "Your name" or setting == "your Name":
                name = raw_input(">> ")
                say ("ok your name is ")
                say (name)
                say ("I'll remember that")
                try:
                    nafile = open(namefile, 'w')
                    nafile.write(name)
                    nafile.close()
                    break
                except (NameError, ValueError, RuntimeError, IOError):
                    cats = "cats"
            elif setting == "Command List" or command == "command list" or command == "Command list" or command == "command List":
                say ("would you like to have me ask for the command list (y/n)")
                CL = raw_input('>> ')
                if CL == "y" or CL == "Y":
                    comask = open(comaskfile, 'w')
                    comask.write("y")
                    comask.close()
                else:
                    say ("ok, i will not say the command list at the beginning of the program")
                    comask = open(comaskfile, 'w')
                    comask.write('no')
                    comask.close()
            elif setting == "Voice Gender" or setting == "voice gender" or setting == "voice Gender" or setting == "Voice gender":
                while 1:
                    say("would you like male or female")
                    gen = raw_input(">> ")
                    if gen == "female" or gen == "Female":
                        say("ok")
                        genfile = open('gender.txt', 'w')
                        genfile.write("female")
                        genfile.close()
                        break
                    else:
                        say("ok")
                        genfile = open('gender.txt', 'w')
                        genfile.write("male")
                        genfile.close()
                        break
                    
                    
    elif command == "":
        say("cats")

    
       
    else:
        say("searching for")
        say(command)
        webbrowser.open(command)
        say("found it")
        
    




    

