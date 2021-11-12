from game import *

def evaluate(state):
    score = 0
    for i in state:
        if i == 0: score += 1
    return score

def move_d(b, depth, scs):
    s, last = b.state, b.last
    
    # print(s)
    if depth == 0:   
        return evaluate(s)

    else:
        b1, b2, b3, b4 = Board(s, last), Board(s, last), Board(s, last), Board(s, last)
        # print(depth)
        # print(b)
        try:
            b1.set_move(b1.move_up())
            scs[0] = move_d(b1, depth-1, scs)
        except:
            pass
        try:
            b2.set_move(b2.move_down())
            scs[1] = move_d(b2, depth-1, scs)
        except:
            pass
        try:
            b3.set_move(b3.move_left())
            scs[2] = move_d(b3, depth-1, scs)
        except:
            pass
        try:
            b4.set_move(b4.move_right())
            scs[3] = move_d(b4, depth-1, scs)
        except:
            pass
        # print(type(b1))
        
        max_sc = max(scs)
        return max_sc
        
        
def move(board):
    t1, t2, t3, t4 = Board(), Board(), Board(), Board()
    
    s1, s2, s3, s4 = evaluate(board.move_up()), evaluate(board.move_down()), evaluate(board.move_left()), evaluate(board.move_right())
    max_score = max(s1, s2, s3, s4)
    # print(max_score, s1, s2, s3, s4)
    if s1 == max_score:
        return board.move_up()
    if s2 == max_score:
        return board.move_down()
    if s3 == max_score:
        return board.move_left()
    if s4 == max_score:
        return board.move_right()

if __name__ == "__main__":
    DEPTH = 1
    board = Board()
    print(board)
    for i in range(100):
        scs = [0] * 4
        # board.set_move(move_d(board, DEPTH, scs))
        max_ind = scs.index(max(scs))
        if max_ind == 0:
            board.set_move(board.move_up())
        elif max_ind == 1:
            board.set_move(board.move_down())
        elif max_ind == 2:
            board.set_move(board.move_left())
        else:
            board.set_move(board.move_right())
        # board.set_move(np.array(move(board)))
        # board.move_left()
        print(board)
        