import random
from FullError import FullError
import numpy as np

class Board:
    def __init__(self, state=np.zeros(16, dtype=int), last=0):
        self.state = state[:]
        self.last = last
        self.lastarr = self.new_num()
        
        

    def new_num(self):
        
        if len(np.where(self.state==0)) == 0:
            raise FullError()
        empty = []
        # print(self.state)
        for i in range(len(self.state)):
            if self.state[i] == 0:
                empty.append(i)
        result = empty[random.randint(0, len(empty) - 1)]
        self.last = result
        self.state[result] = [2, 2, 2, 4][random.randint(0, 3)]
        lastarr = [' '] * 16
        lastarr[result] = '_'
        self.lastarr = lastarr
        return lastarr
    
    def copy(self):
        return Board(self.state[:])

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
'''.format(*self.state, *self.lastarr)
        return string
    
    def set_move(self, new_state):
        self.state = new_state[:]
        self.new_num()
    
    def move_left(self):
        temp = self.state[:]
        
        for i in range(4 ** 2):
            if i % 4 == 0:
                start = i
                continue
            else:
                if temp[i] == 0: continue
                else:
                    pos = i
                    compose = False
                    while pos > start:
                        
                        if temp[pos-1] == 0:
                            temp[pos-1], temp[pos] = temp[pos], temp[pos-1]
                            pos -= 1
                        elif temp[pos-1] == temp[pos] and not compose:
                            
                            temp[pos-1] *= 2
                            temp[pos] = 0
                            pos -= 1
                            compose = True
                        else:
                            break
        return temp
    
    def move_right(self):
        temp = self.state[:]
        
        for i in range(4**2 - 1, -1, -1):
            # print(i)
            if i % 4 == 4 - 1:
                start = i

                continue
            else:
                if temp[i] == 0: continue
                else:
                    pos = i
                    compose = False
                    while pos < start:
                        if temp[pos+1] == 0:
                            # print(pos, pos + 1)
                            temp[pos+1], temp[pos] = temp[pos], temp[pos+1]
                            pos += 1
                        elif temp[pos+1] == temp[pos] and not compose:
                            temp[pos+1] *= 2
                            temp[pos] = 0
                            pos += 1
                            compose = True
                        else:
                            break
        return temp
            
    def move_up(self):
        temp = self.state[:]
        numarr = []
        index = 0
        while len(numarr) < 4**2:
            index %= 4**2 - 1
            numarr.append(index)
            index += 4
        numarr[-1] = 4**2 - 1
        # print(numarr)

        for i in numarr:
            
            if i < 4:
                start = i
                continue
            else:
                if temp[i] == 0: continue
                else:
                    pos = i
                    compose = False
                    while pos > start:
                        if temp[pos-4] == 0:
                            temp[pos-4], temp[pos] = temp[pos], temp[pos-4]
                            pos -= 4
                        elif temp[pos-4] == temp[pos] and not compose:
                            temp[pos-4] *= 2
                            temp[pos] = 0
                            pos -= 4
                            compose = True
                        else: break
        return temp
    
    def move_down(self):
        temp = self.state[:]
        numarr = []
        index = 4**2 - 1
        while len(numarr) < 4**2:
            index %= 4**2 - 1
            numarr.append(index)
            index -= 4
        numarr[0] = 4**2 - 1
        # print(numarr)

        for i in numarr:
            
            if i >= 4**2 - 4:
                start = i
                continue
            else:
                if temp[i] == 0: continue
                else:
                    pos = i
                    compose = False
                    while pos < start:
                        if temp[pos+4] == 0:
                            temp[pos+4], temp[pos] = temp[pos], temp[pos+4]
                            pos += 4
                        elif temp[pos+4] == temp[pos] and not compose:
                            temp[pos+4] *= 2
                            temp[pos] = 0
                            pos += 4
                            compose = True
                        else: break
        return temp


if __name__ == '__main__':
    board = Board()
    print(board)
    # board.move_down()
    while True:
        text = input()
        if text == 'a': board.set_move(board.move_left())
        elif text == 'd': board.set_move(board.move_right())
        elif text == 'w': board.set_move(board.move_up())
        elif text == 's': board.set_move(board.move_down())
        print(board)
    