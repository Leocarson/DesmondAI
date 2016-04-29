import sys
import time
import os
import pyttsx
import webbrowser
engine = pyttsx.init()
def say(text):
    engine.say(text)
    print text
    engine.runAndWait()
def shutdown():
    import subprocess
    time = 10
    subprocess.call(["shutdown.exe", "/t", str(time)]) # replaced `time` with `str(time)`
# OR subprocess.call([r"C:\Windows\system32\shutdown.exe", "/t", str(time)])
#      specified the absolute path of the shutdown.exe
#      The path may vary according to the installation.
app_list = "Unity   Foldit   MusicBee   GW2   Arduino   Chrome   Firefox   NXT   Filezilla   iTunes    Steam   OBS   VLC   Skype    Eyewire   Undertale   Python27   Word   Adobe_Fuse   Portal2   Dropbox   GoProStduio   GoPro   Trove" 
command = ""
command_list = "exit   play_TTT   help   open_(app_name)   app_list   Calculator   web   Command_Line"
say("Hello, I am Desmond, your Personal AI Assistant") 
while True:
    say("Would you like me to open the command list?(y or n)")
    command = raw_input('>> ')
    time.sleep(1)
    if command == "y" :
        
        say("OK")
        print "..."
        say("Here you go")
        print command_list
        break
    elif command == "n":
        say("Would you like me to leave?(y or n)")
        commandA = raw_input('>> ')
        if commandA == "y":
            sys.exit()
        else:
            say("Ok")
            break
    else:
        say("Please type y or n")
while True:
    say("Enter a command")
    command = raw_input('>> ')
    if command == "shutdown":
        say("are you sure?(y or n)")
        commandA = raw_input('>> ')
        if commandA == "y":
            say("ok, bye")
            time.sleep(1)
            shutdown()
        elif commandA == "n":
            say("ok")
        else:
            say("please type y or n")
    elif command == "app_list":
        print app_list
    elif command == "help":
        print command_list
    elif command == "open_Unity":
        os.startfile('C:\Program Files\Unity\Editor\Unity')
    elif command == "open_Foldit":
        os.startfile('C://Foldit/Foldit')
    elif command == "open_GW2":
        os.startfile('C://Program Files (x86)/Guild Wars 2/Gw2')
    elif command == "open_Arduino":
        os.startfile('C://Program Files (x86)/Arduino/arduino')
    elif command == "open_Chrome":
        os.startfile('C://Program Files (x86)/Google/Chrome/Application/chrome')
    elif command == "open_iTunes":
        os.startfile('C://Program Files/iTunes/iTunes')
    elif command == "open_Steam":
        os.startfile('C://Program Files (x86)/Steam/Steam')
    elif command == "open_Firefox":
        os.startfile('C://Program Files (x86)/Mozilla Firefox/firefox')
    elif command == "open_Filezilla":
        os.startfile('C://Program Files/FileZilla FTP Client')
    elif command == "open_NXT":
        os.startfile('C://Program Files (x86)/LEGO Software/LEGO MINDSTORMS Edu NXT/MINDSTORMSNXT')
    elif command == "open_OBS":
        os.startfile('C://Program Files (x86)/OBS/OBS')
    elif command == "open_OBS":
        os.startfile('C://Program Files (x86)/VideoLAN/VLC')
    elif command == "open_Skype":
        os.startfile('C://Program Files (x86)/Skype/Phone/Skype')
    elif command == "open_Eyewire":
        os.startfile('C://Users/kauch/Documents/Links/Eyewire.htm')
    elif command == "Calculator":
        os.system('calc.exe')
    elif command == "open_Python27":
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Python 2.7\IDLE (Python GUI)')
    elif command == "open_Undertale":
        os.startfile('steam://rungameid/391540')
    elif command == "Command_Line":
        say("Entering Command Line")
        while True:
            say("Enter a command for windows or exit")
            command = raw_input(">>")
            if command == "exit":
                say("exiting")
                break
            os.system(command)
    elif command == "open_word":
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word 2016')
    elif command == "Settings":
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Settings')
    
    elif command == "exit":
        say("ok")
        
        sys.exit()
    elif command == "web":
        say("going into web mode")
        while True:
            say("Input website with out https:// or exit")
            website = raw_input(">> ")
            if website == "exit":
                say("exiting")
                break
            webbrowser.open("https://" + website)
    elif command == "open_Adobe_Fuse":
        os.startfile('C:\Program Files (x86)\Adobe\Adobe Fuse CC (Preview)\Code\Build\Output\Fuse\bin\Release\Fuse')
    elif command == "open_Portal2":
        os.startfile('steam://rungameid/620')
    elif command == "open_Dropbox":
        os.startfile('C:\Program Files (x86)\Dropbox\DropboxOEM\DropboxOEM')
    elif command == "open_GoProStudio":
        os.startfile('C:\Program Files (x86)\GoPro\tools\GoPro Studio')
    elif command == "open_Trove":
        os.startfile('steam://rungameid/304050')
    elif command == "open_FaceRig":
        os.startfile('steam://rungameid/274920')
    elif command == "open_GoPro":
        os.startfile('C:\Program Files\GoPro\GoPro Desktop App\GoPro')
    elif command == "open_MusicBee":
        os.startfile('C:\Program Files (x86)\MusicBee\MusicBee')
    
    
            
    else:
        say("no command with that name")
        
    




    

