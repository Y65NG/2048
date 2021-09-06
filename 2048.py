import random

class Board:
    def __init__(self, dim):
        self.board = [0] * dim**2
        self.dim = dim
        self.last = 0
        self.lastarr = self.new_num()
        
        

    def new_num(self):
        empty = []
        # print(self.board)
        for i in range(len(self.board)):
            if self.board[i] == 0:
                empty.append(i)
        result = empty[random.randint(0, len(empty) - 1)]
        self.last = result
        self.board[result] = [2, 2, 2, 4][random.randint(0, 3)]
        lastarr = [' '] * self.dim**2
        lastarr[result] = '_'
        self.lastarr = lastarr
        return lastarr
        

    def __str__(self):
        string = '''
  {16}   {17}   {18}   {19}  
| {0} | {1} | {2} | {3} |
| {20}   {21}   {22}   {23} |
| {4} | {5} | {6} | {7} |
| {24}   {25}   {26}   {27} |
| {8} | {9} | {10} | {11} |
| {28}   {29}   {30}   {31} |
| {12} | {13} | {14} | {15} |
'''.format(*self.board, *self.lastarr)
        return string
    
    def move_left(self):
        
        for i in range(self.dim ** 2):
            if i % self.dim == 0:
                start = i
                continue
            else:
                if self.board[i] == 0: continue
                else:
                    pos = i
                    compose = False
                    while pos > start:
                        
                        if self.board[pos-1] == 0:
                            self.board[pos-1], self.board[pos] = self.board[pos], self.board[pos-1]
                            pos -= 1
                        elif self.board[pos-1] == self.board[pos] and not compose:
                            
                            self.board[pos-1] *= 2
                            self.board[pos] = 0
                            pos -= 1
                            compose = True
                        else:
                            break
        self.new_num()
    
    def move_right(self):
        
        for i in range(self.dim**2 - 1, -1, -1):
            # print(i)
            if i % self.dim == self.dim - 1:
                start = i

                continue
            else:
                if self.board[i] == 0: continue
                else:
                    pos = i
                    compose = False
                    while pos < start:
                        if self.board[pos+1] == 0:
                            # print(pos, pos + 1)
                            self.board[pos+1], self.board[pos] = self.board[pos], self.board[pos+1]
                            pos += 1
                        elif self.board[pos+1] == self.board[pos] and not compose:
                            self.board[pos+1] *= 2
                            self.board[pos] = 0
                            pos += 1
                            compose = True
                        else:
                            break
        self.new_num()
            
    def move_up(self):
        numarr = []
        index = 0
        while len(numarr) < self.dim**2:
            index %= self.dim**2 - 1
            numarr.append(index)
            index += 4
        numarr[-1] = self.dim**2 - 1
        # print(numarr)

        for i in numarr:
            
            if i < self.dim:
                start = i
                continue
            else:
                if self.board[i] == 0: continue
                else:
                    pos = i
                    compose = False
                    while pos > start:
                        if self.board[pos-4] == 0:
                            self.board[pos-4], self.board[pos] = self.board[pos], self.board[pos-4]
                            pos -= 4
                        elif self.board[pos-4] == self.board[pos] and not compose:
                            self.board[pos-4] *= 2
                            self.board[pos] = 0
                            pos -= 4
                            compose = True
                        else: break
        self.new_num()
    
    def move_down(self):
        numarr = []
        index = self.dim**2 - 1
        while len(numarr) < self.dim**2:
            index %= self.dim**2 - 1
            numarr.append(index)
            index -= 4
        numarr[0] = self.dim**2 - 1
        # print(numarr)

        for i in numarr:
            
            if i >= self.dim**2 - 4:
                start = i
                continue
            else:
                if self.board[i] == 0: continue
                else:
                    pos = i
                    compose = False
                    while pos < start:
                        if self.board[pos+4] == 0:
                            self.board[pos+4], self.board[pos] = self.board[pos], self.board[pos+4]
                            pos += 4
                        elif self.board[pos+4] == self.board[pos] and not compose:
                            self.board[pos+4] *= 2
                            self.board[pos] = 0
                            pos += 4
                            compose = True
                        else: break
        self.new_num()



board = Board(4)
print(board)
# board.move_down()
while True:
    text = input()
    if text == 'a': board.move_left()
    elif text == 'd': board.move_right()
    elif text == 'w': board.move_up()
    elif text == 's': board.move_down()
    print(board)

                
