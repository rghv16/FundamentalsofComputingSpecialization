"""
Monte Carlo Tic-Tac-Toe Player
Raghav Aterya
raghavatreya16@gmail.com
http://www.codeskulptor.org/#user46_cRF2vsCB2FjV9R7_0.py
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 10         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.

def mc_trial(board, player):
    '''This function takes a current board and the next player to move. The function should play a game starting 
       with the given player by making random moves, alternating between players. 
       The function should return when the game is over. The modified board will contain the state of the game, 
       so the function does not return anything. In other words, the function should modify the board input.
    '''
    while board.check_win() is None:
        
        choice = random.choice(board.get_empty_squares())
        board.move(choice[0], choice[1], player)
        player = provided.switch_player(player)
    
    #print board.check_win()
    #print "board.get_dim() ",board.get_dim()
    

def mc_update_scores(scores,board,player):
    '''This function takes a grid of scores (a list of lists) with the same dimensions as the Tic-Tac-Toe board, 
    a board from a completed game, and which player the machine player is. The function should score the 
    completed board and update the scores grid. As the function updates the scores grid directly, it does not 
    return anything,
    '''
    player_score = 0
    oth_score = 0
    if board.check_win() == provided.DRAW:
        # no need to update the square
        return ()
    elif board.check_win() == player:
        player_score = 1
        oth_score = -1
    else:
        player_score = -1
        oth_score = 1
    
    dim = board.get_dim()
    other_player = provided.switch_player(player)
    for ind in range(dim):
        for jnd in range(dim):
            if board.square(ind, jnd) == player:
                scores[ind][jnd] += player_score
            elif board.square(ind, jnd) == other_player:
                scores[ind][jnd] += oth_score
     

    

def get_best_move(board,scores):
    '''This function takes a current board and a grid of scores. The function should find all of the empty 
    squares with the maximum score and randomly return one of them as a (row,column) tuple. It is an 
    error to call this function with a board that has no empty squares (there is no possible next move), 
    so your function may do whatever it wants in that case. The case where the board is full will not be tested.
    '''
    # {'key':[(row, col), (row, col)]}
    possible_move = {} 
    dimension =  board.get_dim()
    print "Number of empty squares are", board.get_empty_squares()
    if len(board.get_empty_squares()) == 0:
        return ()
    for ind in range(dimension):
        for jnd in range(dimension):
            num = scores[ind][jnd]
            if board.square(ind, jnd) != provided.EMPTY:
                continue
            print 'Empyt Square found'
            if num in possible_move:
                possible_move[num].append((ind, jnd))
            else:
                possible_move[num] = [(ind, jnd)]
    print possible_move
    key = max(possible_move)
    return random.choice(possible_move[key])  

def mc_move(board,player,trials):
    '''This function takes a current board, which player the machine player is, and the number of trials to run. 
    The function should use the Monte Carlo simulation described above to return a move for the machine player 
    in the form of a (row,column) tuple. Be sure to use the other functions you have written!
    '''
    # make the copy of board before passing the arguments
    scores = [ [0]*board.get_dim() 
               for _ in range(board.get_dim())] 
    
    for _ in range(trials):
        # call the mc_move function
        # check for the suitable
        test_board = board.clone()
        test_player = player
        mc_trial(test_board, test_player)
        mc_update_scores(scores, test_board, player)
    
    return get_best_move(board, scores)



# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
#mc_update_scores([[0, 0, 0], [0, 0, 0], [0, 0, 0]], provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERO, provided.PLAYERX, provided.EMPTY], [provided.EMPTY, provided.PLAYERX, provided.PLAYERO]]), 2)
# expected [[1.0, 1.0, -1.0], [-1.0, 1.0, 0], [0, 1.0, -1.0]] but received [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


#print  get_best_move(provided.TTTBoard(2, False, [[provided.EMPTY, provided.EMPTY], [provided.EMPTY, provided.EMPTY]]), [[13, 0], [3, 0]])

#print mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERO, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), provided.PLAYERX, NTRIALS)

#print mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERO, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), provided.PLAYERX, NTRIALS)

#print mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERO, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), provided.PLAYERX, NTRIALS)

