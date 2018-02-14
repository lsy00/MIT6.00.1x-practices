import random

def readrecord():
    global score
    global record
    score = open('record.txt','r+')
    record = {}
    for l in score:
        temp = []
        s = l.split()
        for i in s[1:]:
            i = int(i)
            temp.append(i)
        record[s[0]] = temp
             
def request_name():
    '''ask for player's name
    '''
    global player
    player = input('Please enter your name ')    
        
def change_record():
    '''to record if the player win this time
    '''
    record[player][0] += 1
    if win > lose:
        print('You win! You score %d in %d goals.'%(win,roundnum))
        record[player][1] += 1
        record[player][2] += win
        record[player][3] += 1
    elif win<lose:
        print('You lose... Computer saved %d out of %d balls'%(lose,roundnum))
    else:
        print('Draw!')
        
def present_record():
    '''
        for old players:
            how many rounds the player has played
            how many rounds he has lost or win
        for new players:
            welcome and create a new record
     '''
    if player not in record.keys():
        record[player] = [0,0,0,0]    
    print('%s, you have played %d round, won %d round, score %d goals.\
You have %d coins.(You can consume coins for prediction)\n'\
              %(player,int(record[player][0]),int(record[player][1]),int(record[player][2]),\
                int(record[player][3])))

def game_procedure():
    global round_num
    global roundnum
    global win
    global lose
    print('=====Round %d====='%(abs(round_num-roundnum)))
    location = ['left','right','middle']
    com_ans = random.choice(location)
    if record[player][3] > 0:
        print('Use one coin to get prediction? You have %d coins now. '%(record[player][3]))
        ans = input('Enter y to use the coin, enter any other character to skip.') 
        if ans == 'y':
            print('The suggestion is everything except %s ' %(com_ans))
            record[player][3] -= 1
        else:
            print('Ok!')
    player_ans = input('which direction would you like to kick? ')
    if player_ans == com_ans:
        print('Oops!')
        round_num -= 1
        lose += 1
    elif player_ans != com_ans and player_ans in location:
        print('Yes!')
        round_num-=1
        win +=1
    else:
        print('Invalid command. Please try again')
        
def playgame():
    '''1. ask players name and show his record before
        2. ask how many rounds the player wants
           3. play the game
           4. ask if they want prediction if they have coin
           5. prediction
           6. show new record after finish the game
    '''
    readrecord()
    request_name()
    present_record()
    global round_num
    global roundnum
    global win
    global lose
    round_num = int(input('How many rounds would you like? '))
    roundnum = round_num
    win = 0
    lose = 0
    while round_num >0:
        game_procedure()
    change_record()
    present_record()
    write_record()

def write_record():
    '''write record into the file
    '''
    result = ''
    for n in record:
        line = player + ' '
        for i in record[player]:
            line += str(i)+' '
        result += line + '\n'
    score.write(result)
    score.close()
    

def startgame():
    while True:
        ans = input('enter s to start the game, e to exit the game ')
        if ans == 's':
            playgame()
        elif ans == 'e':
            print ('Byebye!')
            break
        else:
            print ('Invalid command. Please enter again ')


startgame()
