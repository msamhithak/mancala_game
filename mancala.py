class Mancala_Board:
    '''This is declaration of mancala board 4 for each player'''
    def __init__(self, mancala):
        if mancala != None:
            self.mancala = mancala[:]
        else:
            self.mancala = [0 for i in range(10)]
            for i in range(0,4):
                self.mancala[i] = 4
            for i in range(5,9):
                self.mancala[i] = 4

    '''This is called when player enters their move. This function finds whether the player gets another chance
    to play or not, adds the stones to pits and also checks if the last stone is ending in a empty pit of the 
    player and takes the opponents stones'''
    def player_move(self, i):
        j = i
        repeat_turn = False
        add = self.mancala[j]
        self.mancala[j] = 0
        if i > 4:
            stones = add
            while stones > 0:
                i += 1
                i = i % 10
                if i == 4:
                    continue
                else:
                    self.mancala[i % 10] += 1
                stones -= 1
            if i > 4 and self.mancala[i] == 1 and i != 9 and self.mancala[3-(i-5)] != 0:
                self.mancala[9] += 1 + self.mancala[4-(i-5)]
                self.mancala[i] = 0
                self.mancala[3-(i-5)] = 0
            if i == 9:
                repeat_turn = True
        else:
            stones = add
            while (stones > 0):
                i += 1
                i = i % 10
                if i == 9:
                    continue
                else:
                    self.mancala[i%10] += 1
                stones -= 1
            if i < 4 and self.mancala[i] == 1 and i !=4 and self.mancala[-i + 8]!=0:
                self.mancala[4] += 1 + self.mancala[-i + 8]
                self.mancala[i] = 0
                self.mancala[-i + 8] = 0
            if i == 4:
                repeat_turn = True
        return repeat_turn

    '''This function check if game is eanding or not, if one side of the board is empty then it means its 
    ending and it will return true, it also adds all the stones of opponent to winners manchala(excpt mancala)
    and also empties the pits of board except mancalas nd then returns '''
    def isEnd(self):
        if sum(self.mancala[0:4])==0 :
            self.mancala[9]+=sum(self.mancala[5:9])
            for i in range(10):
                if  (i != 9 and i != 4):
                    self.mancala[i] = 0
            return True
        elif sum(self.mancala[5:9])==0:
            self.mancala[4] += sum(self.mancala[0:4])
            for i in range(10):
                if  (i != 9 and i != 4):
                    self.mancala[i] = 0
            return True
        return False
    
    '''Prints the mancala board'''
    def print_mancala(self):
        for i in range(8,4,-1):
            print('  ', self.mancala[i], '   ', end = '')
        print('  ')
        print(self.mancala[9],'                           ',self.mancala[4])

        for i in range(0,4,1):
            print('  ', self.mancala[i], '   ', end='')
        print('  ')
        
    '''It executed only when the game is ending and it returns which player is winning.If it the positive value
    Ai is winning,if both have same number of stones then its returning 0, negative value indicates that the 
    opponent human player is winning. If the game is not ending it will return the differnce btw ai mancala and
    player mancala'''    
    def husVal(self):
        if self.isEnd():
            if self.mancala[9]>self.mancala[4]:
                return 100
            elif self.mancala[9]==self.mancala[4]:
                return 0
            else :
                 return -100
        else:
            return self.mancala[9]- self.mancala[4]

'''This is for AI BOT. First if the game is ending or if depth is 0 (tht means we reached the root of tree)
it will return which player is winning, else first it will check for possible move by checking if the pit has 0
stones or not then from 5 to 9 it will see all the possibilities nd store the best possibility(as it will return
this best possiblity) and also checks if alpha>beta to prune rest of the tree branches'''
def alphabeta(mancala, depth, alpha, beta , MinorMax):
    if depth == 0 or mancala.isEnd():
        return mancala.husVal(),-1
    '''Hus valuse is calculated here'''
    if MinorMax:
        v = -1000000
        player_move = -1
        for i in range(5,9,1):
            if mancala.mancala[i]==0: continue
            a = Mancala_Board(mancala.mancala[:])
            minormax = a.player_move(i)
            newv,_ =  alphabeta(a, depth-1, alpha, beta, minormax)
            'if the differnce that is returned from hus function if greater than v only then alpha value changes'
            if v < newv:
                player_move = i
                v = newv
            alpha = max(alpha, v)
            if alpha >= beta :
                break
        return v, player_move
    else:
        v = 1000000
        player_move = -1
        for i in range(0, 4, 1):
            if mancala.mancala[i] == 0: continue
            a = Mancala_Board(mancala.mancala[:])
            minormax = a.player_move(i)
            newv,_ = alphabeta(a, depth - 1, alpha, beta, not  minormax)
            if v > newv:
                player_move = i
                v = newv
            beta = min(beta, v)
            if alpha >= beta:
                break
        return v, player_move


'''This is 2nd part when player types 1 and from here it goes to the class mancala_board here j calls the init 
function of mancala board create the mancala board, if mancala is equal to None then only it creates board and 
it also calls print_macala to print the board initially'''
def player_aibot():
    j = Mancala_Board(None)
    j.print_mancala()
    while True:
        if j.isEnd():
            break
        while True:
            if j.isEnd():
                break
            h = int(input("YOUR TURN >>> "))
            if h > 3 or j.mancala[h] == 0:
                print("You can't Play at this position. Choose another position")
                continue
            t = j.player_move(h)
            j.print_mancala()
            if not t:
                break
        while True:
            if j.isEnd():
                break
            print("AI-BOT TURN >>> ", end = "")
            '''Alpha beta pruning is called here only for AI Bot turn'''
            _,k = alphabeta(j, 3, -100000, 100000, True)
            print(k)
            t = j.player_move(k)
            j.print_mancala()
            if not t:
                break
    if j.mancala[0] < j.mancala[9]:
        print("AI-BOT WINS")
    else:
        print("YOU WIN")
    print('GAME ENDED')
    j.print_mancala()

def Feedback():
    print("Give feedback")
    a=input()
    print("Thankyou for the feedback")

'''This is the beginning of code'''
print("\n:::: MANCALA BOARD GAME ::::")
print("!!! Welcome to Mancala Gameplay !!!")
while True:
    print("\nChoose:")
    print("(1) Player vs AI-Bot")
    print("(2) Feedback")
    type = int(input(">>> "))
    if type == 1:
        player_aibot()
        break
    elif type == 2:
        Feedback()
        break
    else:
        print("Wrong Gameplay Type. Enter Again")
        continue