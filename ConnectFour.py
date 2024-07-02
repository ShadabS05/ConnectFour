import random
class Board:
    
    def __init__(self, width, height):
        """Construct a board of size width x height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for r in range(height)]

    def __repr__(self):
        """Return a string representation for an object of type Board.
        """
        s = ''                  # The string to return
        for row in range(self.height):
            s += '|'            # Add the spacer character
            for col in range(self.width):
                s += self.data[row][col] + '|'
            s += '\n'
        s += '--' * self.width  # Add the bottom of the board
        s += '-\n'
        for col in range(self.width):
            s += ' ' + str(col % 10) # Add labels
        s += '\n'
        return s                # The board is complete, return it

    def addMove(self, col, row, ox):
        """Add the game piece ox (either 'X' or 'O') to column col."""
        self.data[row][col] = ox
            
    def clear(self):
        """Clear the game board of all game pieces."""
        for x in range(0, self.height):
            for y in range(0, self.width):
                self.data[x][y] = " "
    def setBoard(self, moves):
        """Set the board using an input string representation."""
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moves:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'
    def allowsMove(self, col, row):
        """Return True if adding a game piece in the given move is
           permitted and return False otherwise."""
        if col >= self.width or col < 0:
            return False
        if row >= self.height or col < 0:
            return False
        if self.data[row][col] != " ":
            return False
        return True
    
    def isFull(self):
        """Return True if the game board is full and False otherwise."""
        count = 0
        for x in range(0, self.height):
            for y in range(0, self.width):
                if self.data[x][y] == " ":
                    count +=1
        if count != 0:
            return False
        else:
            return True 
    
    def delMove(self, col, row):
        """Delete the topmost game piece from the given column."""
        if self.data[row][col] != " ":
            self.data[row][col] = " "
    def inarow_Neast(self, ch, r_start, c_start, A, N):
        """Starting from (row, col) of (r_start, c_start)
        within the 2d list-of-lists A (array),
        returns True if there are N ch's in a row
        heading east and returns False otherwise.
        """
        H = len(A)
        W = len(A[0])
        if r_start < 0 or r_start > H - 1:
            return False            # Out-of-bounds row
        if c_start < 0 or c_start + (N-1) > W - 1:
            return False            # O.o.b. column
        # loop over each location _offset_ i
        for i in range(N):
            if A[r_start][c_start+i] != ch: # A mismatch!
                return False
        return True                 # All offsets succeeded, so we return True

    def inarow_Nsouth(self, ch, r_start, c_start, A, N):
        """Starting from (row, col) of (r_start, c_start)
        within the 2d list-of-lists A (array),
        returns True if there are N ch's in a row
        heading south and returns False otherwise.
        """
        H = len(A)
        W = len(A[0])
        if r_start < 0 or r_start + (N-1) > H - 1:
            return False # out of bounds row
        if c_start < 0 or c_start > W - 1:
            return False # o.o.b. col
        # loop over each location _offset_ i
        for i in range(N):
            if A[r_start+i][c_start] != ch: # A mismatch!
                return False
        return True                 # All offsets succeeded, so we return True

    def inarow_Nnortheast(self,ch, r_start, c_start, A, N):
        """Starting from (row, col) of (r_start, c_start)
        within the 2d list-of-lists A (array),
        returns True if there are N ch's in a row
        heading northeast and returns False otherwise.
        """
        H = len(A)
        W = len(A[0])
        if r_start - (N-1) < 0 or r_start > H - 1:
            return False # out of bounds row
        if c_start < 0 or c_start + (N-1) > W - 1:
            return False # o.o.b. col
        # loop over each location _offset_ i
        for i in range(N):
            if A[r_start-i][c_start+i] != ch: # A mismatch!
                return False
        return True                 # All offsets succeeded, so we return True

    def inarow_Nsoutheast(self, ch, r_start, c_start, A, N):
        """Starting from (row, col) of (r_start, c_start)
        within the 2d list-of-lists A (array),
        returns True if there are N ch's in a row
        heading southeast and returns False otherwise.
        """
        H = len(A)
        W = len(A[0])
        if r_start < 0 or r_start + (N-1) > H - 1:
            return False            # Out-of-bounds row
        if c_start < 0 or c_start + (N-1) > W - 1:
            return False            # O.o.b. column
        # loop over each location _offset_ i
        for i in range(N):
            if A[r_start+i][c_start+i] != ch: # A mismatch!
                return False
        return True    
       

    def winsFor(self, ox):
        """Return True if the game has been won by player ox where ox
           is either 'X' or 'O'."""
        H = self.height
        W = self.width
        D = self.data

        # Check to see if ox wins, starting from any checker:
        for row in range(H):
            for col in range(W):
                if self.inarow_Neast(ox, row, col, D, 3) == True:
                    return True
                elif self.inarow_Nnortheast(ox, row, col, D, 3) == True:
                    return True
                elif self.inarow_Nsouth(ox, row, col, D, 3) == True:
                    return True
                elif self.inarow_Nsoutheast(ox, row, col, D, 3) == True:
                    return True
            
        return False
               
    
    def spotToWin(self, ox):
        """Checks to see if this move allows one to win"""
        win_cols = []
        win_rows = []
        for x in range(self.width):
            for y in range(self.height):
                if self.allowsMove(x, y):
                    self.addMove(x, y, ox)
                    if self.winsFor(ox):
                        win_cols += [x]
                        win_rows += [y]
                    self.delMove(x, y)
        return win_cols, win_rows
    
    def aiMove(self, ox):
        """Chooses the move that the ai should move at based on possible winning moves"""
        if ox == 'X':
            opp_ox = 'O'
        else:
            opp_ox = 'X'
        x, y = self.spotToWin(ox)
        a, b = self.spotToWin(opp_ox)
        if self.isFull():
            return ''
        elif len(x) != 0:
            c = random.choice(x)
            index = x.index(c)
            return c, y[index]
        elif len(a) != 0:
            c = random.choice(a)
            index = a.index(c)
            return c, b[index]
        else:
            d, e = random.choice(range(self.width)), random.choice(range(self.width))
            while self.allowsMove(d,e) != True:
                d, e = random.choice(range(self.width)), random.choice(range(self.width))
            return d, e
               
    def hostGamezero(self):
        """hosts the tic tac toe game for 0 players"""
        while (self.winsFor('X') != True) and (self.winsFor('O') != True):
            users_col = -1    # Note! This -1 is _intentionally_ not valid!
            users_row = -1
            print(self)
            while self.allowsMove(users_col, users_row) == False: # _while_ not valid
                while self.isFull != True:
                    try:
                        users_col, users_row = self.aiMove('X')
                        self.addMove(users_col, users_row, 'X')
                    except:
                        print("No Valid Moves")
                    print(self)
                    if self.winsFor('X'):
                        print(self)
                        print("X Wins")
                        break
                    try:
                        f, g = self.aiMove('O')
                        self.addMove(f, g, 'O')
                    except:
                        print("No Valid Moves")
                    if self.winsFor('O'):
                        print(self)
                        print("O Wins")
                        break
                    print(self)
                break
            break

    def hostGame(self):
        """hosts the tic tac toe game for 1 player"""
        while (self.winsFor('X') != True) and (self.winsFor('O') != True):
            
            users_col = -1    # Note! This -1 is _intentionally_ not valid!
            users_row = -1
            print(self)
            while self.allowsMove(users_col, users_row) == False: # _while_ not valid
                while self.isFull != True:
                    users_col = int(input("X Choose a column: "))  # ask for a column
                    users_row = int(input("X Choose a row: "))  # ask for a column
                    self.addMove(users_col, users_row, 'X')
                    print(self)
                    if self.winsFor('X'):
                        print(self)
                        print("X Wins")
                        break
                    f, g = self.aiMove('O')
                    self.addMove(f, g, 'O')
                    if self.winsFor('O'):
                        print(self)
                        print("O Wins")
                        break
                    print(self)
                break
            break
    
    def hostGametwo(self):
        """hosts the tic tac toe game for 2 players"""
        while (self.winsFor('X') != True) and (self.winsFor('O') != True):
            
            users_col = -1    # Note! This -1 is _intentionally_ not valid!
            users_row = -1
            print(self)
            while self.allowsMove(users_col, users_row) == False: # _while_ not valid
                while self.isFull != True:
                    users_col = int(input("X Choose a column: "))  # ask for a column
                    users_row = int(input("X Choose a row: "))  # ask for a column
                    self.addMove(users_col, users_row, 'X')
                    print(self)
                    if self.winsFor('X'):
                        print(self)
                        print("X Wins")
                        break
                    f = int(input("O Choose a column: "))
                    g = int(input("O Choose a row: "))
                    self.addMove(f, g, 'O')
                    if self.winsFor('O'):
                        print(self)
                        print("O Wins")
                        break
                    print(self)
                break 
            break
    def menu(self):
        """Shows the Menu for the tic tac toe game"""
        scoreo = 0
        scorex = 0
        game = True
        while game == True:
            print("Welcome to Welcome to Tic Tac Toe")
            print("Menu Option 1: Play Game")
            print("Menu Option 3: Quit")
            print("Score for X:", scorex)
            print("Score for O:", scoreo)
            option = int(input("Insert Option: "))
            if option == 3:
                print("Goodbye! Thanks for playing!")
                game = False
            elif option == 1:
                new_option = int(input("How Many Players are playing? "))
                if new_option == 0:
                    try:
                        self.clear()
                        self.hostGamezero()
                        if self.winsFor('X') == True:
                            scorex +=1
                        elif self.winsFor('O') == True:
                            scoreo +=1
                    except IndexError:
                        print("Invalid Move!")
                        self.hostGamezero()
                    except:
                        print("Game is Over")
                    new_option = 4
                elif new_option == 1:
                    try:
                        self.clear()
                        self.hostGame()
                        if self.winsFor('X') == True:
                            scorex +=1
                        elif self.winsFor('O') == True:
                            scoreo +=1
                    except IndexError:
                        print("Invald Move")
                        self.hostGame()
                    except:
                        print("Game Is Over")
                    new_option = 4
                elif new_option == 2:
                    try:
                        self.clear()
                        self.hostGametwo()
                        if self.winsFor('X') == True:
                            scorex +=1
                        elif self.winsFor('O') == True:
                            scoreo +=1
                    except IndexError:
                        print("Invalid Move")
                        self.hostGametwo()
                    except:
                        print("Game is Full")
                    new_option = 4
                elif new_option == 3:
                    print("Invalid Number of Players, sorry!")
                elif new_option == 4:
                    break
            else:
                print("Invalid Option, Try Again!")


               
            
                        
                     