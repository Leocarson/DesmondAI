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
command_list = "exit   play_TTT   help   open_(app_name)   app_list   Calculator   web   Command_Line   Update"
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
    elif command == "Update":
        webbrowser.open("https://github.com/Leocarson/DesmondAI")
        say("If any, download the new python file")
    elif command == "play_TTT":
        from random import randrange, random
        from time import sleep
        #First, setup the board!!

        def draw_board():
            print '', board[1], '|', board[2], '|', board[3], \
                  '\n-----------\n', \
                  '', board[4], '|', board[5], '|', board[6], \
                  '\n-----------\n', \
                  '', board[7], '|', board[8], '|', board[9], \
                  '\n'
        #Next, Choose what team you're on!

        def player_team():
            team = raw_input('Do you want to be X or O? \n').upper()
            print
            if team == 'X':
                return ['X', 'O']
            elif team == 'O':
                return ['O', 'X']
            else:
                print ('That is not a valid choice. Please try again \n')
                return player_team()
        #Next, Find out what player goes first!

        def first_turn():
            turn = random()
            if turn <= .494:
                say ('You will go first \n')
                return ('user', True)
            else:
                say ('The Computer will go first \n')
                return ('computer', False)
        #Next, be able to determine which spaces are available!

        def available(space):
            if board[space] == ' ':
                return True
        #Next, allow a player to pick their move!

        def user_turn():
            try:
                move = int(raw_input('Where would you like to move? (Enter a number from 1-9) \n'))
                if 0 < move < 10:
                    if not available(move):
                        say ('That space is already taken by a player. '
                               'Please select an open space \n')
                        return user_turn()
                    else:
                        board[move] = user_team
                        print
            except:
                say ('That is not a valid move. Please try again. \n')
                return user_turn()   
        #Now define the A.I!

        def computer_turn():
            move = randrange(1, 10)
            if available(move):
                board[move] = computer_team
                return move
            else:
                return computer_turn()
        #Next, we must check if the game has ended or not, and see who won!

        def end_game():
            for row in range(1, 10, 3):
                if not available(row):
                    if board[row] == board[row + 1] and board[row] == board[row + 2]:
                        return True
            for column in range(1, 4):
                if not available(column):
                    if board[column]== board[column + 3] and board[column] == board[column + 6]:
                        return True
            for diagonal in range(1, 10, 2):
                if not available(diagonal):
                    if (diagonal == 1 and board[diagonal] == board[diagonal + 4]
                        and board[diagonal] == board[diagonal + 8]):
                        return True
                    elif (diagonal == 3 and board[diagonal] == board[diagonal + 2]
                        and board[diagonal] == board[diagonal + 4]):
                        return True
            if board.count('X') + board.count('O') == 9:
                return 'Tie'

        def check_winner():
            global user_win, computer_win, ties
            if end_game() == 'Tie':
                ties += 1
                draw_board()
                say ("The game is a tie. You're going to have to try harder"
                       "\nif you wish to beat the computer! \n")
            elif end_game():
                if turn == 'user':
                    user_win += 1
                    draw_board()
                    print ('You won! \n')
                else:
                    computer_win += 1
                    draw_board()
                    say('The computer has won! But... We already knew'
                           'that would happen. (: \n')    
        #Finally, give the option of a New Game+!

        def play_again():
            restart = raw_input('Do you wish to play another game? Yes or no? \n').upper()
            
            if restart == 'YES':
                return True
            elif restart == 'NO':
                return False
            else:
                say('That is not a valid choice. Please try again. \n')
                return play_again()
        #Main Program:    

        say ('Welcome to my Impossible Tic-Tac-Toe game! You are of the bravest'
               ' of souls to take on my challenge, but only failure awaits you. \n')
        count = 1
        user_win, computer_win, ties = 0, 0, 0
        new_game = True
        while new_game:
            board = [' '] * 10
            user_team, computer_team = player_team()
            turn, strategy = first_turn()
            print 'Game', count, '\n'
            while not end_game():
                if turn == 'user':
                    draw_board()
                    user_turn()
                    check_winner()
                    turn = 'computer'
                else:
                    draw_board()
                    say ('The computer is thinking... \n')
                    sleep(1)
                    space_taken = computer_turn()
                    print ('The computer moved on space', space_taken, '\n')
                    check_winner()
                    turn = 'user'
            if not play_again():
                new_game = False
            count += 1
    
       
    else:
        say("no command with that name")
        
    




    

